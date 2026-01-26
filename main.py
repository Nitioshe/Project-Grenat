from ui.intro import start_animation
from classes.player import Player
from core.game import game_loop


def create_character():
    name = input("Name: ") or "Numa"
    race = input("Race (Human/Elf/Dwarf): ").capitalize()
    player_class = input("Class (Mage/Rogue/Samuraï): ").capitalize()
    return Player(name, race, player_class)


def main():
    start_animation()

    player = create_character()

    game_loop(player)


if __name__ == "__main__":
    main()
