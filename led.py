from enums import Color, CommandType
from command import Command
from component import Component

class LED(Component):
    color = Color.Blue
    def __init__(self, device, name):
        super(LED, self).__init__(device, name)

    def setColor(self, color=Color.Blue):
        self.color = color
        try:
            command = Command(type=CommandType.Set, target=self.name, option="color", value=color)
            print(command.toJson())
            self.send(command)
        except Exception as e:
            print(e)
            
