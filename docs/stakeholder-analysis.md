# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001], [MIL-009] |
| Language | en |
| Domain | education |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [93d8321] |
| 2026-11-15 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added concern IDs CN-001 to CN-007 (QC-SA-001 criterion 9), the baseline concern CN-008, the baseline milestone in the communication table and a conflict about the stand-in reviewer; set the domain to education; reviewed in autonomous mode, not independent | [99f5f81] |

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

| Concern ID | Stakeholder | Concern | FURPS+ attribute |
| --- | --- | --- | --- |
| CN-001 | S01 | Game behaves as the assignment specifies | Functionality |
| CN-002 | S01 | Review trail and plan before code | Supportability (process) |
| CN-003 | S02 | Assignment names kept (`Player`, `CarManager`, `Scoreboard`, `go_up`, `is_at_finish_line`, `go_to_start`, `level_up`, `create_cars`, `move_cars`) | Functionality, Usability |
| CN-004 | S02 | README steps work on their OS | Usability |
| CN-005 | S02 | Cars look like cars | Usability |
| CN-006 | S03 | Description, topics, README in plain language | Usability |
| CN-007 | S03 | No runtime dependencies | Supportability, Implementation constraint |
| CN-008 | S01 | The project follows the common baseline of the framework, with the wiki in the framework's location | Supportability |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| S01 | Chat and pull request review | Per milestone | Review record and pull request | All gateways |
| S02 | README, wiki (en, da, ms) | Once per release | Run instructions, wiki pages | MIL-007 |
| S03 | Repository description, topics, README | Once | Repository metadata | MIL-008 |
| S01 | Pull request on the git host and end-of-run summary in chat | Once, for the baseline milestone | Documents, wiki and review records to read, and the stand-in decisions | [MIL-009] |
| S02, S03 | Wiki in English, Danish and Malay | Once, updated on change | Wiki pages | [MIL-009] |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| S02 wants the assignment's simple structure; good project hygiene (constants, tests, docs) adds files | S02, S01 | Keep the assignment's class and method names; put extras in `constants.py`, `tests/` and `docs/` only |
| S03 wants zero dependencies; Doxygen and pytest are tools | S03, S01 | pytest is a dev-only dependency in `pyproject.toml` optional group; runtime has none |
| The documents of the baseline milestone are accepted by an AI stand-in for S01, so that review is not independent | S01 | S01 authorised the stand-in for the baseline milestone only; every review record says `Mode: autonomous, not independent`, and the end-of-run summary lists each stand-in decision so that S01 can challenge it |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | Correct game (CN-001) | [BC-001] Objective 1 |
| S02 | Readable, runnable code (CN-003, CN-004) | [BC-001] Objectives 1, 3, 4 |
| S02 | Cars look like cars (CN-005) | [BC-001] Objective 2 |
| S03 | Clear repository, no dependencies (CN-006, CN-007) | [BC-001] Objectives 3, 5 |
| S01 | Review trail and plan before code (CN-002); the project follows the common baseline of the framework (CN-008) | [BC-001] Objective 6 |

## Sign-Off

| Stakeholder | Date | Decision |
| --- | --- | --- |
| S01 | [93d8321] | Proposed |

The changes of the baseline milestone were accepted by the AI stand-in for S01 after the review record of this document (Go), autonomous, not independent.

---

[BC-001]: ./business-case.md
[93d8321]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/023-turtle-crossing/commit/93d83217622a6c555dca728fe10c83c35f8ac7e2
[MIL-009]: ./milestones/mil-009-framework-baseline.md
[99f5f81]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/023-turtle-crossing/commit/99f5f819127f7d77ea0b6b9fe782e14766de5395
