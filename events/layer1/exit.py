#!/usr/bin/python3

"""
This module contains the events to be carried out when the PLAY button is
being pressed.
"""

from tkinter import messagebox


def on_click(instance_of_main_class):
    """
    Actions which will take place when the EXIT button is clicked
    by the user.
    """

    def actions(*events):
        choice = messagebox.askyesno(
            title="Exit", message="Are you sure you want to exit ?"
        )

        if choice:
            instance_of_main_class.end()

    return actions
