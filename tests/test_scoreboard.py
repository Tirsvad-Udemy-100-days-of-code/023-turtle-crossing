"""@file test_scoreboard.py
@brief Tests for the Scoreboard.
"""

from turtle import TurtleScreen

from scoreboard import Scoreboard


def test_level_starts_at_one(screen: TurtleScreen) -> None:
    assert Scoreboard().level == 1


def test_level_text_shows_level_one_at_start(screen: TurtleScreen) -> None:
    assert Scoreboard().level_text == "Level: 1"


def test_level_text_follows_level() -> None:
    board = Scoreboard.__new__(Scoreboard)
    board.level = 7
    assert board.level_text == "Level: 7"


def test_increase_level_adds_one(screen: TurtleScreen) -> None:
    board = Scoreboard()
    board.increase_level()
    assert board.level == 2
    assert board.level_text == "Level: 2"


def test_game_over_keeps_level(screen: TurtleScreen) -> None:
    board = Scoreboard()
    board.increase_level()
    board.game_over()
    assert board.level == 2
    assert board.position() == (0, 0)
