from abc import ABC, abstractmethod

from action import Action

class State:

    __state: bool = True

    def __init__(self, state) -> None:
        self.__state = state

    @abstractmethod
    def update(self, action: Action) -> None:
        pass

    @abstractmethod
    def get_acting_player(self):
        pass

    @abstractmethod
    def validate_action(self, action: Action) -> bool:
        pass

    @abstractmethod
    def is_finish(self) -> bool:
        pass

    @abstractmethod
    def check_win(self) -> bool:
        pass

    # action
    def play(self, action: Action) -> bool:
        
        if not self.validate_action(action):
            return False
        
        self.update(action)
        return True
    
    def get_state(self):
        return self.__state