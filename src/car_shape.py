"""@file car_shape.py
@brief The drawing of a car, so that cars look like cars and not colour blocks.

A car is a compound turtle shape inside a 40 x 20 pixel footprint, front to the
left: lower body, cabin, two windows, a headlight and two wheels. The geometry
is plain data (see car_components) so it can be tested without a display.
"""

from turtle import Shape, TurtleScreen

from constants import (
    CAR_GLASS_COLOR,
    CAR_LIGHT_COLOR,
    CAR_OUTLINE_COLOR,
    CAR_TYRE_COLOR,
    COLORS,
)

## One polygon of a car: its points, fill colour and outline colour.
Component = tuple[tuple[tuple[float, float], ...], str, str]


def shape_name(color: str) -> str:
    """@brief Name under which the car shape of a colour is registered.

    @param color A turtle colour name from constants.COLORS.
    @return The registered shape name.
    """
    return f"car-{color}"


def _wheel(
    center_x: float, center_y: float, radius: float
) -> tuple[tuple[float, float], ...]:
    """@brief An octagon that stands in for a wheel."""
    offsets = (
        (1, 0),
        (0.7, 0.7),
        (0, 1),
        (-0.7, 0.7),
        (-1, 0),
        (-0.7, -0.7),
        (0, -1),
        (0.7, -0.7),
    )
    return tuple(
        (center_x + radius * dx, center_y + radius * dy) for dx, dy in offsets
    )


def car_components(color: str) -> list[Component]:
    """@brief The polygons that make up a car, drawn bottom to top.

    @param color Fill colour of the body and the cabin.
    @return The components, all inside x -20..20 and y -10..10, front at -x.
    """
    return [
        # lower body with a short sloped nose
        (((-20, -5), (20, -5), (20, 2), (-16, 2), (-20, -1)), color, CAR_OUTLINE_COLOR),
        # cabin
        (((-7, 2), (-3, 9), (10, 9), (14, 2)), color, CAR_OUTLINE_COLOR),
        # front and rear window
        (((-5, 2), (-2, 7), (2, 7), (2, 2)), CAR_GLASS_COLOR, CAR_OUTLINE_COLOR),
        (((4, 2), (4, 7), (9, 7), (12, 2)), CAR_GLASS_COLOR, CAR_OUTLINE_COLOR),
        # headlight at the front
        (
            ((-20, -2), (-18, -2), (-18, 0), (-20, 0)),
            CAR_LIGHT_COLOR,
            CAR_OUTLINE_COLOR,
        ),
        # wheels
        (_wheel(-11, -6, 4), CAR_TYRE_COLOR, CAR_OUTLINE_COLOR),
        (_wheel(11, -6, 4), CAR_TYRE_COLOR, CAR_OUTLINE_COLOR),
    ]


def register_car_shapes(screen: TurtleScreen) -> None:
    """@brief Register one car shape per colour with the screen.

    @param screen The turtle screen that will draw the cars.
    """
    for color in COLORS:
        shape = Shape("compound")
        for polygon, fill, outline in car_components(color):
            shape.addcomponent(polygon, fill, outline)
        screen.register_shape(shape_name(color), shape)
