#!/usr/bin/python3

"""
This contains the GUI implementation of Rock, Paper and Scissors game
using tkinter.
"""

from time import sleep
from constants.moves import Moves
from constants.colors_table import color
from constants.constants import (
    width,
    height,
    font_size,
    font_style,
    common_formatting_options,
    rock_unicode,
    rock_image_url,
    paper_unicode,
    paper_image_url,
    scissor_unicode,
    scissor_image_url,
    scaling_factor,
    background_image_url,
    background_image_scaling_factor,
    canvas_text_x,
    canvas_text_y,
    __project_name__,
)
from events.layer1.__utils__ import remove_field
from events.layer2.__utils__ import resize_image
from effects.layer1 import (
    about as effects_about,
    play as effects_play,
    submit as effects_submit,
    back as effects_back,
    exit as effects_exit,
)
from events.layer1 import (
    about as events_about,
    play as events_play,
    submit as events_next,
    back as events_back,
    exit as events_exit,
)
from effects.layer2 import (
    clear as effects_clear_choice,
    submit as effects_submit_choice,
)
from events.layer2 import clear as events_clear_choice, submit as events_submit_choice
from tkinter import (
    Tk,
    Canvas,
    BOTH,
    NW,
    Button,
    CENTER,
    StringVar,
    Label,
    RAISED,
    Text,
    Frame,
    messagebox,
    IntVar,
    Radiobutton,
)


