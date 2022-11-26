#!/usr/bin/python3

"""
Rock, Paper and Scissors Game implementation.
"""

from time import sleep
from gui import GUI
from random import randint
from constants.moves import Moves
from constants.colors_table import color


class RockPaperScissorsGame:
    """
    Game Engine of Rock, Paper and Scissors game.
    """

    def __init__(self):
        self.player = {1: dict(), 2: dict()}
        self.player[1]["score"] = 0
        self.player[2]["score"] = 0
        self.player[1]["choice"] = None
        self.player[2]["choice"] = None
        self.player[1]["move"] = None
        self.player[2]["move"] = None
        self.number_of_rounds = None
        self.winner = None
        self.computer_side = "right" if randint(0, 1) else "left"

    def __check__(self, action: dict) -> int:
        """
        This method is used to obtain the result of a single round by
        comparing the moves from both the parties.

        The odering are as follows, Rock beats Scissor, Scissor beats
        Paper and finally Paper beats Rock.

        This method returns either 0, 1 or 2 where 0 represents a tie,
        1 represents that the first player is the winner of the current
        round and 2 represents that the second player is the winner of
        the current round.

        This method also returns -1 when the action of the first player
        is missing (i.e. the value of 'first_player' is missing from the
        dictonary action) and if this function returns -2 then the action
        of the second player is missing(i.e. the value of 'second_player'
        is missing from the dictonary action)
        """

        if "first_player" not in action:
            return -1

        if "second_player" not in action:
            return -2

        result = action["second_player"] - action["first_player"]

        return 0 if not result else 1 if result in {3, -1, -2} else 2

    def evaluate(self):
        """
        This method evaluates the moves from both players and decides the
        winner.
        """

        self.gui.update_root()

        sleep(1.5)

        winner = self.__check__(
            {
                "first_player": self.player[1]["move"],
                "second_player": self.player[2]["move"],
            }
        )

        assert winner in (0, 1, 2), f"Invalid Move [{winner=}]"
        assert self.computer_side in (
            "left",
            "right",
        ), f"Invalid Side [{self.computer_side=}]"

        it_is_a_tie = winner == 0

        if it_is_a_tie:
            text = "It's a tie"
            fg = color["lemon_yellow"]
        elif winner == 1:
            self.player[1]["score"] += 1
            fg = (
                color["sky_blue"]
                if self.computer_side == "right"
                else color["lime_green"]
            )
        else:
            self.player[2]["score"] += 1
            fg = (
                color["lime_green"]
                if self.computer_side == "right"
                else color["sky_blue"]
            )

        sum_of_moves = self.player[1]["move"] + self.player[2]["move"]

        assert it_is_a_tie or sum_of_moves in (
            3,
            5,
            6,
        ), f"Invalid Move [{it_is_a_tie=}, {result=}]"

        if sum_of_moves == 3:
            text = "Paper covers Rock"
        elif sum_of_moves == 5:
            text = "Rock crushes Scissor"
        elif sum_of_moves == 6:
            text = "Scissor cuts Paper"

        self.gui.config_status_label(fg=fg)
        self.gui.set_status(status=text)
        self.gui.set_player_score(player=1, score=self.player[1]["score"])
        self.gui.set_player_score(player=2, score=self.player[2]["score"])
        self.gui.destroy_move(player=1)
        self.gui.destroy_move(player=2)

        self.player[1]["choice"].set(0)
        self.player[2]["choice"].set(0)

        if self.player[1]["score"] == self.number_of_rounds:
            self.winner = 1
            self.gui.ending_screen()
        elif self.player[2]["score"] == self.number_of_rounds:
            self.winner = 2
            self.gui.ending_screen()
        else:
            self.gui.load_playground_dynamic_components()

    def generate_next_move(self) -> Moves:
        """
        This method is used to generate random moves.
        """

        result = 2 ** randint(0, 2)

        if result == 1:
            self.player[2]["move"] = Moves.ROCK
        elif result == 2:
            self.player[2]["move"] = Moves.PAPER
        elif result == 4:
            self.player[2]["move"] = Moves.SCISSOR
        else:
            self.player[2]["move"] = None

        return self.player[2]["move"]

    def play(self, replay: bool = False):
        """
        This function is used by the user in order to play the game.
        Calling this function will start and end the game securely
        in an ordered way.
        """

        if replay:
            self.__init__()
        self.gui = GUI(self)
        self.gui.start()


if __name__ == "__main__":
    RockPaperScissorsGame().play()
