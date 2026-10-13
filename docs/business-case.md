# Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001], [PP-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [93d8321] |

---

## Executive Summary

Day 23 of Udemy's "100 Days of Code: The Complete Python Pro Bootcamp" is the
second capstone: a Turtle Crossing game in the style of Crossy Road. The player
steers a turtle north across a multi-lane road of randomly generated cars; each
crossing raises the level and the car speed, and a collision ends the game.
This project delivers the game as a small, readable, tested Python repository
with no runtime dependencies, so that course participants can run and compare
it and GitHub visitors can browse it for ideas.

## Methodological and Standards Foundation

- Object-oriented design with one class per concern (`Player`, `CarManager`,
  `Scoreboard`), using the assignment's names.
- Quality characteristics follow ISO/IEC 25010:2023, as the QC checklists of
  the SQA framework tag them.
- Source is documented with Doxygen comments and built with a `Doxyfile`.
- Work follows the software quality assurance (SQA) and quality control (QC) framework mounted at `framework/`: plan first,
  review each artifact, one pull request per milestone.

## Problem Statement

The course supplies four stub files and a video walkthrough, but no
repository that a participant can clone, run, test and read. Solutions shared
between coursists are single files without tests, run instructions or a
statement of the Python version they need, and cars are drawn as plain colour
blocks.

## Business Opportunity

A well-structured reference solution gives S02 a runnable comparison point and
gives S03 a clear example of a small Python project with tests, continuous integration (CI),
documentation and a multilingual wiki, at no dependency cost.

## Objectives

1. Deliver the game behaviour of the Day 23 assignment at Normal difficulty
   (all steps): forward-only turtle, random cars moving left, level-up with
   speed increase, collision stop, scoreboard and GAME OVER.
2. Draw each car so it reads as a car (body, cabin, wheels), not a colour
   block, while keeping the 20 x 40 px footprint the assignment specifies.
3. Provide `src/`, `tests/` and `docs/` with pytest tests for the game logic
   and no runtime dependencies beyond the Python standard library.
4. Provide a README from the agreed template, a local `.venv` guide, a
   `Doxyfile`, CI and a wiki in English, Danish and Bahasa Malaysia.
5. Publish the repository with a description and topics.

## Scope

### In Scope

- Player, car manager and scoreboard classes, `constants.py`, `main.py`.
- Car appearance drawn with the standard `turtle` module only.
- Unit tests for the logic that does not need a display.
- `pyproject.toml` (Python 3.13 or newer), Python `.gitignore`, Doxygen
  comments and `Doxyfile`.
- README, CI workflow, wiki pages in `en`, `da` and `ms`.
- Repository description and topics on the git host.

### Out of Scope

- Sound, images, sprite files or any third-party package at runtime.
- Menus, difficulty selection, high-score persistence, networking.
- Packaging for PyPI.
- Re-implementing the Hard and Expert course variants.

## Expected Benefits

### Tangible Benefits

- A cloneable repository that runs with one command after the venv is set up.
- A passing automated test suite and a CI run on every pull request.
- Generated source documentation for the three classes.

### Intangible Benefits

- A readable example S02 can compare their own solution against.
- A documented course portfolio item for S01 with a visible review trail.

## Strategic Alignment

This is one project in the 100 Days of Code portfolio. It demonstrates the
same planning, review and pull-request discipline across the whole series.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Game plays as the assignment describes | All five Step 2 behaviours work | Manual play-through checklist in the final milestone |
| 2 | Cars look like cars | Each car shows a body, cabin and two wheels, 40 x 20 px | Visual check in the Cars milestone |
| 3 | Tests pass | 100 % of tests pass on Python 3.13 | `pytest` exit code 0 locally and in CI |
| 4 | No runtime dependencies | Zero entries under `dependencies` | `pyproject.toml` inspection |
| 5 | Run instructions work | A fresh clone runs following the README on Windows, Linux and macOS sections | S01 follows the README on a clean clone |
| 6 | Wiki in three languages | Every wiki page exists in `en`, `da`, `ms` | File listing of the wiki |
| 7 | Repository metadata | Description and at least 5 topics set | Repository page |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Turtle needs a display, so CI and tests cannot open a window | Tests cannot cover rendering | Keep game logic free of the screen where possible; test it against a stub; verify rendering manually |
| Custom car shape renders differently across platforms | Cars look wrong for some viewers | Use `turtle.register_shape` with polygons only; check on Windows first and note limits in the README |
| Python 3.13 tkinter missing on some Linux installs | Participants cannot run the game | Document `python3-tk` in the Linux Debian section |
| Tokens in `.env` end up in the repository | Credential leak | `.env` in `.gitignore` before the first commit that adds files; the file is never read by project code |
| Scope creep from "nice to have" features | Delay | Out of Scope list; changes need a Business Case amendment |

## Assumptions

- S01 is Product Owner, developer and reviewer; reviews are not independent
  (supervised mode).
- The idea is a hunch, not validated by behaviour, and is cheap to build, so no
  riskiest-assumption test is run.
- S01 can reach S02 and S03 through the git host and the course forum.
- The git host `git.tirsystem.com` is available for the repository and wiki.
- S01 stated no deadline; the plan assumes two weeks (see PP-001 Open Issues).

## Constraints

- Python 3.13 or newer, a local `.venv`, pytest for tests.
- Constants live in `constants.py`; configuration lives in `pyproject.toml`.
- Layout is `src/`, `tests/` and `docs/`.
- Only the standard library at runtime.

## Cost–Benefit Assessment

Qualitative: the project is a learning exercise with no budget.

| Costs | Benefits |
| --- | --- |
| S01's time: about two weeks of evening work | Portfolio item, a reusable project template, a shareable solution |
| Review effort (S01 reviews own work) | Documented planning and review trail |

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Product Owner, developer and reviewer; wants a finished, well-planned portfolio piece |
| S02 | Udemy coursists; want readable, runnable code with the assignment's names and run instructions |
| S03 | GitHub viewers; want a clear description, topics and README, and no runtime dependencies |

## Recommendation

Proceed — the scope is small, cheap and fully specified by the course, and it
serves all three stakeholders.

---

[SA-001]: ./stakeholder-analysis.md
[PP-001]: ./project-plan.md
[93d8321]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/023-turtle-crossing/commit/93d83217622a6c555dca728fe10c83c35f8ac7e2
