
import os
from utils.color import Color


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def characterToInt(string: str):
    return ord(string.upper()) - ord('A')

def intToChar(number: int):
    return chr(number + ord('A') - 1)

def join(text: str, display_color: Color):
    return display_color + str(text) + '\033[0m'

def info_join(text: str):
    return join(text, Color.RED)

def danger_join(text: str):
    return join(text, Color.GREEN)

def action_join(text: str):
    return join(text, Color.PURPLE)

__all__ = [characterToInt, intToChar, join ,clear_screen]