from enum import Enum, auto

class GameState(Enum):
    MENU = auto()
    TOWN = auto()
    FOREST = auto()
    COMBAT = auto()
    GUILD = auto()
    BANK = auto()
    INVENTORY = auto()
    EXIT = auto()
