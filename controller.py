from led import LED
from command import Command
from enums import Color, CommandType


led = LED("/dev/robot/rgb/rgb1", "rgb1")
led.setColor(Color.Blue)
