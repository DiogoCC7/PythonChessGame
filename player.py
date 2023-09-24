from abc import ABC, abstractmethod
from action import Action
from game.action import ChessAction
from pieces.piece import Piece
from state import State


class Player():

    _name: str

    _class: int
    _color: str
    _pieces: [Piece]

    def __init__(self, name, color, class_):
        self._class = class_
        self._name = name
        self._color = color

        self._pieces = []

    def add_piece(self, piece: Piece):
        self._pieces.append(piece)

    def check_piece(self, piece: Piece) -> bool:
        
        # TODO: Fix the 32 pieces added problem
        if piece.get_color() == self._color:
            return True
            
        return False

    def has_pieces(self) -> bool:
        return len(self._pieces) > 0

    def get_pieces(self):
        return self._pieces
    
    def get_color(self):
        return self._color
    
    def get_name(self):
        return self._name
    
    def get_class(self):
        return self._class
    
    @abstractmethod
    def get_action(self, state: State) -> Action:
        pass