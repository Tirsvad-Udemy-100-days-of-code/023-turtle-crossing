# MIL-007 README and wiki

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-007 |
| CrossReference | [BC-001], [PP-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [93d8321] |

---

## Purpose

Decide that S02 can run and understand the project.

## Deliverable

Final README and wiki pages in English, Danish and Bahasa Malaysia.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | README run and test instructions work on a clean clone | S01 follows them | A step fails |
| 2 | Every wiki page exists in en, da and ms | File listing | A language is missing |
| 3 | Doxygen builds without warnings | doxygen Doxyfile output | Warnings present |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-006 | The previous step of the assignment must be accepted first |

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

2026-10-26 - within the two-week plan of [PP-001].

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Final README pass | Check every section against the real commands; fill Continuous integration, Build the source documentation, Project layout and License. | No |  |
| 2 | Write the wiki in three languages | Home, Install and Play, Architecture and Contributing pages in en, da and ms, laid out like the TirSystem github-action wiki, with -da and -ms file suffixes. | No |  |
| 3 | Build the source documentation | Run doxygen and fix warnings so the Doxyfile is known to work. | No |  |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[93d8321]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/023-turtle-crossing/commit/93d83217622a6c555dca728fe10c83c35f8ac7e2
