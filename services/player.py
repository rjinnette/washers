from dataclasses import dataclass

@dataclass
class Player:
    name: str
    age: int | None = None