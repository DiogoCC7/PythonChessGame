from pieces.piece import Piece


class Horse(Piece):

    HORSE_LABEL = 'H'

    def __init__(self, x = 0, y = 0) -> None:
        super().__init__(Horse.HORSE_LABEL, x, y)

    def can_move_to(self, x: int, y: int) -> bool:
        return True
