# MIL-003 Player

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001], [PP-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [93d8321] |

---

## Purpose

Decide that the player turtle works and is covered by tests.

## Deliverable

A Player class that starts at STARTING_POSITION facing north and moves forward on the Up key.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Player starts at (0, -280) facing north | Test asserts position and heading | Wrong start |
| 2 | go_up moves by MOVE_DISTANCE and never back, left or right | Test asserts y only increases | Other movement possible |
| 3 | Up key is bound to go_up | Manual play-through | Key does not move the turtle |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-002 | The previous step of the assignment must be accepted first |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 1 (step 2, bullet 1) | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-17 - within the two-week plan of [PP-001].

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Implement Player class | Subclass of Turtle with turtle shape, penup, start position and heading north, as in the assignment. | No |  |
| 2 | Implement go_up and key binding | go_up moves forward by MOVE_DISTANCE; main.py listens for Up with screen.onkey. | No |  |
| 3 | Test Player | Pytest tests for start state and go_up that run without opening a window. | No |  |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[93d8321]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/023-turtle-crossing/commit/93d83217622a6c555dca728fe10c83c35f8ac7e2
