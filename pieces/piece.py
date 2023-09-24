from abc import ABC, abstractmethod
import utils.color_tools as color_tools

from utils.color import Color

class Piece(ABC):

    SELECTION_COLOR = Color.GREEN
    POSSIBLE_COLOR = Color.YELLOW

    _color: str
    _label: str

    _x: int
    _y: int

    _is_possible: bool = False
    _is_selected: bool = False

    def __init__(self, label, x = 0, y = 0) -> None:
        self._label = label
        self._x = x
        self._y = y

    def set_color(self, color):
        self._color = color

    def get_color(self):
        return self._color
    
    def get_label(self):
        return self._label
    
    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
    
    def set_x(self, value: int):
        return value
    
    def set_y(self, value: int):
        return value
    
    def can_move_to(self, x: int, y: int) -> bool:
        pass

    def select_piece(self):
        self._is_selected = True

    def unselect_piece(self):
        self._is_selected = False

    def is_selected(self) -> bool:
        return self._is_selected
    
    def mark(self):
        self._is_possible = True

    def unmark(self):
        self._is_possible = False

    def is_possible(self) -> bool:
        return self._is_possible

    def __str__(self) -> str:
        
        if self._is_possible:
            return color_tools.join(self._label, Piece.POSSIBLE_COLOR)

        if self._is_selected:
            return color_tools.join(self._label, Piece.SELECTION_COLOR)

        return color_tools.join(self._label, self._color)