#!/usr/bin/python3

"""
This module contains the events to be carried out when the PLAY button is
being pressed.
"""

from sys import stderr

try:
    from events.layer1.__utils__ import remove_field
except ImportError as e:
    print(e, file=stderr)


def on_click(instance_of_main_class):
    """
    Actions which will take place when the PLAY button is clicked
    by the user.
    """

    def actions(*events):

        remove_field(
            instance_of_main_class.button_about,
            instance_of_main_class.button_play,
            instance_of_main_class.button_exit,
        )

        instance_of_main_class.load_intermediate_screen_dynamic_components()

    return actions
