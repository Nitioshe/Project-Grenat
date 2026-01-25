import json

def save_game(player):
    with open("Saves/save.json", "w") as file:
        json.dump(player.to_dict(), file)
    print("Game saved successfully.")

def load_game(player):
    try:
        with open("Saves/save.json", "r") as file:
            data = json.load(file)
        for key, value in data.items():
            setattr(player, key, value)
        print("Game loaded successfully.")
        return player
    except FileNotFoundError:
        print("No saved game found.")
        return None