class GUI:
    """
    This class contains the gui components and their implementation.
    """

    def __init__(self, game_engine):
        self.unicode = {
            Moves.ROCK: rock_unicode,
            Moves.PAPER: paper_unicode,
            Moves.SCISSOR: scissor_unicode,
        }
        self.image_url = {
            Moves.ROCK: rock_image_url,
            Moves.PAPER: paper_image_url,
            Moves.SCISSOR: scissor_image_url,
        }
        self.root = None
        self.mode = None
        self.width = width
        self.height = height
        self.font_style = font_style
        self.font_size = font_size
        self.common_formatting_options = common_formatting_options
        self.scaling_factor = scaling_factor
        self.game_engine = game_engine

    def update_root(self):
        """
        This method is used to update the current tkinter window.
        """

        self.root.update()

    def config_status_label(self, fg):
        """
        This method is used to configure the status label.
        """

        self.status_label.config(fg=fg)

    def set_status(self, status: str):
        """
        This method is used to set status.
        """

        self.status.set(status)

    def set_player_score(self, player: int, score: int):
        """
        This method is used to set the score of the current player.
        """

        assert player in (1, 2), "Invalid Player"

        if player == 1:
            self.player_1_score.set(str(score))
        else:
            self.player_2_score.set(str(score))

    def destroy_move(self, player: int):
        """
        This method is used to destroy the move of the current player.
        """

        assert player in (1, 2), "Invalid Player"

        if player == 1:
            remove_field(self.player_1_move)
        else:
            remove_field(self.player_2_move)

    def place_next_move(self):
        """
        This method is used to place the next random move, played by the
        computer on the screen.
        """

        result = self.game_engine.generate_next_move()

        assert result in (
            Moves.ROCK,
            Moves.PAPER,
            Moves.SCISSOR,
        ), f"Invalid Move [{result=}]"
        assert self.game_engine.computer_side in (
            "left",
            "right",
        ), f"Invalid Side [{computer_side=}]"

        if self.game_engine.computer_side == "right":
            choice_rock = self.right_choice_rock
            choice_paper = self.right_choice_paper
            choice_scissor = self.right_choice_scissor
            radio_button_rock = self.right_radio_button_rock
            radio_button_paper = self.right_radio_button_paper
            radio_button_scissor = self.right_radio_button_scissor
            button_submit_choice = self.right_button_submit_choice
            button_clear_choice = self.right_button_clear_choice
        else:
            choice_rock = self.left_choice_rock
            choice_paper = self.left_choice_paper
            choice_scissor = self.left_choice_scissor
            radio_button_rock = self.left_radio_button_rock
            radio_button_paper = self.left_radio_button_paper
            radio_button_scissor = self.left_radio_button_scissor
            button_submit_choice = self.left_button_submit_choice
            button_clear_choice = self.left_button_clear_choice

        if result == Moves.ROCK:
            radio_button_rock.select()
            choice = resize_image(self.image_url[Moves.ROCK], self.scaling_factor * 2)
        elif result == Moves.PAPER:
            radio_button_paper.select()
            choice = resize_image(self.image_url[Moves.PAPER], self.scaling_factor * 2)
        elif result == Moves.SCISSOR:
            radio_button_scissor.select()
            choice = resize_image(
                self.image_url[Moves.SCISSOR], self.scaling_factor * 2
            )

        remove_field(
            choice_rock,
            choice_paper,
            choice_scissor,
            radio_button_rock,
            radio_button_paper,
            radio_button_scissor,
            button_submit_choice,
            button_clear_choice,
        )

        self.player_2_move = Label(self.root, image=choice, borderwidth=0)
        self.player_2_move.image = choice

        assert self.game_engine.computer_side in ("left", "right"), f"Invalid Side [{self.game_engine.computer_side=}]"

        if self.game_engine.computer_side == "right":
            self.player_2_move.place(x=self.width // 2 + 120, y=100)
        else:
            self.player_2_move.place(x=120, y=100)

    def load_initial_window(self):
        """
        This method will initialize the main window and its contents which
        will remain fixed all through out, till the window is open.
        """

        # Creating the root/master window
        self.root = Tk()

        # Setting up the geometry of the screen
        self.root.geometry(f"{self.width}x{self.height}")

        # Disabling the option of maximizing from either end
        self.root.resizable(False, False)

        # Setting up the title of the root window
        self.root.title(
            "Rock(%s), Paper(%s) and Scissors(%s)"
            % (
                self.unicode[Moves.ROCK],
                self.unicode[Moves.PAPER],
                self.unicode[Moves.SCISSOR],
            )
        )

        self.load_starting_screen_static_components()

    def load_starting_screen_static_components(self):
        """
        This method is the starting point of the gameplay. It contains
        the implementation of the first layer of the game.

        This method is responsible for all the components of the game in the
        first layer which will remain static all throughout the game, which
        includes the background image and the text on the image only.

        This function will automatically call the next level of the layer. So
        calling this function will create a chain of function calls which will
        lead to the proper channeling of data and control flow of the game.
        """

        # Resizing the image
        self.bg_image = resize_image(
            background_image_url, background_image_scaling_factor
        )

        # Setting up that image as the background
        self.canvas = Canvas(self.root, width=self.width, height=self.height)

        # Packing and filling up the canvas
        self.canvas.pack(fill=BOTH, expand=True)

        # Pasting the image as the background
        self.canvas.create_image(0, 0, image=self.bg_image, anchor=NW)

        self.canvas.create_text(
            canvas_text_x,
            canvas_text_y,
            text=__project_name__,
            font=(self.font_style, self.font_size * 2),
            fill=color["white"],
        )

        self.load_starting_screen_dynamic_components()

    def load_starting_screen_dynamic_components(self):
        """
        This method deals with all the dynamic components of the first layer
        which includes ABOUT, PLAY and EXIT buttons only.
        """

        # Creating the buttons to operate the control flow of the game play
        self.button_about = Button(
            self.canvas,
            text="ABOUT",
            **self.common_formatting_options,
            command=events_about.on_click,
        )
        self.button_play = Button(
            self.canvas,
            text="PLAY",
            **self.common_formatting_options,
            command=events_play.on_click(self),
        )
        self.button_exit = Button(
            self.canvas,
            text="EXIT",
            **self.common_formatting_options,
            command=events_exit.on_click(self),
        )

        # Obtaining the x and y co-ordinates of the three buttons
        x = (self.width // 7 - 47, 55 + 3 * self.width // 7, 72 + 5 * self.width // 7)
        y = self.height * 0.87

        # Setting up the buttons created within the window
        self.canvas.create_window(x[0], y, anchor=NW, window=self.button_about)
        self.canvas.create_window(x[1], y, anchor=NW, window=self.button_play)
        self.canvas.create_window(x[2], y, anchor=NW, window=self.button_exit)

        # Binding the actions of the buttons to their respective effects and actions
        self.button_about.bind("<Enter>", effects_about.on_enter(self))
        self.button_about.bind("<Leave>", effects_about.on_leave(self))
        self.button_play.bind("<Enter>", effects_play.on_enter(self))
        self.button_play.bind("<Leave>", effects_play.on_leave(self))
        self.button_exit.bind("<Enter>", effects_exit.on_enter(self))
        self.button_exit.bind("<Leave>", effects_exit.on_leave(self))

    def load_intermediate_screen_dynamic_components(self):
        """
        This method gets called after the player presses the PLAY button. It deals with
        inputting the number of rounds the user is willing to play.
        """

        # Obtaining the x and y co-ordinates of the three components
        x = (
            1 * self.width // 9 - 40,
            3 * self.width // 9 - 85,
            5 * self.width // 9 + 215,
            7 * self.width // 9 + 80,
        )
        y = self.height * 0.87

        # Creating the label which will prompt the user to input the
        # number of rounds they are willing to play.
        self.number_of_rounds_label = Label(
            self.canvas,
            text="NUMBER OF ROUNDS",
            relief=RAISED,
            **self.common_formatting_options,
        )

        # Creating the text box from where the user will input the number
        # of rounds the user is willing to play.
        self.text_box = Text(self.canvas, height=1, width=60)

        # Creating the submit button
        self.button_next = Button(
            self.canvas,
            text="NEXT",
            **self.common_formatting_options,
            command=events_next.on_click(self),
        )

        # Creating the back button
        self.button_back = Button(
            self.canvas,
            text="BACK",
            **self.common_formatting_options,
            command=events_back.on_click(self),
        )

        # Placing the widgets in their respective locations
        self.canvas.create_window(x[1], y + 3, anchor=NW, window=self.text_box)
        self.canvas.create_window(
            x[0], y, anchor=NW, window=self.number_of_rounds_label
        )
        self.canvas.create_window(x[2], y, anchor=NW, window=self.button_next)
        self.canvas.create_window(x[3], y, anchor=NW, window=self.button_back)

        # Binding the actions of the different widgets to their respective
        # action calls
        self.button_next.bind("<Enter>", effects_submit.on_enter(self))
        self.button_next.bind("<Leave>", effects_submit.on_leave(self))
        self.button_back.bind("<Enter>", effects_back.on_enter(self))
        self.button_back.bind("<Leave>", effects_back.on_leave(self))

    def load_playground_static_components(self):
        """
        This method marks the starting point of the second layer
        (aka the playground) and it is used to load all the static components
        of the second layer of the game.
        """

        self.root["bg"] = color["dark_grey_1"]

        # Creating the top frame which will contain the status label
        self.status_frame = Frame(
            self.root, height=45, width=self.width, bg=color["dark_grey_2"]
        )

        self.status_frame.pack_propagate(False)

        # Creating the top frame which will contain the status label
        self.bottom_frame = Frame(
            self.root, height=45, width=self.width, bg=color["dark_grey_2"]
        )

        self.bottom_frame.pack_propagate(False)

        # Creating the divider frame
        self.divider_frame = Frame(
            self.root, height=self.height - 67, width=20, bg=color["dark_grey_1"]
        )

        self.divider_frame.pack_propagate(False)

        # Creating the left marginal frame
        self.left_frame = Frame(
            self.root, height=self.height - 67, width=10, bg=color["dark_grey_2"]
        )

        self.left_frame.pack_propagate(False)

        # Creating the right marginal frame
        self.right_frame = Frame(
            self.root, height=self.height - 67, width=10, bg=color["dark_grey_2"]
        )

        self.right_frame.pack_propagate(False)

        self.status = StringVar()
        self.status.set(__project_name__)

        # Creating the top status label
        self.status_label = Label(
            self.status_frame,
            bg=color["dark_grey_2"],
            fg=color["lemon_yellow"],
            textvariable=self.status,
            padx=10,
            font=("Mono", int(self.font_size * 2.5)),
        )

        # Creating the instances of the marginal left and right window
        self.left_window = Frame(
            self.root,
            width=(self.width - 40) // 2,
            height=self.height - 182,
            bg=color["sky_blue"],
        )

        self.right_window = Frame(
            self.root,
            width=(self.width - 40) // 2,
            height=self.height - 182,
            bg=color["lime_green"],
        )

        # Creating the main instances of the left and right window
        self.left_main_frame = Frame(
            self.root,
            width=(self.width - 40) // 2 - 4,
            height=self.height - 237,
            bg=color["dark_grey_3"],
        )

        self.right_main_frame = Frame(
            self.root,
            width=(self.width - 40) // 2 - 4,
            height=self.height - 237,
            bg=color["dark_grey_3"],
        )

        # Creating the left and right name frames where upon the names of
        # both the players will be displayed on the screen
        self.left_name_frame = Frame(
            self.root,
            width=(self.width - 40) // 2 - 4,
            height=50,
            bg=color["dark_grey_2"],
        )

        self.right_name_frame = Frame(
            self.root,
            width=(self.width - 40) // 2 - 4,
            height=50,
            bg=color["dark_grey_2"],
        )

        assert self.game_engine.computer_side in (
            "left",
            "right",
        ), f"Invalid Side [{self.game_engine.computer_side=}]"

        if self.game_engine.computer_side == "left":
            left_player, right_player = "Computer", "You"
        else:
            left_player, right_player = "You", "Computer"

        # Creating the label which will contain the names of the players
        # in the screen
        self.left_name_label = Label(
            self.root,
            bg=color["dark_grey_1"],
            fg=color["sky_blue"],
            font=("Mono", 20),
            padx=10,
            text=left_player,
        )

        self.right_name_label = Label(
            self.root,
            bg=color["dark_grey_1"],
            fg=color["lime_green"],
            font=("Mono", 20),
            padx=10,
            text=right_player,
        )

        self.player_1_score = StringVar()
        self.player_1_score.set(str(self.game_engine.player[1]["score"]))

        self.player_2_score = StringVar()
        self.player_2_score.set(str(self.game_engine.player[2]["score"]))

        self.points_frame = [None] * 6

        self.points_frame[0] = Frame(
            self.root,
            height=58,
            width=(self.width - 20) // 3,
            bg=color["dark_grey_1"],
        )

        self.points_frame[1] = Frame(
            self.root,
            height=58,
            width=(self.width - 20) // 3,
            bg=color["dark_grey_1"],
        )

        self.points_frame[2] = Frame(
            self.root,
            height=58,
            width=(self.width - 20) // 3 + 2,
            bg=color["dark_grey_1"],
        )

        self.points_frame[3] = Frame(
            self.root,
            height=54,
            width=(self.width - 28) // 3,
            bg=color["dark_grey_2"],
        )

        self.points_frame[4] = Frame(
            self.root,
            height=54,
            width=(self.width - 28) // 3,
            bg=color["dark_grey_2"],
        )

        self.points_frame[5] = Frame(
            self.root,
            height=54,
            width=(self.width - 28) // 3,
            bg=color["dark_grey_2"],
        )

        # Creating the points table
        self.points_label = [None] * 6

        assert self.game_engine.computer_side in (
            "left",
            "right",
        ), f"Invalid Side [{self.game_engine.computer_side=}]"

        if self.game_engine.computer_side == "right":
            self.points_label[0] = Label(
                self.root,
                bg=color["dark_grey_1"],
                fg=color["sky_blue"],
                font=("Mono", 15, "underline"),
                padx=10,
                text="YOUR SCORE",
            )

            self.points_label[1] = Label(
                self.root,
                bg=color["dark_grey_1"],
                fg=color["lime_green"],
                font=("Mono", 15, "underline"),
                padx=10,
                text="COMPUTER'S SCORE",
            )

            self.points_label[3] = Label(
                self.root,
                bg=color["dark_grey_2"],
                fg=color["sky_blue"],
                font=("Mono", 20, "bold"),
                padx=10,
                textvariable=self.player_1_score,
            )

            self.points_label[4] = Label(
                self.root,
                bg=color["dark_grey_2"],
                fg=color["lime_green"],
                font=("Mono", 20, "bold"),
                padx=10,
                textvariable=self.player_2_score,
            )
        else:
            self.points_label[0] = Label(
                self.root,
                bg=color["dark_grey_1"],
                fg=color["lime_green"],
                font=("Mono", 15, "underline"),
                padx=10,
                text="YOUR SCORE",
            )

            self.points_label[1] = Label(
                self.root,
                bg=color["dark_grey_1"],
                fg=color["sky_blue"],
                font=("Mono", 15, "underline"),
                padx=10,
                text="COMPUTER'S SCORE",
            )

            self.points_label[3] = Label(
                self.root,
                bg=color["dark_grey_2"],
                fg=color["lime_green"],
                font=("Mono", 20, "bold"),
                padx=10,
                textvariable=self.player_1_score,
            )

            self.points_label[4] = Label(
                self.root,
                bg=color["dark_grey_2"],
                fg=color["sky_blue"],
                font=("Mono", 20, "bold"),
                padx=10,
                textvariable=self.player_2_score,
            )

        self.points_label[2] = Label(
            self.root,
            bg=color["dark_grey_1"],
            fg=color["red_orange"],
            font=("Mono", 15, "underline"),
            padx=10,
            text="TOTAL",
        )

        self.points_label[5] = Label(
            self.root,
            bg=color["dark_grey_2"],
            fg=color["red_orange"],
            font=("Mono", 20, "bold"),
            padx=10,
            text=str(self.game_engine.number_of_rounds),
        )

        # Placing the widgets on the screen
        self.status_frame.place(x=0, y=0)
        self.status_label.place(x=self.width // 2, y=22, anchor=CENTER)

        self.left_frame.place(x=0, y=45)

        self.right_frame.place(x=self.width - 10, y=45)

        self.divider_frame.place(x=self.width // 2 - 10, y=45)

        self.bottom_frame.place(x=0, y=self.height - 22)

        self.left_window.place(x=10, y=45)

        self.right_window.place(x=self.width // 2 + 10, y=45)

        self.left_name_frame.place(x=12, y=47)
        self.left_name_label.place(x=self.width // 4, y=70, anchor=CENTER)

        self.right_name_frame.place(x=self.width // 2 + 12, y=47)
        self.right_name_label.place(x=3 * self.width // 4, y=70, anchor=CENTER)

        self.left_main_frame.place(x=12, y=95)

        self.right_main_frame.place(x=self.width // 2 + 12, y=95)

        self.points_frame[0].place(x=10, y=self.height - 140)
        self.points_label[0].place(x=self.width // 6, y=self.height - 112, anchor=CENTER)

        self.points_frame[1].place(x=10 + (self.width - 20) // 3, y=self.height - 140)
        self.points_label[1].place(
            x=(self.width - 20) // 3 + self.width // 6,
            y=self.height - 112,
            anchor=CENTER,
        )

        self.points_frame[2].place(
            x=10 + 2 * (self.width - 20) // 3 - 1, y=self.height - 140
        )
        self.points_label[2].place(
            x=2 * (self.width - 20) // 3 + self.width // 6 + 5,
            y=self.height - 112,
            anchor=CENTER,
        )

        self.points_frame[3].place(x=12, y=self.height - 78)
        self.points_label[3].place(x=self.width // 6, y=self.height - 51, anchor=CENTER)

        self.points_frame[4].place(x=12 + (self.width - 20) // 3, y=self.height - 78)
        self.points_label[4].place(
            x=(self.width - 20) // 3 + self.width // 6,
            y=self.height - 51,
            anchor=CENTER,
        )

        self.points_frame[5].place(
            x=12 + 2 * (self.width - 20) // 3, y=self.height - 78
        )
        self.points_label[5].place(
            x=2 * (self.width - 20) // 3 + self.width // 6 + 5,
            y=self.height - 51,
            anchor=CENTER,
        )

        self.game_engine.player[1]["choice"] = IntVar()
        self.game_engine.player[2]["choice"] = IntVar()

        self.load_playground_dynamic_components()

    def load_playground_dynamic_components(self):
        """
        This method contains the dynamic components of the labels representing
        the choices of the moves i.e. the move of ROCK, PAPER or SCISSOR
        which the player will play.
        """

        # Resizing the images
        resized_rock = resize_image(self.image_url[Moves.ROCK], self.scaling_factor)
        resized_paper = resize_image(self.image_url[Moves.PAPER], self.scaling_factor)
        resized_scissor = resize_image(
            self.image_url[Moves.SCISSOR], self.scaling_factor
        )

        # Creating the choices for the first player
        self.left_choice_rock = Label(
            self.root, image=resized_rock, borderwidth=0, anchor=NW
        )
        self.left_choice_rock.image = resized_rock
        self.left_choice_paper = Label(
            self.root, image=resized_paper, borderwidth=0, anchor=NW
        )
        self.left_choice_paper.image = resized_paper
        self.left_choice_scissor = Label(
            self.root, image=resized_scissor, borderwidth=0, anchor=NW
        )
        self.left_choice_scissor.image = resized_scissor

        # Creating the choices for the second player
        self.right_choice_rock = Label(
            self.root, image=resized_rock, borderwidth=0, anchor=NW
        )
        self.right_choice_rock.image = resized_rock
        self.right_choice_paper = Label(
            self.root, image=resized_paper, borderwidth=0, anchor=NW
        )
        self.right_choice_paper.image = resized_paper
        self.right_choice_scissor = Label(
            self.root, image=resized_scissor, borderwidth=0, anchor=NW
        )
        self.right_choice_scissor.image = resized_scissor

        # Creating the submit and clear selection buttons in the left section
        self.left_button_submit_choice = Button(
            self.root,
            text="SUBMIT",
            **self.common_formatting_options,
            borderwidth=0,
            command=events_submit_choice.on_click_left_button(self),
        )
        self.left_button_submit_choice.config(bg=color["dark_grey_3"])
        self.left_button_submit_choice.config(fg=color["royal_blue"])

        self.left_button_clear_choice = Button(
            self.root,
            text="CLEAR SELECTION",
            **self.common_formatting_options,
            borderwidth=0,
            command=events_clear_choice.on_click_left_button(self),
        )
        self.left_button_clear_choice.config(bg=color["dark_grey_3"])
        self.left_button_clear_choice.config(fg=color["red_orange"])

        # Creating the submit and clear selection buttons in the right section
        self.right_button_submit_choice = Button(
            self.root,
            text="SUBMIT",
            **self.common_formatting_options,
            borderwidth=0,
            command=events_submit_choice.on_click_right_button(self),
        )
        self.right_button_submit_choice.config(bg=color["dark_grey_3"])
        self.right_button_submit_choice.config(fg=color["royal_blue"])

        self.right_button_clear_choice = Button(
            self.root,
            text="CLEAR SELECTION",
            **self.common_formatting_options,
            borderwidth=0,
            command=events_clear_choice.on_click_right_button(self),
        )
        self.right_button_clear_choice.config(bg=color["dark_grey_3"])
        self.right_button_clear_choice.config(fg=color["red_orange"])

        common_kwargs = dict()

        assert self.game_engine.computer_side in (
            "left",
            "right",
        ), f"Invalid Side [{self.game_engine.computer_side=}]"

        if self.game_engine.computer_side == "right":
            player_variable_1 = self.game_engine.player[1]["choice"]
            player_variable_2 = self.game_engine.player[2]["choice"]
        else:
            player_variable_1 = self.game_engine.player[2]["choice"]
            player_variable_2 = self.game_engine.player[1]["choice"]

        common_kwargs[1] = {
            "text": "",
            "command": None,
            "bg": color["dark_grey_3"],
            "fg": color["raspberry"],
            "borderwidth": 0,
            "variable": player_variable_1,
        }

        common_kwargs[2] = {
            "text": "",
            "command": None,
            "bg": color["dark_grey_3"],
            "fg": color["raspberry"],
            "borderwidth": 0,
            "variable": player_variable_2,
        }

        # Creating the radio buttons required for choice selection
        self.left_radio_button_rock = Radiobutton(
            self.left_main_frame, **common_kwargs[1], value=1
        )

        self.left_radio_button_paper = Radiobutton(
            self.left_main_frame, **common_kwargs[1], value=2
        )

        self.left_radio_button_scissor = Radiobutton(
            self.left_main_frame, **common_kwargs[1], value=4
        )

        self.right_radio_button_rock = Radiobutton(
            self.right_main_frame, **common_kwargs[2], value=1
        )

        self.right_radio_button_paper = Radiobutton(
            self.right_main_frame, **common_kwargs[2], value=2
        )

        self.right_radio_button_scissor = Radiobutton(
            self.right_main_frame, **common_kwargs[2], value=4
        )

        # Binding actions to the respective actions/events and effects
        self.left_button_submit_choice.bind(
            "<Enter>", effects_submit_choice.on_enter(self)
        )
        self.left_button_submit_choice.bind(
            "<Leave>", effects_submit_choice.on_leave(self)
        )
        self.right_button_submit_choice.bind(
            "<Enter>", effects_submit_choice.on_enter(self)
        )
        self.right_button_submit_choice.bind(
            "<Leave>", effects_submit_choice.on_leave(self)
        )
        self.left_button_clear_choice.bind(
            "<Enter>", effects_clear_choice.on_enter(self)
        )
        self.left_button_clear_choice.bind(
            "<Leave>", effects_clear_choice.on_leave(self)
        )
        self.right_button_clear_choice.bind(
            "<Enter>", effects_clear_choice.on_enter(self)
        )
        self.right_button_clear_choice.bind(
            "<Leave>", effects_clear_choice.on_leave(self)
        )

        # Placing the choice labels
        self.left_choice_rock.place(x=24, y=125)
        self.left_choice_paper.place(x=183, y=125)
        self.left_choice_scissor.place(x=self.width // 2 - 159, y=125)
        self.right_choice_rock.place(x=self.width // 2 + 24, y=125)
        self.right_choice_paper.place(x=self.width // 2 + 183, y=125)
        self.right_choice_scissor.place(x=self.width - 159, y=125)

        assert self.game_engine.computer_side in (
            "left",
            "right",
        ), f"Invalid Side [{self.game_engine.computer_side=}]"

        if self.game_engine.computer_side == "right":
            self.left_radio_button_rock.place(x=60, y=240)
            self.left_radio_button_paper.place(x=220, y=240)
            self.left_radio_button_scissor.place(x=380, y=240)
            self.left_button_submit_choice.place(x=35, y=self.height - 195)
            self.left_button_clear_choice.place(
                x=self.width // 2 - 175, y=self.height - 195
            )
        else:
            self.right_radio_button_rock.place(x=60, y=240)
            self.right_radio_button_paper.place(x=220, y=240)
            self.right_radio_button_scissor.place(x=380, y=240)
            self.right_button_submit_choice.place(
                x=self.width // 2 + 35, y=self.height - 195
            )
            self.right_button_clear_choice.place(
                x=self.width - 175, y=self.height - 195
            )

    def ending_screen(self):
        """
        This is the last and final layer of the game. This will display the
        winner and also prompt the user to play again or quit from playing.
        This is the the last or final stage of the game. The control flows
        to the final __end__ method which is the end point of the game and
        where everything gets dumped at last.
        """

        self.update_root()
        sleep(1)

        assert self.game_engine.computer_side in (
            "left",
            "right",
        ), f"Invalid Side [{self.game_engine.computer_side=}]"
        assert self.game_engine.winner in (
            1,
            2,
        ), f"Invalid Winner [{self.game_engine.winner=}]"

        if self.game_engine.winner == 1:
            text = "Congratulations! You have won. :D"
        else:
            text = "Oops! You have lost this game. :("

        if self.game_engine.computer_side == "left":
            fg = color["sky_blue" if self.game_engine.winner - 1 else "lime_green"]
        else:
            fg = color["lime_green" if self.game_engine.winner - 1 else "sky_blue"]

        self.status_label.config(fg=fg)
        self.status.set(text)

        messagebox.showinfo(__project_name__, text)

        choice = messagebox.askyesno("Replay", "Do you want to play again ?")

        if choice:
            self.end()
            self.game_engine.play(replay=True)
        else:
            choice = messagebox.askyesno("Exit", "Do you want to exit this game ?")
            self.end()
            if not choice:
                self.game_engine.play(replay=True)

    def start(self):
        """
        This method is the entry point of the game play. The game engine needs
        to call this method in order to play this game.
        """

        self.load_initial_window()

        # The main event loop
        self.root.mainloop()

    def end(self):
        """
        This function is the end point of the game. This is used to
        close everything securely.
        """

        remove_field(self.root)

        # Deleting all the available components
        del self
