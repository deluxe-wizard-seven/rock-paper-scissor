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
    Actions which will take place when the BACK button is clicked
    by the user.
    """

    def actions(*events):
        instance_of_main_class.number_of_rounds = None

        remove_field(
            instance_of_main_class.number_of_rounds_label,
            instance_of_main_class.text_box,
            instance_of_main_class.button_next,
            instance_of_main_class.button_back,
        )

        instance_of_main_class.load_starting_screen_dynamic_components()

    return actions
