"""Shared fixtures. Tests that need a window skip when no display is available."""

import tkinter
import turtle

import pytest


@pytest.fixture(scope="session")
def screen() -> turtle.TurtleScreen:
    """A single hidden turtle screen shared by the tests that draw."""
    try:
        game_screen = turtle.Screen()
    except tkinter.TclError:
        pytest.skip("no display available")
    game_screen.tracer(0)
    game_screen.getcanvas().winfo_toplevel().withdraw()
    return game_screen
