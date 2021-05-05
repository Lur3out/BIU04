from led import LED
from command import Command
from enums import Color, CommandType

"""
  Simple example
"""
led = LED("/dev/robot/rgb/rgb1", "rgb1")
led.setColor(Color.Blue)
