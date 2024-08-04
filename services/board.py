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

    def calculate_net_one(self):
        team_1_score_count: int = 0
        team_2_score_count: int = 0
        if self.one is not None:
            for washer in self.one:
                if washer.team_number == 1:
                    team_1_score_count += 1
                elif washer.team_number == 2:
                    team_2_score_count += 1
            return team_1_score_count - team_2_score_count
        return
    
    def calculate_net_two(self):
        team_1_score_count: int = 0
        team_2_score_count: int = 0
        if self.two is not None:
            for washer in self.two:
                if washer.team_number == 1:
                    team_1_score_count += 1
                elif washer.team_number == 2:
                    team_2_score_count += 1
            return team_1_score_count - team_2_score_count
        return
    
    def calculate_net_three(self):
        team_1_score_count: int = 0
        team_2_score_count: int = 0
        if self.three is not None:
            for washer in self.three:
                if washer.team_number == 1:
                    team_1_score_count += 1
                elif washer.team_number == 2:
                    team_2_score_count += 1
            return team_1_score_count - team_2_score_count
        return
    
    def compute_score(self):
        ones = self.calculate_net_one()
        twos = self.calculate_net_two()
        threes = self.calculate_net_three()

        if ones > 0:
            self.team1.add_score(ones)
            self.team2.add_score(0)
        elif ones < 0:
            ones = abs(ones)
            self.team1.add_score(0)
            self.team2.add_score(ones)

        if twos > 0:
            self.team1.add_score(twos*2)
            self.team2.add_score(0)
        elif twos < 0:
            twos = abs(twos)
            self.team1.add_score(0)
            self.team2.add_score(twos*2)

        if threes > 0:
            self.team1.add_score(threes*3)
            self.team2.add_score(0)
        elif threes < 0:
            threes = abs(threes*3)
            self.team1.add_score(0)
            self.team2.add_score(threes)
            
            
            
            

