import random
import time
from core.audio import jouer_bruit

def battle(player, monster):
    poison = 1
    PoisonAtk = False
    stun = 1

    print("Battle Start!")
    while player.health > 0 and monster.health > 0:

        print("\n1. Attack")
        choice = input("> ")

        if choice == "1":
            damage = random.randint(player.attack // 2, player.attack)
            
            if PoisonAtk == True :
                poison_damage = random.randint(1, poison * 2)
                monster.health -= poison_damage

            monster.health -= damage
            jouer_bruit("Sound Effect/attack-sound.mp3")
            print(f"{player.name} deals {damage} damage")

        if monster.health <= 0:
            print(f"{monster.name} defeated!")
            for item, qty in monster.drop.items():
                player.inventory.add_item(item, qty)
            player.exp += monster.exp_reward
            player.level_up()
            return True

        damage = random.randint(monster.attack // 2, monster.attack)
        player.health -= damage
        jouer_bruit("Sound Effect/attack-sound.mp3")
        print(f"{monster.name} hits {player.name} for {damage}")

        if player.health <= 0:
            jouer_bruit("Sound Effect/death-sound.mp3")
            print("You died.")
            return False
