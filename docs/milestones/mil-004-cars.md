# MIL-004 Cars

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001], [PP-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Purpose

Decide that cars are generated, drawn as cars and moved correctly.

## Deliverable

A CarManager with create_cars and move_cars, and a registered car shape that shows a body, cabin and two wheels inside a 40 x 20 px footprint.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Cars are generated at random y values, never in the top or bottom 50 px | Test over many samples | A car appears in the safe zone |
| 2 | A new car is created on one in six loop runs | Test of the spawn rule | Wrong rate |
| 3 | Cars move right to left by the current speed | Test of position change | Wrong direction |
| 4 | Each car is drawn as a car, not a colour block, using the standard library only | Visual check and shape registration in code | A plain rectangle is shown or an image file is needed |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-003 | The previous step of the assignment must be accepted first |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 1, 2 (step 2, bullet 2) | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-19 - within the two-week plan of [PP-001].

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Design the car shape | Draw a car silhouette as a compound turtle Shape: lower body, cabin with window, two wheels, 40 x 20 px, pointing left. Register it once with register_shape. The colour comes from COLORS. | No |  |
| 2 | Implement create_cars | Random colour and random y inside the safe-zone limits, one car in six loop runs, each car using the registered shape. | No |  |
| 3 | Implement move_cars | Move every car left by the current speed and drop cars that left the screen. | No |  |
| 4 | Test CarManager | Pytest tests for spawn rule, safe zone and movement, with the display parts separated from the logic. | No |  |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
