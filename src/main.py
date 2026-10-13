"""@file main.py
@brief Entry point: sets up the screen and runs the game loop.
"""

import time
from turtle import Screen

from car_manager import CarManager
from car_shape import register_car_shapes
from constants import LOOP_DELAY, SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from scoreboard import Scoreboard


def main() -> None:
    """@brief Run the game until the player is hit by a car."""
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.tracer(0)
    register_car_shapes(screen)

    player = Player()
    car_manager = CarManager()
    scoreboard = Scoreboard()
    screen.listen()
    screen.onkey(player.go_up, "Up")

    game_is_on = True
    while game_is_on:
        time.sleep(LOOP_DELAY)
        screen.update()
        car_manager.create_cars()
        car_manager.move_cars()

        if car_manager.is_hit(player):
            game_is_on = False
            scoreboard.game_over()

        if player.is_at_finish_line():
            player.go_to_start()
            car_manager.level_up()
            scoreboard.increase_level()

    screen.update()
    screen.exitonclick()


if __name__ == "__main__":
    main()
