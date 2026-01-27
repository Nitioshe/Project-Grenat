"""
Docstring for core.game
"""
from core.state import GameState
from zones import Tettno_main, Forest, AdventurersGuild, Bank
from combat.battle import battle


def game_loop(player):
    """
    Docstring for game_loop
    
    :param player: using player data
    """
    state = GameState.TOWN
    running = True
    current_monster = None

    while running:
        if state == GameState.TOWN:
            state = Tettno_main(player)

        elif state == GameState.FOREST:
            state, current_monster = Forest(player)

        elif state == GameState.COMBAT:
            state = battle(player, current_monster)
            current_monster = None

        elif state == GameState.GUILD:
            state = AdventurersGuild(player)

        elif state == GameState.BANK:
            state = Bank(player)

        elif state == GameState.EXIT:
            running = False

    print("Game is over")
