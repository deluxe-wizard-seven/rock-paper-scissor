#!/usr/bin/python3

"""
This module contains the events to be carried out when the SUBMIT button is
being pressed.
"""

from tkinter import messagebox, StringVar
from sys import stderr

try:
    from events.layer1.__utils__ import remove_field
except ImportError as e:
    print(e, file=stderr)


def on_click(instance_of_main_class):
    """
    Actions which will take place when the user presses the SBUMIT button
    after entering the number of rounds they are willing to play.
    Essentially this function checks the validity of the number, if the
    number is invalid then an appropriate error message is displayed
    prompting the user about the error. If everything is alright then
    this function removes every components present in the screen and
    then executes the next layer of the game play setup.
    """

    def actions(*events):
        try:
            rounds = int(instance_of_main_class.text_box.get(1.0, "end"))
        except ValueError:
            messagebox.showerror(
                "Invalid Data", "Please enter a valid positive integer number."
            )
            instance_of_main_class.text_box.delete(1.0, "end")
        else:
            if rounds <= 0:
                messagebox.showerror(
                    "Invalid Data", "Please enter a positive integer number."
                )
                instance_of_main_class.text_box.delete(1.0, "end")
            else:
                instance_of_main_class.game_engine.number_of_rounds = rounds
                remove_field(
                    instance_of_main_class.number_of_rounds_label,
                    instance_of_main_class.text_box,
                    instance_of_main_class.button_next,
                    instance_of_main_class.button_back,
                    instance_of_main_class.canvas,
                )
                instance_of_main_class.load_playground_static_components()

    return actions
