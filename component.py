import serial
import time

class Component():
    device = ""
    baudrate = 9600
    name = ""
    def __init__(self, device=None, name=""):
        self.device = device
        self.name = name

    def send(self, command):
        print(self.device)
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
                    print ("opening error")

            except KeyboardInterrupt:
                print("Interrupted")

            finally:
                uno.close()