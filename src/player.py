"""@file player.py
@brief The turtle the user controls.
"""

from turtle import Turtle

from constants import FINISH_LINE_Y, MOVE_DISTANCE, STARTING_POSITION


class Player(Turtle):
    """@brief The turtle that crosses the road; it can only move forward (north)."""

    def __init__(self) -> None:
        """@brief Create the player at the starting position, facing north."""
        super().__init__(shape="turtle")
        self.penup()
        self.setheading(90)
        self.go_to_start()

    def go_up(self) -> None:
        """@brief Move one step north."""
        self.forward(MOVE_DISTANCE)

    def is_at_finish_line(self) -> bool:
        """@brief Tell whether the player has crossed the road.

        @return True when the player is above the finish line.
        """
        return self.ycor() > FINISH_LINE_Y

    def go_to_start(self) -> None:
        """@brief Put the player back at the starting position."""
        self.goto(STARTING_POSITION)
