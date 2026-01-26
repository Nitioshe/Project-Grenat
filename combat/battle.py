import random
import time
from core.audio import jouer_bruit
from core.state import GameState


def battle(player, monster):
    poison = 0
    poison_active = False
    stun = 0

    print("\nBattle Start!")
    print(f"{monster.name} appears.")

    while player.health > 0 and monster.health > 0:

        print("\n╔----------------------╗")
        print(f"{player.name} HP: {player.health}/{player.max_health}")
        print(f"    {monster.name} HP: {monster.health}")
        print("╚----------------------╝")

        print("1. Attack\n2. Inventory\n3. Flee")

        choice = input("> ")

        # ================= PLAYER TURN ================= #

        if choice == "1":
            damage = random.randint(player.attack // 2, player.attack)
            monster.health -= damage
            jouer_bruit("Sound Effect/attack-sound.mp3")
            print(f"{player.name} attacks {monster.name} for {damage}")

            if poison_active:
                poison_damage = random.randint(1, poison * 2)
                monster.health -= poison_damage
                print(f"{monster.name} suffers {poison_damage} poison damage")

        elif choice == "2":
            player.inventory.display_inventory()
            input("Press Enter to continue...")

        elif choice == "3":
            if random.random() < 0.5:
                print("You successfully escaped.")
                return GameState.TOWN
            else:
                print("Escape failed.")

        else:
            print("Invalid choice.")
            continue

        # ================= MONSTER DEAD ================= #

        if monster.health <= 0:
            print(f"{monster.name} has been defeated.")

            for item, qty in monster.drop.items():
                player.inventory.add_item(item, qty)

            player.exp += monster.exp_reward
            player.level_up()

            time.sleep(1)
            return GameState.TOWN

        # ================= MONSTER TURN ================= #

        if stun > 0:
            print(f"{monster.name} is stunned and cannot move.")
            stun -= 1
        else:
            damage = random.randint(monster.attack // 2, monster.attack)
            player.health -= damage
            jouer_bruit("Sound Effect/attack-sound.mp3")
            print(f"{monster.name} attacks {player.name} for {damage}")

        # ================= PLAYER DEAD ================= #

        if player.health <= 0:
            jouer_bruit("Sound Effect/death-sound.mp3")
            print(f"{player.name} has been defeated.")
            return GameState.EXIT

    return GameState.TOWN
