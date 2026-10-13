"""Tests for the pure collision rule."""

from collision import is_colliding
from constants import CAR_HEIGHT, CAR_LENGTH, PLAYER_HALF_SIZE

REACH_X = CAR_LENGTH / 2 + PLAYER_HALF_SIZE
REACH_Y = CAR_HEIGHT / 2 + PLAYER_HALF_SIZE


def test_hit_when_player_overlaps_car() -> None:
    assert is_colliding(5, 3, 0, 0)


def test_no_hit_when_beyond_car_half_length_horizontally() -> None:
    assert not is_colliding(REACH_X + 1, 0, 0, 0)


def test_no_hit_when_a_lane_away_vertically() -> None:
    assert not is_colliding(0, CAR_HEIGHT * 2, 0, 0)


def test_no_hit_when_exactly_at_horizontal_boundary() -> None:
    assert not is_colliding(REACH_X, 0, 0, 0)


def test_no_hit_when_exactly_at_vertical_boundary() -> None:
    assert not is_colliding(0, REACH_Y, 0, 0)


def test_hit_just_inside_the_boundary() -> None:
    assert is_colliding(REACH_X - 1, REACH_Y - 1, 0, 0)
