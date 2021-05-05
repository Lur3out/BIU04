import serial
import sys
import time
import keyboard 
import json
# import pyudev
from decorator import debounce, throttle

port = "COM3"
baudrate = 9600
cond = 1

with serial.Serial(port, 
            baudrate,
            parity=serial.PARITY_NONE, 
            bytesize=serial.EIGHTBITS, 
            stopbits=serial.STOPBITS_ONE) as uno:

    @throttle(interval=1) #seconds
    def write(msg, data):
        print(msg)
        uno.write(data)

    try:
        # while cond:
            # if keyboard.is_pressed('q'):
            #     write("Enable blue", b'\x01')
            # elif keyboard.is_pressed('e'):
            #     write("Enable green", b'\x02')
            # elif keyboard.is_pressed('esc'):
            #     break
        data = {}
        data["operation"] = "sequence"

        data=json.dumps(data)
        print (data)
        if uno.isOpen():
            time.sleep(2) #Reqiered delay for Ardiuno reboot. During reboot sended data is recieved by setup func. Delay average 5 sec
            uno.write(data.encode('ascii'))
            while cond:
                try:
                    # uno.flush()
                    incoming = uno.readline()
                    decoded = incoming.decode("utf-8")
                    print (incoming)
                    print (decoded)
                    time.sleep(0.01)
                    cond = 0
                except Exception as e:
                    print (e)
                    pass
        else:
            print ("opening error")

    except KeyboardInterrupt:
        print("Interrupted")

    finally:
        uno.close()