# MIL-001 Baseline documents

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001], [PP-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [93d8321] |

---

## Purpose

Decide whether the planning baseline is complete so that code may start.

## Deliverable

Accepted Business Case, Stakeholder Analysis, Project Plan and milestone documents, each with a Go review record.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | BC, SA and PP are Accepted | Each Version History row is Accepted | Any is Proposed or No-Go |
| 2 | Every milestone has a Go review | A review record (RC) exists with verdict Go | A milestone has no review |

## Dependencies

| Depends on | Reason |
| --- | --- |
| None | First milestone |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 1-5 (planning basis) | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-14 - within the two-week plan of [PP-001].

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Review baseline documents | Review BC-001, SA-001 and PP-001 against their checklists, write the review records (RC) and set rows to Accepted. This is the gate for everything under src/ and tests/. | No |  |
| 2 | Review milestone documents | Review MIL-001 to MIL-008 against qc-milestones-gateways and write the review records (RC). | No |  |
| 3 | Install git hooks and plan gate | Run install-git-hooks.sh with --enable-plan-gate so commits touching src/ or tests/ need a Task trailer. | No |  |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[93d8321]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/023-turtle-crossing/commit/93d83217622a6c555dca728fe10c83c35f8ac7e2
