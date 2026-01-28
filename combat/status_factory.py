from combat.status import Poison, Stun

STATUS_REGI = {
    "Poison": Poison,
    "Stun": Stun
}

def create_status(name, duration):
    if name not in STATUS_REGI:
        raise ValueError(f"Unknown status: {name}")
    return STATUS_REGI[name](duration=duration)
