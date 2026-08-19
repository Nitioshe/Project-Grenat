import time
from pypresence import Presence


CLIENT_ID = "1054459253617852436"

_rpc = None
_start_time = int(time.time())


def start_rpc():
    global _rpc

    try:
        _rpc = Presence(CLIENT_ID)
        _rpc.connect()

        _rpc.update(
            details="Dans le monde de Grenat",
            state="En train de jouer",
            large_image="game_logo",
            large_text="Project-Grenat",
            start=_start_time
        )

        print("Discord Rich Presence activée.")

    except Exception as error:
        print(f"Discord Rich Presence indisponible : {error}")
        _rpc = None


def update_rpc(details, state):
    if _rpc is None:
        return

    try:
        _rpc.update(
            details=details,
            state=state,
            large_image="game_logo",
            large_text="Mon jeu",
            start=_start_time
        )
    except Exception:
        pass


def stop_rpc():
    global _rpc

    if _rpc is not None:
        try:
            _rpc.close()
        except Exception:
            pass

        _rpc = None