#!/usr/bin/python3

"""
This module contains the utility functions.
"""


def remove_field(*fields):
    """
    This function is used to remove all the fields passed into
    the function, from the current screen.

    NOTE : This function will only delete the fields passed to
           it if and only if that field contains the attribute
           delete.

           If there is no delete attribute present, then nothing
           will get deleted from the screen.
    """

    for field in fields:
        if "destroy" in dir(field):
            field.destroy()
