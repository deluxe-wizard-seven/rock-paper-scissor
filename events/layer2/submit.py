#!/usr/bin/python3

"""
This module contains the events to be carried out when the SUBMIT button is
being pressed.
"""

from tkinter import messagebox, Label
from sys import stderr

try:
    from events.layer2.__utils__ import resize_image
    from events.layer1.__utils__ import remove_field
    from constants.moves import Moves
except ImportError as e:
    print(e, file=stderr)


def on_click_left_button(instance_of_main_class):
    """
    Actions which will take place when the SUBMIT button of the left
    window will be clicked.
    """

    def actions(*events):
        result = instance_of_main_class.game_engine.player[1]["choice"].get()

        assert result in (0, 1, 2, 4), "Invalid Move"

        if result == 1:
            choice = resize_image(
                instance_of_main_class.image_url[Moves.ROCK],
                instance_of_main_class.scaling_factor * 2,
            )
            instance_of_main_class.game_engine.player[1]["move"] = Moves.ROCK
        elif result == 2:
            choice = resize_image(
                instance_of_main_class.image_url[Moves.PAPER],
                instance_of_main_class.scaling_factor * 2,
            )
            instance_of_main_class.game_engine.player[1]["move"] = Moves.PAPER
        elif result == 4:
            choice = resize_image(
                instance_of_main_class.image_url[Moves.SCISSOR],
                instance_of_main_class.scaling_factor * 2,
            )
            instance_of_main_class.game_engine.player[1]["move"] = Moves.SCISSOR
        else:
            messagebox.showerror("Invalid move", "Please choose a valid move")
            instance_of_main_class.game_engine.player[1]["choice"].set(0)
            return

        remove_field(
            instance_of_main_class.left_choice_rock,
            instance_of_main_class.left_choice_paper,
            instance_of_main_class.left_choice_scissor,
            instance_of_main_class.left_radio_button_rock,
            instance_of_main_class.left_radio_button_paper,
            instance_of_main_class.left_radio_button_scissor,
            instance_of_main_class.left_button_submit_choice,
            instance_of_main_class.left_button_clear_choice,
        )

        instance_of_main_class.player_1_move = Label(
            instance_of_main_class.root, image=choice, borderwidth=0
        )
        instance_of_main_class.player_1_move.image = choice
        instance_of_main_class.player_1_move.place(x=120, y=100)

        instance_of_main_class.place_next_move()
        instance_of_main_class.game_engine.evaluate()

    return actions


def on_click_right_button(instance_of_main_class):
    """
    Actions which will take place when the SUBMIT button of the right
    window will be clicked.
    """

    def actions(*events):
        result = instance_of_main_class.game_engine.player[1]["choice"].get()

        assert result in (0, 1, 2, 4), "Invalid Move"

        if result == 1:
            choice = resize_image(
                instance_of_main_class.image_url[Moves.ROCK],
                instance_of_main_class.scaling_factor * 2,
            )
            instance_of_main_class.game_engine.player[1]["move"] = Moves.ROCK
        elif result == 2:
            choice = resize_image(
                instance_of_main_class.image_url[Moves.PAPER],
                instance_of_main_class.scaling_factor * 2,
            )
            instance_of_main_class.game_engine.player[1]["move"] = Moves.PAPER
        elif result == 4:
            choice = resize_image(
                instance_of_main_class.image_url[Moves.SCISSOR],
                instance_of_main_class.scaling_factor * 2,
            )
            instance_of_main_class.game_engine.player[1]["move"] = Moves.SCISSOR
        else:
            messagebox.showerror("Invalid move", "Please choose a valid move")
            instance_of_main_class.game_engine.player[1]["choice"].set(0)
            return

        remove_field(
            instance_of_main_class.right_choice_rock,
            instance_of_main_class.right_choice_paper,
            instance_of_main_class.right_choice_scissor,
            instance_of_main_class.right_radio_button_rock,
            instance_of_main_class.right_radio_button_paper,
            instance_of_main_class.right_radio_button_scissor,
            instance_of_main_class.right_button_submit_choice,
            instance_of_main_class.right_button_clear_choice,
        )

        instance_of_main_class.player_1_move = Label(
            instance_of_main_class.root, image=choice, borderwidth=0
        )
        instance_of_main_class.player_1_move.image = choice
        coordinates = {"x": instance_of_main_class.width // 2 + 120, "y": 100}
        instance_of_main_class.player_1_move.place(**coordinates)

        instance_of_main_class.place_next_move()
        instance_of_main_class.game_engine.evaluate()

    return actions
