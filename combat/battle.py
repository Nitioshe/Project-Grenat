"""
Docstring for combat.battle
    Module generating battle logic
"""
import random
import time
from core.audio import jouer_bruit
from core.state import GameState


def battle(player, monster):
    """
    Docstring for battle
    
        Game battle logic
    :param player: using player data
    :param monster: using monster data loaded from zones
    """
    poison = 0
    poison_active = False
    stun = 0

    print("\nBattle Start!")
    print(f"{monster.name} appears.")

    while player.health > 0 and monster.health > 0:

        print("\n╔----------------------╗")
        print(f"  {player.name} HP: {player.health}/{player.max_health}")
        print(f"    {monster.name} HP: {monster.health}")
        print("╚----------------------╝")

        print("1. Attack\n2. Skills\n3. Inventory\n4. Flee")

        choice = input("> ")

        # ================= PLAYER TURN ================= #

        for status in player.status_effect[:]:
            status.on_turn_start(player)
            if status.tick():
                player.status_effect.remove(status)
        
        if player.stunned:
            print(f"{player.name} is stunned !")
            player.stunned = False
            
        # A ident pour stun bloquant atk
        
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
            for i, skill in enumerate(player.skills):
                cd = f"(CD: {skill.current_cd})" if skill.current_cd > 0 else ""
                print(f"{i+1}. {skill.name} {cd}")

            s = int(input("> ")) - 1
            skill = player.skills[s]

            if skill.can_use(player):
                skill.use(player, monster)
            else:
                print("Skill indisponible")

        elif choice == "3":
            player.inventory.display_inventory()
            input("Press Enter to continue...")

        elif choice == "4":
            if random.random() < 0.5:
                print("You successfully escaped.")
                return GameState.TOWN
            else:
                print("Escape failed.")

        else:
            print("Invalid choice.")
            continue
        
        for skill in player.skills:
            skill.reduce_cooldown()

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

        usable_skills = [s for s in monster.skills if s.can_use(monster)]

        if usable_skills and random.randint(1, 2) < 0.4:
            skill = random.choice(usable_skills)
            skill.use(monster, player)
            jouer_bruit("Sound Effect/attack-sound.mp3")    #must be fixed

        elif stun > 0:
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
