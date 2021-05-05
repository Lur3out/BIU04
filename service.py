import pyudev
import os
import json
import serial
import sys
import time
import keyboard
from enums import CommandType 
from command import Command, CommandEncoder

baudrate = 9600

context = pyudev.Context()
monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by(subsystem='usb')

devices = {}

def interview_contoller(port):
    global devices
    with serial.Serial(port, 
            baudrate,
            parity=serial.PARITY_NONE, 
            bytesize=serial.EIGHTBITS, 
            stopbits=serial.STOPBITS_ONE) as uno:

        try:
            data = Command(type=CommandType.Init).toJson()

            if uno.isOpen():
                # During reboot sended data is recieved by setup func. 
                # Delay average 5 sec
                # Reqiered delay for Ardiuno reboot. 
                time.sleep(2)

                uno.write(data.encode('ascii'))
                try:
                    incoming = uno.readline()
                    array = json.loads(incoming.decode("utf-8"))["devices"]
                    devices = list(map(lambda e: e, array))
                except Exception as e:
                    print(e)
                    uno.close() 
                    pass
            else:
                print ("opening error")

        except KeyboardInterrupt:
            print("Interrupted")

        finally:
            uno.close()          

def create_device(device, controller):
    path = f'/dev/robot/{device["type"]}'
    file = f'{path}/{device["name"]}'
    os.makedirs(path, exist_ok=True)
    os.symlink(controller, file)


for device in iter(monitor.poll, None):
    if device.action == 'add' and device.device_type == 'usb_interface':
        devs = list(filter(lambda f: f.startswith('tty'), os.listdir(device.sys_path)))
        for dev in devs:
            path = os.path.join('/dev', devs[0])
            interview_contoller(path)
            for component in devices:
                create_device(component, path)