from dataclasses import dataclass
from services.team import Team
from typing import Any


@dataclass
class Board:
    box: Team
    one: list[Team | Any]
    two: list[Team | Any]
    three: list[Team | Any]
    team1: Team
    team2: Team

    def check_bust(self):
        if self.box.score > 21:
            self.box.bust()

    def check_win(self):
        if self.box.score == 21:
            return True
        return False

    def calculate_net(self, hole: list[Team | Any]):
        team_1_score_count: int = 0
        team_2_score_count: int = 0
        for washer in hole:
            if washer is not None:
                if washer == 1:
                    team_1_score_count += 1
                elif washer == 2:
                    team_2_score_count += 1
        return team_1_score_count - team_2_score_count

    def compute_score(self):
        team_1_original = self.team1.score
        team_2_original = self.team2.score

        ones = self.calculate_net(self.one)
        twos = self.calculate_net(self.two)
        threes = self.calculate_net(self.three)

        if ones > 0:
            self.team1.add_score(ones)
            self.team2.add_score(0)
        elif ones < 0:
            ones = abs(ones)
            self.team1.add_score(0)
            self.team2.add_score(ones)

        if twos > 0:
            self.team1.add_score(twos * 2)
            self.team2.add_score(0)
        elif twos < 0:
            twos = abs(twos)
            self.team1.add_score(0)
            self.team2.add_score(twos * 2)

        if threes > 0:
            self.team1.add_score(threes * 3)
            self.team2.add_score(0)
        elif threes < 0:
            threes = abs(threes * 3)
            self.team1.add_score(0)
            self.team2.add_score(threes)

        team_1_final = self.team1.score
        team_2_final = self.team2.score

        team_1_diff = team_1_final - team_1_original
        team_2_diff = team_2_final - team_2_original

        return team_1_diff, team_2_diff

    # def calculate_box(self, team1_score: int, team2_score: int):
    #     if team1_score > team2_score:
    #         self.box = self.team1
    #     elif team1_score < team2_score:
    #         self.box = self.team2
    #     else:
    #         self.box = None
    #     return self.box
