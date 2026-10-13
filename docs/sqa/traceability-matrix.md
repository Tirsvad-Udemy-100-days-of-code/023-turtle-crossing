# Traceability Matrix

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [93d8321] |

---

## Purpose

Tracks backward/forward links between artifact instances so that the Business Case's
cross-artifact traceability success criterion is measurable. A row is added or
updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | Business Case | en | it | - | [SA-001], [PP-001] | [RC-001] |
| [SA-001] | Stakeholder Analysis | en | it | [BC-001] | [PP-001] | [RC-002] |
| [PP-001] | Project Plan | en | it | [BC-001], [SA-001] | [MIL-001] to [MIL-008] | - (accepted by S01, no checklist) |
| [MIL-001] | Milestone | en | it | [PP-001] | - | [RC-003] |
| [MIL-002] | Milestone | en | it | [PP-001] | - | [RC-004] |
| [MIL-003] | Milestone | en | it | [PP-001] | - | [RC-005] |
| [MIL-004] | Milestone | en | it | [PP-001] | - | [RC-006] |
| [MIL-005] | Milestone | en | it | [PP-001] | - | [RC-007] |
| [MIL-006] | Milestone | en | it | [PP-001] | - | [RC-008] |
| [MIL-007] | Milestone | en | it | [PP-001] | - | [RC-009] |
| [MIL-008] | Milestone | en | it | [PP-001] | - | [RC-010] |

## Coverage Notes

- `-` in Upstream means foundational, in Downstream that nothing is built on it yet, and in Last Reviewed that no review record exists.
- No use case, domain model or design artifacts exist: the project has no use-case tasks.
- Source code is added from MIL-003 on and reviewed against `qc-programming-python`.

---

## Purpose

Tracks backward/forward links between artifact instances so that the Business Case's
cross-artifact traceability success criterion is measurable. A row is added or
updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [<ID>] | <type> | <Language row, or - for a technical type> | <Domain row, or -> | [<upstream-ID>] | [<downstream-ID>] | [<RC-ID>] |
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[MIL-001]: ../milestones/mil-001-baseline-docs.md
[MIL-002]: ../milestones/mil-002-scaffold.md
[MIL-003]: ../milestones/mil-003-player.md
[MIL-004]: ../milestones/mil-004-cars.md
[MIL-005]: ../milestones/mil-005-collision-levelup.md
[MIL-006]: ../milestones/mil-006-scoreboard.md
[MIL-007]: ../milestones/mil-007-readme-wiki.md
[MIL-008]: ../milestones/mil-008-repo-metadata.md
[RC-001]: ./reviews/rc-001-business-case.md
[RC-002]: ./reviews/rc-002-stakeholder-analysis.md
[RC-003]: ./reviews/rc-003-mil-001.md
[RC-004]: ./reviews/rc-004-mil-002.md
[RC-005]: ./reviews/rc-005-mil-003.md
[RC-006]: ./reviews/rc-006-mil-004.md
[RC-007]: ./reviews/rc-007-mil-005.md
[RC-008]: ./reviews/rc-008-mil-006.md
[RC-009]: ./reviews/rc-009-mil-007.md
[RC-010]: ./reviews/rc-010-mil-008.md
[93d8321]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/023-turtle-crossing/commit/93d83217622a6c555dca728fe10c83c35f8ac7e2
