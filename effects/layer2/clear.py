#!/usr/bin/python3

"""
This module contains the visual effects of the CLEAR SELECTION button.
"""

from sys import stderr

try:
    from constants.colors_table import color
except ImportError as e:
    print(e, file=stderr)


def on_enter(instance_of_main_class):
    """
    The visual effects that will take place when the mouse is
    hovered over the CLEAR button.
    """

    def actions(*events):
        instance_of_main_class.left_button_clear_choice["bg"] = color["red_orange"]
        instance_of_main_class.left_button_clear_choice["fg"] = color["white"]

    return actions


def on_leave(instance_of_main_class):
    """
    The visual effects that will take place when the mouse is
    hovered outside the CLEAR button.
    """

    def actions(*events):
        instance_of_main_class.left_button_clear_choice["bg"] = color["dark_grey_3"]
        instance_of_main_class.left_button_clear_choice["fg"] = color["red_orange"]

    return actions
