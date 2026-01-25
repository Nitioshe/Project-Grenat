import json
import time

player_zone = ""

def load_zone(zone_path):
    global player_zone
    try:
        with open(zone_path, "r") as file:
            data = json.load(file)

        time.sleep(1)
        print("Zone loaded successfully.")
        player_zone = zone_path

        print("-")
        print("Zone Name:", data["name"])
        time.sleep(1)
        print("Description:", data["description"])
        print("-")

        return data
        

    except FileNotFoundError:
        print(f"Zone '{zone_path}' not found.")
    except json.JSONDecodeError:
        print(f"Invalid JSON in '{zone_path}'.")
