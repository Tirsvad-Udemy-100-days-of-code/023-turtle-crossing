"""Tests for the CarManager, using a fake car so no window is needed."""

import random

from car_manager import CarManager
from constants import (
    CAR_REMOVE_X,
    CAR_START_X,
    CAR_Y_LIMIT,
    MOVE_INCREMENT,
    SAFE_ZONE,
    SCREEN_HEIGHT,
    SPAWN_ODDS,
    STARTING_MOVE_DISTANCE,
)


class FakeCar:
    """Stands in for a turtle car."""

    def __init__(self) -> None:
        self.x = 0.0
        self.y = 0.0
        self.shape_name = ""
        self.hidden = False

    def penup(self) -> None:
        """Nothing to lift: a fake draws nothing."""

    def shape(self, name: str) -> None:
        self.shape_name = name

    def goto(self, x: float, y: float) -> None:
        self.x, self.y = x, y

    def xcor(self) -> float:
        return self.x

    def setx(self, x: float) -> None:
        self.x = x

    def hideturtle(self) -> None:
        self.hidden = True


class AlwaysOne(random.Random):
    """Random source whose die always shows 1, so a car is always created."""

    def randint(self, a: int, b: int) -> int:
        return 1 if (a, b) == (1, SPAWN_ODDS) else super().randint(a, b)


def make_manager(rng: random.Random | None = None) -> CarManager:
    return CarManager(car_factory=FakeCar, rng=rng or AlwaysOne(1))


def test_create_cars_places_car_at_right_edge() -> None:
    manager = make_manager()
    manager.create_cars()
    assert [car.x for car in manager.all_cars] == [CAR_START_X]


def test_cars_stay_out_of_the_safe_zone() -> None:
    manager = make_manager()
    for _ in range(500):
        manager.create_cars()
    ys = [car.y for car in manager.all_cars]
    assert min(ys) >= -(SCREEN_HEIGHT / 2 - SAFE_ZONE)
    assert max(ys) <= SCREEN_HEIGHT / 2 - SAFE_ZONE
    assert max(abs(y) for y in ys) <= CAR_Y_LIMIT


def test_a_car_is_created_about_one_call_in_six() -> None:
    manager = make_manager(random.Random(7))
    for _ in range(6000):
        manager.create_cars()
    assert 800 < len(manager.all_cars) < 1200


def test_cars_get_a_registered_car_shape() -> None:
    manager = make_manager()
    manager.create_cars()
    assert manager.all_cars[0].shape_name.startswith("car-")


def test_move_cars_moves_left_by_move_distance() -> None:
    manager = make_manager()
    manager.create_cars()
    manager.move_cars()
    assert manager.all_cars[0].x == CAR_START_X - STARTING_MOVE_DISTANCE


def test_cars_past_the_left_edge_are_removed() -> None:
    manager = make_manager()
    manager.create_cars()
    car = manager.all_cars[0]
    car.x = CAR_REMOVE_X
    manager.move_cars()
    assert manager.all_cars == [] and car.hidden


def test_level_up_increases_speed() -> None:
    manager = make_manager()
    manager.level_up()
    assert manager.move_distance == STARTING_MOVE_DISTANCE + MOVE_INCREMENT
