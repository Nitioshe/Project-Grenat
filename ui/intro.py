import time
from core.audio import jouer_bruit
from data.ascii_art import ASCII_ART_1, ASCII_ART_2

def start_animation():
    jouer_bruit("Sound Effect/logo-sound.wav")
    print(ASCII_ART_1)
    time.sleep(1)
    print(ASCII_ART_2)
    print("Starting game", end="", flush=True)
    for _ in range(5):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print("\n")
