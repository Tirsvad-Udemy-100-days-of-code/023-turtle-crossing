# Code review for MIL-004

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-016 |
| CrossReference | [MIL-004], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: [MIL-004]
- Checklist used: [QC-PY-001]
- Scope: full review of the source and tests changed by MIL-004: car_shape.py orientation fix (to_shape_frame) and its tests
- Language and domain: n/a (source code is a technical type)
- Language reviewer: none
- Mode: autonomous, not independent (reviewer is `AI as stand-in for S01`; the author is S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) (Mandatory) | Pass | Names checked against PEP 8: snake_case functions, PascalCase classes, UPPER_SNAKE constants. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes (Mandatory) | Pass | Names state purpose; no single-letter names outside comprehension scopes. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions (Mandatory) | Pass | Formatting follows PEP 8 and 88 columns by hand; no linter is configured in this project (project tooling gap noted, no suppressions). |
| 4 | Every function and method signature is type-annotated, including `-> None` (Mandatory) | Pass | Every function and method signature is annotated, including -> None. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) (Mandatory) | N-A | No exception handling in the changed code. |
| 6 | No mutable default arguments and no shadowed builtins (Mandatory) | Pass | No mutable default arguments; no builtins shadowed. |
| 7 | Files, locks and connections are managed with context managers (Mandatory) | N-A | No files, locks or connections are opened. |
| 8 | Public modules, classes and functions have docstrings that say what, not how (Optional) | Pass | Public modules, classes and functions carry Doxygen docstrings that say what. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output (Mandatory) | N-A | No logging; the game writes only to the turtle window. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded (Mandatory) | N-A | The project has no Design Class Diagram: the tasks are plain tasks (no use case), the classes follow the assignment names. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network (Mandatory) | Pass | The orientation bug was reproduced by a display test that fails without the fix and passes with it. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment (Optional) | N-A | Optional: no type checker is configured. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused (Optional) | Pass | No runtime dependencies; pytest is declared in the dev dependency group. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike (Mandatory) | Pass | Constants are defined once in constants.py and imported. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles (Mandatory) | Pass | Rule modules import nothing from the screen; turtle classes sit at the edge; no import cycles. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations (Mandatory) | Pass | One responsibility per class; the car factory is injected so the logic is tested with a fake. |

## Overall Verdict

Go - every Mandatory criterion of QC-PY-001 passes or is not applicable with a stated reason. The review is not independent: author and reviewer are the same person, with the AI standing in for S01.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Challenge this review in the end-of-run summary if needed | S01 | 2026-10-27 |

---

[MIL-004]: ../../milestones/mil-004-cars.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
