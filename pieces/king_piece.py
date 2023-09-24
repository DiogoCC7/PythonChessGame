from pieces.piece import Piece


class King(Piece):

    KING_LABEL = 'K'

    def __init__(self, x = 0, y = 0) -> None:
        super().__init__(King.KING_LABEL, x, y)

    def can_move_to(self, x: int, y: int) -> bool:
        # only can move one square
        diff_x = abs(x - self._x)
        diff_y = abs(y - self._y)

        return (diff_x <= 1 and diff_y <= 1)