# Traceability Matrix

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001], [SA-001], [PP-001], [MIL-009] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [93d8321] |
| 2026-11-15 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added the baseline milestone, the wiki and the source code rows, the new review records, the concern coverage and the domain education; removed the template remainder after the document; reviewed in autonomous mode, not independent | [99f5f81] |

---

## Purpose

Tracks backward/forward links between artifact instances so that the Business Case's
cross-artifact traceability success criterion is measurable. A row is added or
updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | Business Case | en | education | - | [SA-001], [PP-001], [MIL-009] | [RC-017] (Go, re-review of the whole document), [RC-001] (Go, the first review) |
| [SA-001] | Stakeholder Analysis | en | education | [BC-001] | [PP-001], [MIL-009] | [RC-018] (Go, re-review of the whole document), [RC-002] (Go, the first review) |
| [PP-001] | Project Plan | en | education | [BC-001], [SA-001] | [MIL-001] to [MIL-009] | [RC-019] (Go, review of the whole document; the plan had no review record before) |
| [MIL-001] | Milestone | en | education | [PP-001] | - | [RC-020] (Go, re-review after the metadata change), [RC-003] (Go, the first review) |
| [MIL-002] | Milestone | en | education | [PP-001] | - | [RC-021] (Go, re-review after the metadata change), [RC-004] (Go, the first review) |
| [MIL-003] | Milestone | en | education | [PP-001] | - | [RC-022] (Go, re-review after the metadata change), [RC-005] (Go, the first review) |
| [MIL-004] | Milestone | en | education | [PP-001] | - | [RC-023] (Go, re-review after the metadata change), [RC-006] (Go, the first review) |
| [MIL-005] | Milestone | en | education | [PP-001] | - | [RC-024] (Go, re-review after the metadata change), [RC-007] (Go, the first review) |
| [MIL-006] | Milestone | en | education | [PP-001] | - | [RC-025] (Go, re-review after the metadata change), [RC-008] (Go, the first review) |
| [MIL-007] | Milestone | en | education | [PP-001] | - | [RC-026] (Go, re-review after the metadata change), [RC-009] (Go, the first review) |
| [MIL-008] | Milestone | en | education | [PP-001] | - | [RC-027] (Go, re-review after the metadata change), [RC-010] (Go, the first review) |
| [MIL-009] | Milestone | en | education | [BC-001], [PP-001], [MIL-008] | - | [RC-028] (Go) |
| Wiki | Wiki | en, da, ms | education | [BC-001] | - | [RC-029] (Go-with-conditions) |
| Python code (`src/`, `tests/`) | Python Source Code (PY) | - | - | [MIL-002], [MIL-003], [MIL-004], [MIL-005], [MIL-006] | - | [RC-011], [RC-012], [RC-013], [RC-014], [RC-015], [RC-016] |

## Concern Coverage

| Concern (CN-ID) | Views that answer it | Decisions (ADR) | Quality check (TP) | Status |
| --- | --- | --- | --- | --- |
| CN-001 | [MIL-003], [MIL-004], [MIL-005], [MIL-006] | - | - | Covered |
| CN-002 | [MIL-001], [MIL-009] | - | - | Covered |
| CN-003 | [MIL-003], [MIL-004], [MIL-005] | - | - | Covered |
| CN-004 | [MIL-002], [MIL-007] | - | - | Covered |
| CN-005 | [MIL-004] | - | - | Covered |
| CN-006 | [MIL-007], [MIL-008] | - | - | Covered |
| CN-007 | [MIL-002] | - | - | Covered |
| CN-008 | [MIL-009] | - | - | Covered |

## Coverage Notes

- `-` in Upstream means foundational, in Downstream that nothing is built on it yet, and in Last Reviewed that no review record exists.
- No use case, domain model or design artifacts exist: the project has no use-case tasks.
- Source code is added from MIL-003 on and reviewed against `qc-programming-python`.
- The domain of every artifact is `education` since [MIL-009]; the earlier review records state the former domain `it` as it was at the time.
- The review records and this matrix have no QC checklist for themselves and are not reviewed.

---

[BC-001]: ../business-case.md
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
[MIL-009]: ../milestones/mil-009-framework-baseline.md
[RC-011]: ./reviews/rc-011-mil-002-code.md
[RC-012]: ./reviews/rc-012-mil-003-code.md
[RC-013]: ./reviews/rc-013-mil-004-code.md
[RC-014]: ./reviews/rc-014-mil-005-code.md
[RC-015]: ./reviews/rc-015-mil-006-code.md
[RC-016]: ./reviews/rc-016-mil-004-code.md
[RC-017]: ./reviews/rc-017-business-case-baseline.md
[RC-018]: ./reviews/rc-018-stakeholder-analysis-baseline.md
[RC-019]: ./reviews/rc-019-project-plan-baseline.md
[RC-020]: ./reviews/rc-020-milestone-001-baseline.md
[RC-021]: ./reviews/rc-021-milestone-002-baseline.md
[RC-022]: ./reviews/rc-022-milestone-003-baseline.md
[RC-023]: ./reviews/rc-023-milestone-004-baseline.md
[RC-024]: ./reviews/rc-024-milestone-005-baseline.md
[RC-025]: ./reviews/rc-025-milestone-006-baseline.md
[RC-026]: ./reviews/rc-026-milestone-007-baseline.md
[RC-027]: ./reviews/rc-027-milestone-008-baseline.md
[RC-028]: ./reviews/rc-028-milestone-009.md
[RC-029]: ./reviews/rc-029-wiki.md
[99f5f81]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/023-turtle-crossing/commit/99f5f819127f7d77ea0b6b9fe782e14766de5395
