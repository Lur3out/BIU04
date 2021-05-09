import serial
import time
import sys
from enums import CommandType
from command import Command
import json
from testing import Test

class Component(Test):
    device = ""
    baudrate = 9600
    name = ""
    def __init__(self, device=None, name=""):
        self.device = device
        self.name = name

    def log(self, *args, **kwargs):
        print(*args, file=sys.stderr, **kwargs)

    def send(self, command):
        with serial.Serial(self.device, 
            self.baudrate,
            parity=serial.PARITY_NONE, 
            bytesize=serial.EIGHTBITS, 
            stopbits=serial.STOPBITS_ONE) as uno:

            try:
                data = command.toJson()

                if uno.isOpen():
                    # During reboot sended data is recieved by setup func. 
                    # Delay average 5 sec
                    # Reqiered delay for Ardiuno reboot. 
                    time.sleep(2)  
                    try:
                        uno.write(data.encode('ascii'))
                    except Exception as e:
                        print (e)
                        uno.close() 
                        pass
                else:
                    log("Controller opening error")

            except KeyboardInterrupt:
                print("Interrupted")

            finally:
                uno.close()

    def ping(self):
        result = False
        with serial.Serial(self.device, 
            self.baudrate,
            parity=serial.PARITY_NONE, 
            bytesize=serial.EIGHTBITS, 
            stopbits=serial.STOPBITS_ONE) as uno:

            try:
                command = Command(type=CommandType.Ping)
                data = command.toJson()

                if uno.isOpen():
                    # During reboot sended data is recieved by setup func. 
                    # Delay average 5 sec
                    # Reqiered delay for Ardiuno reboot. 
                    time.sleep(2)  
                    try:
                        uno.write(data.encode('ascii'))
                        incoming = uno.readline()
                        pong = json.loads(incoming.decode("utf-8"))["Pong"]
                        result = pong == 'True'
                    except Exception as e:
                        print(e, file=sys.stderr)
                        uno.close() 
                        pass
                else:
                    log("Controller opening error")

            except KeyboardInterrupt:
                print("Interrupted")

            finally:
                uno.close()

        return result
