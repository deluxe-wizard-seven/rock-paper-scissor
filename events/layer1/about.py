#!/usr/bin/python3

"""
This module contains the events to be carried out when the ABOUT button is
being pressed.
"""

from tkinter import messagebox
from sys import stderr

try:
    from constants.constants import (
        __author__,
        __version__,
        __project_name__,
        __project_description__,
    )
except ImportError as e:
    print(e, file=stderr)


def on_click(*events):
    """
    Actions which will take place when the ABOUT button from the
    first level of the first layer is clicked by the user.
    """

    text = ""

    text += f"Project Name : {__project_name__}\n"
    text += f"Project Version : {__version__}\n"
    text += f"Project Author : {__author__}\n"
    text += f"Project Description : {__project_description__}\n"

    messagebox.showinfo(__project_name__, text)
