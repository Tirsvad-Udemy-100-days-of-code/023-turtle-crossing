"""Tests for the Player class (need a display; skipped without one)."""

import pytest

from constants import FINISH_LINE_Y, MOVE_DISTANCE, STARTING_POSITION
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


def test_player_is_not_at_finish_line_at_start(player: Player) -> None:
    assert not player.is_at_finish_line()


def test_player_is_at_finish_line_above_finish_y(player: Player) -> None:
    player.goto(0, FINISH_LINE_Y + 1)
    assert player.is_at_finish_line()


def test_go_to_start_returns_to_starting_position(player: Player) -> None:
    player.goto(0, FINISH_LINE_Y + 1)
    player.go_to_start()
    assert player.position() == STARTING_POSITION


def test_go_up_never_moves_sideways(player: Player) -> None:
    for _ in range(5):
        player.go_up()
    assert player.xcor() == pytest.approx(STARTING_POSITION[0])
