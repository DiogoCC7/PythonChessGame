from game.game_simulator import ChessGameSimulator
from game.result import ChessResult
from players.human_player import HumanPlayer
from utils.color import Color

PLAYER1_NAME = "Cavas Callahan"
PLAYER2_NAME = "Robert Shot"

game_simulator = ChessGameSimulator(
    HumanPlayer(PLAYER1_NAME, Color.BLUE, 0),
    HumanPlayer(PLAYER2_NAME, Color.LIGHT_GRAY, 1)
)

result: ChessResult = game_simulator.start_game()
print(f"Game Finished!, {result}")