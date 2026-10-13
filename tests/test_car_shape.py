"""Tests for the car drawing."""

from car_shape import car_components, register_car_shapes, shape_name
from constants import CAR_HEIGHT, CAR_LENGTH, COLORS


def test_car_fits_the_footprint() -> None:
    points = [p for polygon, _, _ in car_components("red") for p in polygon]
    assert all(abs(x) <= CAR_LENGTH / 2 for x, _ in points)
    assert all(abs(y) <= CAR_HEIGHT / 2 for _, y in points)


def test_car_is_more_than_a_colour_block() -> None:
    components = car_components("red")
    fills = [fill for _, fill, _ in components]
    assert fills.count("black") == 2  # two wheels
    assert "light sky blue" in fills  # windows
    assert len(components) >= 5


def test_body_and_cabin_use_the_car_colour() -> None:
    fills = [fill for _, fill, _ in car_components("green")]
    assert fills.count("green") == 2


def test_register_car_shapes_adds_one_shape_per_colour(screen) -> None:
    register_car_shapes(screen)
    assert all(shape_name(color) in screen.getshapes() for color in COLORS)
