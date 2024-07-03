from dataclasses import dataclass

@dataclass
class Connection:
    state1: str
    state2: str
    weight: int
