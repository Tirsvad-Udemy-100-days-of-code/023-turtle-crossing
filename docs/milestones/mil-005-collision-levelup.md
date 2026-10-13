# MIL-005 Collision and level up

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-005 |
| CrossReference | [BC-001], [PP-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Purpose

Decide that collisions end the game and finishing a crossing raises difficulty.

## Deliverable

Collision detection, is_at_finish_line, go_to_start and level_up working together in the game loop.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Game stops when the player touches a car's footprint | Test and manual play | Game continues after a hit |
| 2 | is_at_finish_line is true when y exceeds FINISH_LINE_Y | Test | Wrong result |
| 3 | Reaching the finish line returns the player to start and raises car speed by MOVE_INCREMENT | Test | Speed or position unchanged |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-004 | The previous step of the assignment must be accepted first |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 1 (step 2, bullets 3 and 4) | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-21 - within the two-week plan of [PP-001].

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Implement collision detection | Compare the player with each car using a hit area derived from the 20 px car height and 40 px width, so the whole car body counts and not only its centre. | No |  |
| 2 | Implement finish line and go_to_start | Player.is_at_finish_line and Player.go_to_start per the assignment. | No |  |
| 3 | Implement level_up | CarManager.level_up adds MOVE_INCREMENT to the move distance. | No |  |
| 4 | Test collision and level up | Pytest tests for collision, finish line and speed increase. | No |  |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
