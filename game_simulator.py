from abc import ABC, abstractmethod
from game.result import ChessResult
from player import Player

from state import State

class GameSimulator:

    _player1: Player
    _player2: Player

    def __init__(self, player1: Player, player2: Player) -> None:
        self._player1 = player1
        self._player2 = player2
    
    @abstractmethod
    def init_game(self) -> State:
        pass

    def start_game(self) -> ChessResult:

        state = self.init_game()
        selected_player: Player = state.get_acting_player()
        
        while not state.is_finish():
            state.display()
            
            while True:
                selected_action = selected_player.get_action(state.clone())

                if selected_action is None:
                    return state.get_result(selected_player)

                if state.validate_action(selected_action):
                    break

                state.display()

            state.play(selected_action)

        self.win_game_scene(state, selected_player)

    def win_game_scene(self, state, selected_player):
        if state.check_win():
            print("Player: ", selected_player.get_name(), " won!")