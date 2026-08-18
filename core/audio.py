import os
import platform
import shutil
import subprocess
import threading

_audio_available = None


def _init_audio():
    global _audio_available

    if _audio_available is not None:
        return _audio_available

    system = platform.system()

    if system == "Windows":
        try:
            import winsound
            _audio_available = True
        except ImportError:
            _audio_available = False

    elif system == "Darwin":
        _audio_available = shutil.which("afplay") is not None

    elif system == "Linux":
        _audio_available = any(
            shutil.which(cmd) is not None
            for cmd in ("paplay", "aplay", "ffplay")
        )

    else:
        _audio_available = False

    return _audio_available


def jouer_bruit(sound_path):
    if not _init_audio():
        return

    if not os.path.isfile(sound_path):
        return

    system = platform.system()

    try:
        if system == "Windows":
            import winsound

            winsound.PlaySound(
                sound_path,
                winsound.SND_FILENAME | winsound.SND_ASYNC
            )

        elif system == "Darwin":
            subprocess.Popen(
                ["afplay", sound_path],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )

        elif system == "Linux":
            lecteur = None

            for cmd in ("paplay", "aplay", "ffplay"):
                chemin = shutil.which(cmd)
                if chemin:
                    lecteur = chemin
                    break

            if lecteur == shutil.which("paplay"):
                subprocess.Popen(
                    [lecteur, sound_path],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )

            elif lecteur == shutil.which("aplay"):
                subprocess.Popen(
                    [lecteur, sound_path],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )

            elif lecteur == shutil.which("ffplay"):
                subprocess.Popen(
                    [lecteur, "-nodisp", "-autoexit", "-loglevel", "quiet", sound_path],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )

    except (OSError, subprocess.SubprocessError):
        pass