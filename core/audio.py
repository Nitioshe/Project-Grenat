import pygame

_audio_available = None


def _init_audio():
    global _audio_available

    if _audio_available is not None:
        return _audio_available

    try:
        pygame.mixer.init()
        _audio_available = True
    except pygame.error:
        _audio_available = False

    return _audio_available


def jouer_bruit(sound_path):
    if not _init_audio():
        return

    try:
        sound = pygame.mixer.Sound(sound_path)
        sound.play()
    except pygame.error:
        pass