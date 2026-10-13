"""@file player.py
@brief The turtle the user controls.
"""

from turtle import Turtle

from constants import MOVE_DISTANCE, STARTING_POSITION


class Player(Turtle):
    """@brief The turtle that crosses the road; it can only move forward (north)."""

    def __init__(self) -> None:
        """@brief Create the player at the starting position, facing north."""
        super().__init__(shape="turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def go_up(self) -> None:
        """@brief Move one step north."""
        self.forward(MOVE_DISTANCE)
