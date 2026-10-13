# Architecture

🌐 **English** · [Dansk](Architecture-da) · [Bahasa Malaysia](Architecture-ms)

## Modules (`src/`)

| Module | Responsibility |
| --- | --- |
| `main.py` | Creates the screen, the objects and runs the game loop |
| `constants.py` | Every constant, defined once |
| `player.py` | `Player(Turtle)`: `go_up`, `is_at_finish_line`, `go_to_start` |
| `car_manager.py` | `CarManager`: `create_cars`, `move_cars`, `is_hit`, `level_up` |
| `car_shape.py` | The drawing of a car: body, cabin, windows, headlight, two wheels |
| `collision.py` | `is_colliding`: pure rectangle test, no turtle needed |
| `scoreboard.py` | `Scoreboard(Turtle)`: level text and `GAME OVER` |

## Design choices

- **Cars look like cars.** A car is a compound turtle shape inside the 40 x 20
  pixel footprint of the assignment. One shape is registered per colour, so no
  image files are needed.
- **Testable without a window.** Geometry (`car_components`), the collision
  test and the spawn rule are plain code. `CarManager` receives a car factory
  and a random source, so tests use a fake car and a seeded dice.
- **Collision uses the whole car.** The player is compared with the car's
  rectangle, not only with its centre.

## Documentation

Source comments are Doxygen comments. Build them with `doxygen Doxyfile`.
Planning and review documents are in `docs/`.

Back to [Home](Home).
