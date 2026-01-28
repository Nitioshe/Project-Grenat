"""
Docstring for main module
"""
from ui.intro import start_animation
from ui.menu import main_menu
from classes.player import Player
from classes.inventory import Inventory
from core.game import game_loop
from core.save import load_game
from core.save import save_game


def create_character():
    """
    Docstring for create_character

        character creation logic
    """
    name = input("Name: ") or "Numa"
    race = input("Race (Human/Elf/Dwarf): ").capitalize() or "Human"
    player_class = input("Class (Mage/Rogue/Warrior/Samuraï): ").capitalize() or "Warrior"
    return Player(name, race, player_class)


def main():
    """
    Docstring for main
        main function for game
    """
    start_animation()

    choice = main_menu()

    if choice == "load":
        player = load_game()

        if player is None:
            print("No save found.")
            return
    else:
        inventory = Inventory()
        player = create_character()

    game_loop(player)


if __name__ == "__main__":
    main()
