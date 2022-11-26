#!/usr/bin/python3

"""
This module contains the visual effects of the EXIT button.
"""

from sys import stderr

try:
    import effects.layer1.__effects__ as e
except ImportError as e:
    print(e, file=stderr)


def on_enter(instance_of_main_class):
    """
    This method contains the visual effects which will take place
    when the mouse pointer is hovered over the exit button.
    """

    def actions(*events):
        e.on_enter(instance_of_main_class, "crimson")

    return actions


def on_leave(instance_of_main_class):
    """
    This method contains the visual effects which will take place
    when the mouse pointer is hovered out of the exit button.
    """

    def actions(*events):
        e.on_leave(instance_of_main_class)

    return actions
