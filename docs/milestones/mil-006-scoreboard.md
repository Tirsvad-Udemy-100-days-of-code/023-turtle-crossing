# MIL-006 Scoreboard and game over

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-006 |
| CrossReference | [BC-001], [PP-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Purpose

Decide that the game is complete in play.

## Deliverable

A Scoreboard showing the level, increasing on each crossing, and GAME OVER displayed in the centre on a collision.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Scoreboard shows the level at top left and it rises per crossing | Test and manual play | Level not shown or not updated |
| 2 | GAME OVER appears at the centre on collision and the window stays open | Manual play | Missing, or the window closes |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-005 | The previous step of the assignment must be accepted first |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 1 (step 2, bullet 5) | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-23 - within the two-week plan of [PP-001].

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Implement Scoreboard | Subclass of Turtle, hidden, writes the level in FONT at the top left; increase_level and update_scoreboard clear and rewrite. | No |  |
| 2 | Implement game_over | Write GAME OVER at the centre and keep the window open with exitonclick. | No |  |
| 3 | Test Scoreboard and full play-through | Pytest tests for level text and a manual checklist of the five Step 2 behaviours. | No |  |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
