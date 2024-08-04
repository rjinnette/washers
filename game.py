from services.team import Team
from services.player import Player
from services.board import Board

def main():
    ryan = Player("Ryan", 21)
    reed = Player("Reed", 53)

    team_1 = Team(team_number=1, player1=ryan, player2=None, score=0)
    team_2 = Team(team_number=2, player1=reed, player2=None, score=0)

    ones = [team_2, team_2, team_2] # 3
    twos = [team_1, team_1, team_2] # 2
    threes = [team_1, team_2, team_2] # 3
    # 6 to 2

    board = Board(box=team_1, one=ones, two=twos, three=threes, team1=team_1, team2=team_2)

    board.compute_score()

    print(f"{team_1.player1.name}: {team_1.score}\n{team_2.player1.name}: {team_2.score}")

main()