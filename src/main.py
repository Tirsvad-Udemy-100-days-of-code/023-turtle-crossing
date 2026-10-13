"""@file main.py
@brief Entry point: sets up the screen and runs the game loop.
"""

import time
from turtle import Screen

from car_manager import CarManager
from constants import LOOP_DELAY, SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from scoreboard import Scoreboard


def main() -> None:
    """@brief Run the game until the player is hit by a car."""
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.tracer(0)

    player = Player()
    screen.listen()
    screen.onkey(player.go_up, "Up")

    game_is_on = True
    while game_is_on:
        time.sleep(LOOP_DELAY)
        screen.update()


if __name__ == "__main__":
    main()
