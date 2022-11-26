#!/usr/bin/python3

"""
This module contains all the constants which are used in the game.
"""

from tkinter import CENTER
from sys import stderr
from os import getcwd
from os.path import exists, join
from functools import reduce

try:
    from constants.colors_table import color
except ImportError as e:
    print(e, file=stderr)

__project_name__ = "Rock, Paper and Scissors Game"
__author__ = "Dipto Bhattacharjee"
__version__ = "1.0.0"
__project_description__ = "A simple rock, paper and scissors game created using tkinter module in python. This game follows the normal conventions of the game where the rock crushes the scissor, the paper covers the rock and the scissor cuts the paper."

rock_unicode = "\u270a"
paper_unicode = "\u270b"
scissor_unicode = "\u270c"

rock_image_url = reduce(join, [getcwd(), "images", "rock.png"])
assert exists(rock_image_url), "Rock Image Not Found"

paper_image_url = reduce(join, [getcwd(), "images", "paper.png"])
assert exists(paper_image_url), "Paper Image Not Found"

scissor_image_url = reduce(join, [getcwd(), "images", "scissor.png"])
assert exists(scissor_image_url), "Scissor Image Not Found"

background_image_url = reduce(join, [getcwd(), "images", "background_image.png"])
assert exists(background_image_url), "Background Image Not Found"

background_image_scaling_factor = 0.5

width = 1000
height = 668
font_style = "Helvetica"
font_size = 10

canvas_text_x = width // 2
canvas_text_y = 0.135 * height

common_formatting_options = {
    "padx": 5,
    "pady": 5,
    "justify": CENTER,
    "bg": color["dark_grey_1"],
    "fg": color["white"],
    "font": ("Helvetica", 10, "bold")
}

scaling_factor = 135 / 534
