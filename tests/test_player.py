"""Tests for the Player class (need a display; skipped without one)."""

import pytest

from constants import MOVE_DISTANCE, STARTING_POSITION
from player import Player


@pytest.fixture
def player(screen) -> Player:
    new_player = Player()
    yield new_player
    new_player.hideturtle()


def test_player_starts_at_starting_position(player: Player) -> None:
    assert player.position() == STARTING_POSITION


def test_player_faces_north(player: Player) -> None:
    assert player.heading() == 90


def test_go_up_moves_forward_by_move_distance(player: Player) -> None:
    start_y = player.ycor()
    player.go_up()
    assert player.ycor() == start_y + MOVE_DISTANCE


def test_go_up_never_moves_sideways(player: Player) -> None:
    for _ in range(5):
        player.go_up()
    assert player.xcor() == pytest.approx(STARTING_POSITION[0])
