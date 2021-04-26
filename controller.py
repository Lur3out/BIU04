import serial
import sys
import time
import keyboard 
from processing import debounce, throttle

# add user to dialout group
port = "/dev/ttyS0"
baudrate = 115200
cond = 1

with serial.Serial(port, baudrate) as uno:
    time.sleep(0.005)

    @throttle(interval=1) #seconds
    def write(msg, data):
        print(msg)
        uno.write(data)

    try:
        while cond:
            if keyboard.is_pressed('q'):
                write("Enable blue", b'\x01')
            elif keyboard.is_pressed('e'):
                write("Enable green", b'\x02')
            elif keyboard.is_pressed('esc'):
                break
            
            uno.flush()
            time.sleep(0.01)

    except KeyboardInterrupt:
        print("Interrupted")

    finally:
        uno.close()