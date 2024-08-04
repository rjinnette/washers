from dataclasses import dataclass
from services.player import Player

@dataclass
class Team:
    team_number: int
    player1: Player
    player2: Player | None = None
    score: int  | None = 0

    def add_score(self, points_to_add:int):
        self.score += abs(points_to_add)

    def bust(self):
        self.score = 0

    
    


