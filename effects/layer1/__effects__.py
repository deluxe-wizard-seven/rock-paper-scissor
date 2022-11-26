#!/usr/bin/python3

"""
This module contains the visual effects of the button lying in the first layer
of the game.
"""

from sys import stderr

try:
    from constants.colors_table import color
except ImportError as e:
    print(e, file=stderr)


def on_enter(instance_of_main_class, bg_color):
    """
    This method contains the visual effects which will take place
    when the mouse pointer is hovered over the component, who has called this
    method.
    """

    def actions():
        instance_of_main_class.button_submit["bg"] = color[bg_color]
        instance_of_main_class.button_submit["fg"] = color["white"]

    return actions


def on_leave(instance_of_main_class):
    """
    This method contains the visual effects which will take place
    when the mouse pointer is hovered out the component, who has called this
    method.
    """

    def actions():
        instance_of_main_class.button_submit["bg"] = color["dark_grey_1"]
        instance_of_main_class.button_submit["fg"] = color["white"]

    return actions
