from services.board import Board
from services.player import Player
from services.team import Team
from dataclasses import dataclass
from typing import Any


@dataclass
class Throw:
    team_1: Team
    team_2: Team

    # at the start of the game, the existing box is team_1's
    existing_box: Team  # noqa: F821
    board: Board

    def washer(self, hole: list[Team | Any], team: Team):
        hole.append(team.team_number)

    def box(self, team_1_net: int, team_2_net: int):
        if team_1_net > team_2_net:
            self.board.box = self.team_1
        elif team_2_net > team_1_net:
            self.board.box = self.team_2
        elif team_1_net == team_2_net:
            self.board.box = self.existing_box

    def end_of_throw(self):
        team_1_net, team_2_net = self.board.compute_score()
        self.box(team_1_net, team_2_net)
