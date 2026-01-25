import json
from ui.intro import start_animation
from classes.player import Player
from classes.inventory import Inventory
from zones.tettno import Tettno_main
from zones.forest import Forest
from zones.bank import Bank
from zones.guild import AdventurersGuild
from core.game import game_loop

def create_character():
    name = input("Name: ") or "Numa"
    race = input("Race (Human/Elf/Dwarf): ").capitalize()
    player_class = input("Class (Mage/Rogue/Samuraï): ").capitalize()
    return Player(name, race, player_class)

def main():
    start_animation()

    inventory = Inventory()
    inventory.load()

    player = create_character()

    game_loop(player)

if __name__ == "__main__":
    main()
