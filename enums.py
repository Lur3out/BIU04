from enum import Enum

class Color(str, Enum):
    Red = "r"
    Green = "g"
    Blue = "b"

class CommandType(str, Enum):
    Init = "init"
    Set = "set"