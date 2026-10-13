# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Purpose

Identify who is affected by the Turtle Crossing project, who decides and who
reviews, using the power/interest grid. S01 is both author and reviewer; this
is a known, accepted exception for a single-person course project, recorded in
every review as "not independent".

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant; Product Owner, developer, reviewer | TirSystem | HIGH | HIGH | Manage Closely | A finished, correct game with a clear review trail |
| S02 | Udemy coursists | Fellow participants of the bootcamp | Udemy community | LOW | HIGH | Keep Informed | Readable, runnable code with the assignment's function names and README run instructions |
| S03 | GitHub viewers | Visitors browsing for ideas | Public | LOW | MEDIUM | Keep Informed | A clear repository description, topics and README, and no runtime dependencies |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** decides scope, reviews and accepts every artifact,
  and does all the work.
- **Keep Informed (S02, S03):** cannot change the project, but their use of it
  is its purpose. S02 has higher interest because they compare solutions; S03
  is a casual audience.

## Primary Concerns and FURPS+ Mapping

FURPS+ is the quality model with Functionality, Usability, Reliability, Performance and Supportability, plus design, implementation, interface and physical constraints.

| ID | Concern | FURPS+ attribute |
| --- | --- | --- |
| S01 | Game behaves as the assignment specifies | Functionality |
| S01 | Review trail and plan before code | Supportability (process) |
| S02 | Assignment names kept (`Player`, `CarManager`, `Scoreboard`, `go_up`, `is_at_finish_line`, `go_to_start`, `level_up`, `create_cars`, `move_cars`) | Functionality, Usability |
| S02 | README steps work on their OS | Usability |
| S02 | Cars look like cars | Usability |
| S03 | Description, topics, README in plain language | Usability |
| S03 | No runtime dependencies | Supportability, Implementation constraint |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| S01 | Chat and pull request review | Per milestone | Review record and pull request | All gateways |
| S02 | README, wiki (en, da, ms) | Once per release | Run instructions, wiki pages | MIL-007 |
| S03 | Repository description, topics, README | Once | Repository metadata | MIL-008 |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| S02 wants the assignment's simple structure; good project hygiene (constants, tests, docs) adds files | S02, S01 | Keep the assignment's class and method names; put extras in `constants.py`, `tests/` and `docs/` only |
| S03 wants zero dependencies; Doxygen and pytest are tools | S03, S01 | pytest is a dev-only dependency in `pyproject.toml` optional group; runtime has none |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | Correct game | [BC-001] Objective 1 |
| S02 | Readable, runnable code | [BC-001] Objectives 1, 3, 4 |
| S02 | Cars look like cars | [BC-001] Objective 2 |
| S03 | Clear repository, no dependencies | [BC-001] Objectives 3, 5 |

## Sign-Off

| Stakeholder | Date | Decision |
| --- | --- | --- |
| S01 | pending | Proposed |

---

[BC-001]: ./business-case.md
