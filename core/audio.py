import pygame

def jouer_bruit(sound_path):
    pygame.mixer.init()
    sound = pygame.mixer.Sound(sound_path)
    sound.play()
