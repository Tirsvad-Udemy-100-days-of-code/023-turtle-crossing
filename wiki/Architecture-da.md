# Arkitektur

🌐 [English](Architecture) · **Dansk** · [Bahasa Malaysia](Architecture-ms)

## Moduler (`src/`)

| Modul | Ansvar |
| --- | --- |
| `main.py` | Opretter skærmen og objekterne og kører spilløkken |
| `constants.py` | Alle konstanter, defineret ét sted |
| `player.py` | `Player(Turtle)`: `go_up`, `is_at_finish_line`, `go_to_start` |
| `car_manager.py` | `CarManager`: `create_cars`, `move_cars`, `is_hit`, `level_up` |
| `car_shape.py` | Tegningen af en bil: karrosseri, kabine, ruder, forlygte, to hjul |
| `collision.py` | `is_colliding`: ren rektangeltest, uden turtle |
| `scoreboard.py` | `Scoreboard(Turtle)`: niveautekst og `GAME OVER` |

## Designvalg

- **Biler ligner biler.** En bil er en sammensat turtle-form inden for opgavens
  fodaftryk på 40 x 20 pixel. Der registreres én form pr. farve, så der ikke
  skal bruges billedfiler.
- **Kan testes uden vindue.** Geometrien (`car_components`), kollisionstesten og
  reglen for oprettelse er almindelig kode. `CarManager` får en bilfabrik og en
  tilfældighedskilde, så testene bruger en falsk bil og en fastlagt terning.
- **Kollision bruger hele bilen.** Spilleren sammenlignes med bilens rektangel,
  ikke kun dens midte.

## Dokumentation

Kommentarerne i kilden er Doxygen-kommentarer. Byg dem med `doxygen Doxyfile`.
Plan- og reviewdokumenter ligger i `docs/`.

Tilbage til [Forside](Home-da).
