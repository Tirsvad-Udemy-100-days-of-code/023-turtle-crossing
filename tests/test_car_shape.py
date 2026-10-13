"""Tests for the car drawing."""

from turtle import Turtle, TurtleScreen

from car_shape import (
    car_components,
    register_car_shapes,
    shape_name,
    to_shape_frame,
)
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


def test_register_car_shapes_adds_one_shape_per_colour(screen: TurtleScreen) -> None:
    register_car_shapes(screen)
    assert all(shape_name(color) in screen.getshapes() for color in COLORS)


def test_to_shape_frame_maps_screen_points_to_the_upright_shape_frame() -> None:
    assert to_shape_frame((-20, 0)) == (0, -20)  # front (screen left) -> shape -y
    assert to_shape_frame((20, 0)) == (0, 20)
    assert to_shape_frame((0, 10)) == (-10, 0)
    assert to_shape_frame((0, 0)) == (0, 0)


def test_drawn_car_is_horizontal(screen: TurtleScreen) -> None:
    register_car_shapes(screen)
    car = Turtle(visible=False)
    car.penup()
    car.shape(shape_name("red"))
    car.showturtle()
    try:
        screen.update()
        canvas = screen.getcanvas()
        # the first compound component is the lower body
        coords = canvas.coords(car.turtle._item[0])  # type: ignore[attr-defined]
        xs, ys = coords[0::2], coords[1::2]
        width, height = max(xs) - min(xs), max(ys) - min(ys)
        assert width > height
        assert width <= CAR_LENGTH
        assert height <= CAR_HEIGHT
    finally:
        car.hideturtle()
