"""@file scoreboard.py
@brief Shows the level and the game over message.
"""

from turtle import Turtle

from constants import (
    FONT,
    GAME_OVER_POSITION,
    GAME_OVER_TEXT,
    LEVEL_TEXT_PREFIX,
    SCOREBOARD_POSITION,
    STARTING_LEVEL,
)


class Scoreboard(Turtle):
    """@brief Writes the current level and the game over message."""

    def __init__(self) -> None:
        """@brief Create the scoreboard and write level 1."""
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.level = STARTING_LEVEL
        self.update_scoreboard()

    @property
    def level_text(self) -> str:
        """@brief The text shown for the current level."""
        return f"{LEVEL_TEXT_PREFIX}{self.level}"

    def update_scoreboard(self) -> None:
        """@brief Clear the board and write the current level."""
        self.clear()
        self.goto(SCOREBOARD_POSITION)
        self.write(self.level_text, align="left", font=FONT)

    def increase_level(self) -> None:
        """@brief Go up one level and redraw the board."""
        self.level += 1
        self.update_scoreboard()

    def game_over(self) -> None:
        """@brief Write the game over message in the middle of the screen."""
        self.goto(GAME_OVER_POSITION)
        self.write(GAME_OVER_TEXT, align="center", font=FONT)
