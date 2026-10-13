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
## A car spawns just off the right edge and is removed once fully off the left.
CAR_START_X = SCREEN_WIDTH // 2 + CAR_LENGTH // 2
CAR_REMOVE_X = -(SCREEN_WIDTH // 2 + CAR_LENGTH)
## Cars are placed at a y coordinate within -CAR_Y_LIMIT..CAR_Y_LIMIT.
CAR_Y_LIMIT = SCREEN_HEIGHT // 2 - SAFE_ZONE
## Colours of the non-body parts of a car.
CAR_OUTLINE_COLOR = "black"
CAR_GLASS_COLOR = "light sky blue"
CAR_TYRE_COLOR = "black"
CAR_LIGHT_COLOR = "gold"

## Scoreboard text.
FONT = ("Courier", 24, "normal")
SCOREBOARD_POSITION = (-280, 250)
GAME_OVER_TEXT = "GAME OVER"
GAME_OVER_POSITION = (0, 0)
STARTING_LEVEL = 1
LEVEL_TEXT_PREFIX = "Level: "
