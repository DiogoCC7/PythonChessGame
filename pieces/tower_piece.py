
from pieces.piece import Piece


class Tower(Piece):

    TOWER_LABEL = 'T'

    def __init__(self, x = 0, y = 0) -> None:
        super().__init__(Tower.TOWER_LABEL, x, y)

    def can_move_to(self, x: int, y: int) -> bool:
        return self._x == x or self._y == y