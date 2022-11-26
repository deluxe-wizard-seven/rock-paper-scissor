#!/usr/bin/python3

"""
This class contains the constants representing the moves played by
the user in the Rock, Paper and Scissor game.
"""

from enum import IntEnum


class Moves(IntEnum):
    """
    This class contains constants representing the move played in
    Rock, Paper and Scissor game, with each having a distinct integer id.
    """

    ROCK = 1
    PAPER = 2
    SCISSOR = 4
