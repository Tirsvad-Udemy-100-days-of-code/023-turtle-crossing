"""Smoke tests for the constants module."""

from constants import CAR_HEIGHT, CAR_LENGTH, COLORS, SAFE_ZONE, SCREEN_HEIGHT


def test_car_footprint_matches_assignment() -> None:
    assert (CAR_LENGTH, CAR_HEIGHT) == (40, 20)


def test_safe_zone_leaves_room_for_cars() -> None:
    assert 0 < SAFE_ZONE < SCREEN_HEIGHT / 2


def test_colors_are_not_empty() -> None:
    assert COLORS
