from pieces.piece import Piece


class Pawn(Piece):

    PEAN_LABEL = 'P'

    def __init__(self, x, y) -> None:
        super().__init__(Pawn.PEAN_LABEL, x, y)

    def can_move_to(self, x: int, y: int) -> bool:
        # only can move one square to the front
        diff_x = abs(x - self._x)
        diff_y = abs(y - self._y)

        return (diff_x == 0 and diff_y == 1)