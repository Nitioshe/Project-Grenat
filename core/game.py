from core.state import GameState
from zones import Tettno_main, Forest, AdventurersGuild
from combat import battle
from classes import inventory

def game_loop(player):
    state = GameState.TOWN
    running = True

    while running:
        if state == GameState.TOWN:
            state = Tettno_main(player, inventory)

        elif state == GameState.FOREST:
            state = Forest(player, inventory)

        elif state == GameState.COMBAT:
            state = battle(player, inventory)
        
        elif state == GameState.GUILD:
            state = AdventurersGuild(player, inventory)

        elif state == GameState.EXIT:
            running = False

    print("Game is over")
