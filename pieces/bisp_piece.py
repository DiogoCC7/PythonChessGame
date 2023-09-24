from pieces.piece import Piece


class Bisp(Piece):

    BISP_LABEL = 'B'

    def __init__(self, x = 0, y = 0) -> None:
        super().__init__(Bisp.BISP_LABEL, x, y)

    def can_move_to(self, x: int, y: int) -> bool:
        diff_x = abs(x - self._x)
        diff_y = abs(y - self._y)

        return (diff_x == diff_y)