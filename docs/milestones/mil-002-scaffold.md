# MIL-002 Project scaffold

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001], [PP-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Purpose

Decide that the repository skeleton, tooling and environment documentation are ready for game code.

## Deliverable

A repository with src/, tests/, docs/, pyproject.toml, .gitignore (including .env), constants.py, Doxyfile, a continuous integration (CI) workflow and a README that documents the local .venv set up.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | pyproject.toml requires Python 3.13 or newer and has no runtime dependencies | File inspected | A dependency is listed or an older Python is allowed |
| 2 | .gitignore covers .venv, caches and .env | git status shows .env ignored | A secret file would be tracked |
| 3 | pytest runs green on a smoke test | pytest exit code 0 | pytest fails |
| 4 | README follows the agreed template and documents the venv and python -m pip install --upgrade pip | Headings match the template | A heading or instruction is missing |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-001 | The previous step of the assignment must be accepted first |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 3, 4 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-15 - within the two-week plan of [PP-001].

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Create pyproject.toml and .gitignore | Python >=3.13, src layout, pytest as an optional dev dependency, no runtime dependencies. Python .gitignore that also ignores .env. | No |  |
| 2 | Move starter code into src/ and create constants.py | Place main, player, car_manager and scoreboard under src/ and move every constant, including the screen size and loop delay, into constants.py. | No |  |
| 3 | Add Doxyfile and Doxygen comment style | Doxyfile that reads src/ and writes to docs/api; document the comment convention used in source. | No |  |
| 4 | Write README from the template | Fill every template heading with real instructions for Windows PowerShell, Linux Debian and macOS, including creating a local .venv. | No |  |
| 5 | Add CI workflow | Gitea Actions workflow that sets up Python 3.13, installs the dev extras and runs pytest, from framework/templates/ci. | No |  |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
