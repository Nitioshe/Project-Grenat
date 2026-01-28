def skills_menu(player):
    while True:
        print("\n=== Skills ===")
        for i, skill in enumerate(player.skills):
            cd = f" | Cooldown: {skill.cooldown}"
            cost = f" | Cost: {skill.cost}"
            print(f"{i+1}. {skill.name}{cost}{cd}")
        
        print("\nb. Back")
        choice = input("> ")

        if choice == "b":
            return