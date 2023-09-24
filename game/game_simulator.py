from game.game_state import GameState
from game_simulator import GameSimulator
from pieces.bisp_piece import Bisp
from pieces.horse_piece import Horse
from pieces.king_piece import King
from pieces.pawn_piece import Pawn
from pieces.piece import Piece
from pieces.queen_piece import Queen
from pieces.tower_piece import Tower
from player import Player


class ChessGameSimulator(GameSimulator):

    POSSIBLE_PLAYER_PIECES = [
        Tower,
        Horse,
        Bisp,
        Queen,
        King,
        Bisp,
        Horse,
        Tower,
        Pawn,
        Pawn,
        Pawn,
        Pawn,
        Pawn,
        Pawn,
    ]
    
    BOARD_SIZE: int = 9

    def __init__(self, player1: Player, player2: Player) -> None:
        super().__init__(player1, player2)

    def init_game(self):
        
        state = GameState(0, self._player1, self._player2, ChessGameSimulator.BOARD_SIZE)
        
        self.__add_pieces(state.get_board())

        return state
    
    def __add_pieces(self, board: [[int]]):
        self.__set_up_pieces(self._player1, board)
        self.__set_up_pieces(self._player2, board)
    
    def __set_up_pieces(self, player: Player, board: [[int]]) -> [Piece]:
        # Current Piece Position
        position = 0

        # Offset y position
        offset = 0

        # Distribute pieces in the board
        shifter = 0

        # Array of each player pieces
        initial_pieces: [Piece] = []

        for piece in ChessGameSimulator.POSSIBLE_PLAYER_PIECES:
            
            piece = {
                    0: self.__add_player_piece(piece(offset, position - shifter), player),
                    1: self.__add_player_piece(piece(ChessGameSimulator.BOARD_SIZE - 2 - offset, position - shifter), player)
                }.get(player.get_class())

            if position >= ChessGameSimulator.BOARD_SIZE - 2:
                offset = 1
                shifter += 1
            else:
                position += 1

            initial_pieces.append(piece)
            board[piece.get_x()][piece.get_y()] = piece

        return initial_pieces
    
    def __add_player_piece(self, piece: Piece, player: Player):
        piece.set_color(player.get_color())
        player.add_piece(piece)
        return piece