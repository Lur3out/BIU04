from enums import CommandType
import json
from json import JSONEncoder

class CommandEncoder(JSONEncoder):
    def default(self, obj):
        return obj.toJSON()

class Command():
    def __init__(self, type, target=None, option=None, value=None):
        self.command = {}
        if type is not None:
            self.command["type"] = type
        if target is not None:
            self.command["device"] = target
        if option is not None:
            self.command["option"] = option
        if target is not None:
            self.command["value"] = value

    def setTarget(self, target):
        self.command["device"] = target

    def setOption(self, option):
        self.command["option"] = option
    
    def setValue(self, value):
        self.command["value"] = value

    def toJson(self):
        return json.dumps(self.command, default=lambda o: o.__dict__, 
            sort_keys=True, separators=(',', ':'))
