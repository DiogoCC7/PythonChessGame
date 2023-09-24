from action import Action
from pieces.piece import Piece


class ChessAction(Action):

    _selected_piece: Piece
    _move_to_x: int
    _move_to_y: int

    def __init__(self, piece: Piece, x: int, y: int) -> None:
        self._selected_piece = piece
        self._move_to_x = x
        self._move_to_y = y

    def get_selected_piece(self) -> Piece:
        return self._selected_piece
    
    def get_move_to_x(self) -> int:
        return self._move_to_x
    
    def get_move_to_y(self) -> int:
        return self._move_to_y