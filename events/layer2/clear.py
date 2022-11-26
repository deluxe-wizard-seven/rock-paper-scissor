#!/usr/bin/python3

"""
This module contains the events to be carried out when the CLEAR SELECTION
button is being pressed.
"""


def on_click_left_button(instance_of_main_class):
    """
    Actions which will take place when the CLEAR SELECTION button on the
    left side of the window is clicked.
    """

    def actions(*events):
        instance_of_main_class.left_radio_button_rock.deselect()
        instance_of_main_class.left_radio_button_paper.deselect()
        instance_of_main_class.left_radio_button_scissor.deselect()

        instance_of_main_class.game_engine.player[1]["choice"].set(0)

    return actions


def on_click_right_button(instance_of_main_class):
    """
    Actions which will take place when the CLEAR SELECTION button on the
    right side of the window is clicked.
    """

    def actions(*events):
        instance_of_main_class.right_radio_button_rock.deselect()
        instance_of_main_class.right_radio_button_paper.deselect()
        instance_of_main_class.right_radio_button_scissor.deselect()

        instance_of_main_class.game_engine.player[1]["choice"].set(0)

    return actions
