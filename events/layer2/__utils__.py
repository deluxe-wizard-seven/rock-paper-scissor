#!/usr/bin/python3

"""
This module contains the utility functions.
"""

from sys import stderr
from PIL import Image, ImageTk


def resize_image(image_url: str, scaling_factor: float = 1):
    """
    This method is used to scale the image with respect to its
    scaling factor keeping the aspect ratio of the picture
    constant.

    This function returns the resized image as the output if
    the image is found at the url. In case any exception occurs
    then None will be returned.
    """

    try:
        image = Image.open(image_url)
    except BaseException as e:
        print(e, file=stderr)
        return None
    else:
        new_height = int(image.height * scaling_factor)
        new_width = int(image.width * scaling_factor)
        image = image.resize((new_width, new_height), Image.ANTIALIAS)
        return ImageTk.PhotoImage(image)
