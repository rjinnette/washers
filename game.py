from services.team import Team
from services.player import Player
from services.board import Board
from services.throw import Throw


def main():
    ryan = Player("Ryan", 21)
    reed = Player("Reed", 53)

    team_1 = Team(team_number=1, player1=ryan, player2=None, score=0)
    team_2 = Team(team_number=2, player1=reed, player2=None, score=0)

    ones = []
    twos = []
    threes = []

    board = Board(
        box=team_1, one=ones, two=twos, three=threes, team1=team_1, team2=team_2
    )
    throw = Throw(existing_box=team_1, board=board, team_1=team_1, team_2=team_2)

    throw.washer(throw.board.one, team_1)
    throw.washer(throw.board.one, team_1)
    throw.washer(throw.board.one, team_1)

    throw.washer(throw.board.two, team_1)
    throw.washer(throw.board.two, team_1)
    throw.washer(throw.board.two, team_1)

    throw.washer(throw.board.three, team_2)
    throw.washer(throw.board.three, team_2)
    throw.washer(throw.board.three, team_2)

    throw.end_of_throw()
    # 6 to 2

    print(
        f"{team_1.player1.name}: {team_1.score}\n{team_2.player1.name}: {team_2.score}"
    )


main()
