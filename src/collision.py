"""@file collision.py
@brief The collision rule between the player and a car, free of any window.
"""

from constants import CAR_HEIGHT, CAR_LENGTH, PLAYER_HALF_SIZE


def is_colliding(player_x: float, player_y: float, car_x: float, car_y: float) -> bool:
    """@brief Tell whether the player's square overlaps the car's rectangle.

    Touching edges is not a collision.

    @param player_x X coordinate of the player's centre.
    @param player_y Y coordinate of the player's centre.
    @param car_x X coordinate of the car's centre.
    @param car_y Y coordinate of the car's centre.
    @return True when the two shapes overlap.
    """
    is_overlapping_x = abs(player_x - car_x) < CAR_LENGTH / 2 + PLAYER_HALF_SIZE
    is_overlapping_y = abs(player_y - car_y) < CAR_HEIGHT / 2 + PLAYER_HALF_SIZE
    return is_overlapping_x and is_overlapping_y
