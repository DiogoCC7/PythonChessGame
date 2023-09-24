import itertools
from typing import Optional
from action import Action
from game.action import ChessAction
from game.result import ChessResult
from pieces.piece import Piece
from state import State

from player import Player
from utils.color import Color
import utils.color_tools as color_tools

class GameState(State):

    EMPTY_CELL = -1
    POSSIBLE_CELL = -2
    POSSIBLE_CELL_SYMBOL = 'x'

    __size: int
    _board: [[int]]

    _player1: Player
    _player2: Player

    __acting_player_class: int

    def __init__(self, class_ : int, player1: Player, player2: Player, size = 9) -> None:
        self.__size = size
        self._player1 = player1
        self._player2 = player2

        self.__acting_player_class = class_

        self._board = [[GameState.EMPTY_CELL for _ in range(8)] for _ in range(8)]

    def display(self):
        color_tools.clear_screen()

        self.__display_numbers()

        for row in range(0, self.__size - 1):
            print(f"{color_tools.action_join(chr((row + 1) - 1 + ord('A')))} ", end="")
            for col in range(0, self.__size - 1):
                print(color_tools.join('|', Color.YELLOW), end="")
                self.__display_cell(row, col)

            print(color_tools.join('|', Color.YELLOW), end="")
            print('')
        
        self.__print_game_status()

    def __display_numbers(self):
        print('  ', end="")
        for col in range(0, self.__size - 1):
            if col < 10:
                print(' ', end="")
            print(f'{color_tools.action_join(col + 1)}', end="")
        print("")

    def __display_cell(self, row, col):
        cell = self._board[row][col]

        display_elem =  {
            GameState.EMPTY_CELL: ' ',
            GameState.POSSIBLE_CELL: color_tools.join(GameState.POSSIBLE_CELL_SYMBOL, Color.YELLOW),
        }

        print(display_elem.get(cell, cell), end="")

    def __print_game_status(self):
        print('\nGaming State: ',
               {
                   True: color_tools.join('Playing', Color.YELLOW),
                    False: color_tools.join('Finished', Color.GREEN)
               }.get(self.get_state())
            , "\n")

    # TODO: Implement this method
    def check_win(self, value = False) -> bool:
        return value

    # TODO: Implement condition to check if the action is valid
    # TODO: Validate jumping over pieces
    def validate_action(self, action: ChessAction) -> bool:
        selected_piece: Piece|int = action.get_selected_piece()
        selected_x = action.get_move_to_x()
        selected_y = action.get_move_to_y()

        # Make sure that the selected piece is not empty and it's inside of the board
        if selected_x < 0 or selected_x > self.__size - 1:
            return False
        
        if selected_y < 0 or selected_y > self.__size - 1:
            return False

        # Selected choosen piece
        choosen_position: Piece|int = self._board[selected_x][selected_y]

        # Check if the piece is from the acting player
        if isinstance(choosen_position, Piece) and selected_piece.get_color() != self.get_acting_player().get_color():
            return False
        
        if isinstance(choosen_position, Piece) and choosen_position.get_color() == self.get_acting_player().get_color():
            return False
        
        # Check jumping over pieces
        if self.dont_jump_piece(selected_piece.get_x(), selected_piece.get_y(), selected_x, selected_y):
            return False
        
        # Validate's the piece's movement
        return selected_piece.can_move_to(selected_x, selected_y)
    
    def dont_jump_piece(self, x_start, y_start, x_end, y_end):

        # combinations
        diff_row = 1 if x_end > x_start else -1 if x_end < x_start else 0
        diff_col = 1 if y_end > y_start else -1 if y_end < y_start else 0

        for i in range(1, max(abs(x_end - x_start), abs(y_end - y_start))):
            row = x_start + i * diff_row
            col = y_start + i * diff_col
            if row < 0 or row >= len(self._board) or col < 0 or col >= len(self._board[0]):
                return False

            check_piece = self._board[row][col]

            if isinstance(check_piece, Piece):
                return False

        return True

    def get_acting_player(self) -> Player:
        return {
            0: self._player1,
            1: self._player2
        }.get(self.__acting_player_class)
    
    def update(self, action: ChessAction) -> None:
        # Move Piece
        self.__move_piece(action)

        # Change Player
        self.__acting_player_class = self.__change_player_turn()

    def __move_piece(self, action: ChessAction):
        piece = action.get_selected_piece()

        x = piece.get_x()
        y = piece.get_y()

        move_to_x = action.get_move_to_x()
        move_to_y = action.get_move_to_y()

        self._board[x][y] = GameState.EMPTY_CELL
        piece.set_x(move_to_x)
        piece.set_y(move_to_y)
        self._board[move_to_x][move_to_y] = piece

    def __change_player_turn(self):
        return {
            0: 1,
            1: 0
        }.get(self.__acting_player_class)

    def get_board(self) -> [[int]]:
        return self._board
    
    def get_result(self, player: Player) -> Optional[ChessResult]:
        
        if self.check_win(True):
            return ChessResult.WIN if player.get_class() == self.__acting_player_class else ChessResult.LOSE
        
        return None

    def is_finish(self) -> bool:
        return self.check_win()
    
    def clone(self):
        clone_state = GameState(self.__acting_player_class, self._player1, self._player2, self.__size)
        clone_state._board = self.get_board()
        clone_state.__acting_player_class = self.__acting_player_class

        return clone_state
    
    def get_possible_actions(self, init_x: int, init_y: int) -> [Action]:
        possibles = list(
            filter(
                lambda action: self.validate_action(action),
                map(
                    lambda position: ChessAction(self._board[init_x][init_y], position[0], position[1]),
                    itertools.product(range(0, self.__size - 1),
                                  range(0, self.__size - 1))
                )
            )
        )

        return possibles

        