from action import Action
from game.action import ChessAction
from game.game_state import GameState
from pieces.piece import Piece
from player import Player
from utils.color import Color

import utils.color_tools as color_tools 


class HumanPlayer(Player):

    DELIMITER = '|'
    GIVEUP_CODE  = -1

    def __init__(self, name, color, class_):
        super().__init__(name, color, class_)

    def get_action(self, state: GameState) -> Action:
        choosen_position: Piece
        acting_piece: Piece

        board = state.get_board()
        acting_player = state.get_acting_player()

        # Print Player's name
        print("Player: ", color_tools.join(acting_player.get_name(), acting_player.get_color()))

        # Choose Player's piece and select it
        acting_piece = self.choose_player_piece(acting_player, board)

        # Check Give up, there is no play
        if acting_piece == HumanPlayer.GIVEUP_CODE:
            return None

        # Re-render the board
        self.re_render(acting_piece, state)

        # Choose where to play piece
        choosen_position = self.choose_where_to_play_piece(acting_player, board)

        return ChessAction(acting_piece, choosen_position[0], choosen_position[1])
    
    def re_render(self, acting_piece: Piece, state: GameState):
        acting_piece.select_piece()
        self.show_possible_actions(state, acting_piece)
        state.display()
        
        self.unshow_possible_actions(state, acting_piece)
        acting_piece.unselect_piece()

    def show_possible_actions(self, state: GameState, acting_piece: Piece):
        possible_actions = state.get_possible_actions(acting_piece.get_x(), acting_piece.get_y())

        for action in possible_actions:
            
            cell: Piece|int = state.get_board()[action.get_move_to_x()][action.get_move_to_y()]

            if cell == GameState.EMPTY_CELL:
                state.get_board()[action.get_move_to_x()][action.get_move_to_y()] = GameState.POSSIBLE_CELL
            else:
                state.get_board()[action.get_move_to_x()][action.get_move_to_y()].mark()

    def unshow_possible_actions(self, state: GameState, acting_piece: Piece):
        possible_actions = state.get_possible_actions(acting_piece.get_x(), acting_piece.get_y())

        for action in possible_actions:
            
            cell: Piece|int = state.get_board()[action.get_move_to_x()][action.get_move_to_y()]

            if cell == GameState.POSSIBLE_CELL:
                state.get_board()[action.get_move_to_x()][action.get_move_to_y()] = GameState.EMPTY_CELL
            else:
                state.get_board()[action.get_move_to_x()][action.get_move_to_y()].unmark()
                 
    def extract_position(self, position: str) -> (int, int):
        
        if len(position) == 0:
            raise Exception("Please, provide a valid position to move")

        result = position.split(HumanPlayer.DELIMITER)

        if len(result) != 2:
            raise Exception(f"Please, provide the character {HumanPlayer.DELIMITER} between the position and the piece to move")

        if not result[0].isalpha():
            raise Exception(f"Please, provide a valid position to move")

        if not result[1].isnumeric():
            raise Exception(f"Please, provide a valid position to move")
        
        return (int(color_tools.characterToInt(result[0])), int(result[1]))
    
    def show_error(self, text):
        print(color_tools.danger_join(f"{text}\n"))

    def choose_player_piece(self, acting_player: Player, board: [[int]]) -> Piece:
        
        while True:

            try:

                message = input(color_tools.info_join("Please, Choose an valid piece to play (g: giveup): "))

                if message == 'g':
                    return -1

                choosen_piece: Piece|int = self.extract_position(message)

                # real piece position
                choosen_piece = board[choosen_piece[0]][choosen_piece[1]]

                if choosen_piece == GameState.EMPTY_CELL:
                    raise Exception(f"Please, provide an position where is a piece")
                
                if not acting_player.check_piece(choosen_piece):
                    raise Exception(f"Please, only select your pieces")
                
                return choosen_piece
            
            except Exception as e:
                self.show_error(e)
    
    def choose_where_to_play_piece(self, acting_player: Player, board: [[int]]):
        choosen_piece: Piece|int
        
        while True:

            try:
                
                message = input(color_tools.info_join("Please, Choose an valid position to move it (d: discard): "))
                
                if message == 'd':
                    return (-1, -1)
                
                choosen_position: Piece|int = self.extract_position(message)

                # real piece position
                choosen_piece = board[choosen_position[0]][choosen_position[1]]

                # Can be either an piece or an empty cell, cannot be player's piece
                if isinstance(choosen_piece, Piece) and choosen_piece.get_color() == acting_player.get_color():
                    raise Exception(f"Please, provide an position or piece where isn't a piece of yours")
                
                return choosen_position

            except Exception as e:
                self.show_error(e)
