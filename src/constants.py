"""@file constants.py
@brief Every constant of the Turtle Crossing game, defined once.
"""

## Screen size in pixels.
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
## Seconds to sleep between two frames of the game loop.
LOOP_DELAY = 0.1

## Where the player starts, and how far one key press moves it.
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
## The player has crossed when its y coordinate is above this value.
FINISH_LINE_Y = 280
## Half the width and height of the player used for collision tests.
PLAYER_HALF_SIZE = 8

## Car colours, one registered shape per colour.
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
## Distance a car moves per frame on level 1, and the speed-up per level.
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
## Car footprint in pixels; the drawn shape fits inside it.
CAR_LENGTH = 40
CAR_HEIGHT = 20
## A new car is created when a die with this many sides shows 1.
SPAWN_ODDS = 6
## No cars in the top and bottom strip of this height.
SAFE_ZONE = 50

## Scoreboard text.
FONT = ("Courier", 24, "normal")
SCOREBOARD_POSITION = (-280, 250)
GAME_OVER_TEXT = "GAME OVER"
