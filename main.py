"""
Docstring for main module
"""
from ui.intro import start_animation
from ui.menu import main_menu
from classes.player import Player
from core.game import game_loop
from core.save import load_game, save_game
from core.discord_rpc import start_rpc, stop_rpc

def create_character():
    """
    Character creation logic
    """
    name = input("Name: ") or "Numa"
    race = input("Race (Human/Elf/Dwarf): ").capitalize() or "Human"
    player_class = input("Class (Mage/Rogue/Warrior/Samurai): ").capitalize() or "Warrior"
    return Player(name, race, player_class)


def main():
    """
    Main entry point
    """
    start_rpc()
    start_animation()

    choice = main_menu()

    if choice == "new":
        print("\n=    Character Creation Menu    =\n")
        player = create_character()

    if choice == "load":
        player = load_game()

        if player is None:
            print("No save found.")
            return

    if choice == "quit":
        print("\nQuit Game.")
        return

    try:
        game_loop(player)
    finally:
        stop_rpc()
        save_game(player)


if __name__ == "__main__":
    main()
