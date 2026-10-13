"""@file car_manager.py
@brief Creates and moves the cars.
"""

import random
from collections.abc import Callable
from turtle import Turtle

from car_shape import shape_name
from constants import (
    CAR_REMOVE_X,
    CAR_START_X,
    CAR_Y_LIMIT,
    COLORS,
    MOVE_INCREMENT,
    SPAWN_ODDS,
    STARTING_MOVE_DISTANCE,
)


class CarManager:
    """@brief Keeps the cars of the road: creates, moves and removes them."""

    def __init__(
        self,
        car_factory: Callable[[], Turtle] = Turtle,
        rng: random.Random | None = None,
    ) -> None:
        """@brief Create a manager with no cars.

        @param car_factory Creates one car; replaced by a fake in tests.
        @param rng Random source; replaced by a seeded one in tests.
        """
        self._car_factory = car_factory
        self._rng = rng or random.Random()
        self.all_cars: list[Turtle] = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def create_cars(self) -> None:
        """@brief Create a car on one call in SPAWN_ODDS, at a random lane."""
        if self._rng.randint(1, SPAWN_ODDS) != 1:
            return
        car = self._car_factory()
        car.penup()
        car.shape(shape_name(self._rng.choice(COLORS)))
        car.goto(CAR_START_X, self._rng.randint(-CAR_Y_LIMIT, CAR_Y_LIMIT))
        self.all_cars.append(car)

    def move_cars(self) -> None:
        """@brief Move every car left and remove the ones that left the screen."""
        for car in self.all_cars:
            car.setx(car.xcor() - self.move_distance)
        for car in [car for car in self.all_cars if car.xcor() < CAR_REMOVE_X]:
            car.hideturtle()
            self.all_cars.remove(car)

    def level_up(self) -> None:
        """@brief Make the cars faster."""
        self.move_distance += MOVE_INCREMENT
