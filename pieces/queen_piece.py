from pieces.piece import Piece


class Queen(Piece):

    QUEEN_LABEL = 'Q'

    def __init__(self, x = 0, y = 0) -> None:
        super().__init__(Queen.QUEEN_LABEL, x, y)

    def can_move_to(self, x: int, y: int) -> bool:
        diff_x = abs(x - self._x)
        diff_y = abs(y - self._y)

        return (
            (diff_x > 0 and diff_y == 0) or (diff_x == 0 and diff_y > 0) or (diff_x == diff_y) or
            diff_x > 0 and diff_y == 0 or
            diff_x == 0 and diff_y > 0
        )