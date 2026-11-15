# Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001], [PP-001], [MIL-009] |
| Language | en |
| Domain | education |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [93d8321] |
| 2026-11-15 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added objective 6, success criterion 8, a scope item, a risk, an assumption and a constraint exception for the baseline milestone MIL-009; set the domain to education; reviewed in autonomous mode, not independent | pending |

---

## Executive Summary

Day 23 of Udemy's "100 Days of Code: The Complete Python Pro Bootcamp" is the
second capstone: a Turtle Crossing game in the style of Crossy Road. The player
steers a turtle north across a multi-lane road of randomly generated cars; each
crossing raises the level and the car speed, and a collision ends the game.
This project delivers the game as a small, readable, tested Python repository
with no runtime dependencies, so that course participants can run and compare
it and GitHub visitors can browse it for ideas. A later milestone, [MIL-009], brings the finished project to the baseline of the framework.

## Methodological and Standards Foundation

- Object-oriented design with one class per concern (`Player`, `CarManager`,
  `Scoreboard`), using the assignment's names.
- Quality characteristics follow ISO/IEC 25010:2023, as the QC checklists of
  the SQA framework tag them.
- Source is documented with Doxygen comments and built with a `Doxyfile`.
- Work follows the software quality assurance (SQA) and quality control (QC) framework mounted at `framework/`: plan first,
  review each artifact, one pull request per milestone.

## Problem Statement

The course supplies four stub files and a video walkthrough, but no
repository that a participant can clone, run, test and read. Solutions shared
between coursists are single files without tests, run instructions or a
statement of the Python version they need, and cars are drawn as plain colour
blocks.

## Business Opportunity

A well-structured reference solution gives S02 a runnable comparison point and
gives S03 a clear example of a small Python project with tests, continuous integration (CI),
documentation and a multilingual wiki, at no dependency cost.

## Objectives

1. Deliver the game behaviour of the Day 23 assignment at Normal difficulty
   (all steps): forward-only turtle, random cars moving left, level-up with
   speed increase, collision stop, scoreboard and GAME OVER.
2. Draw each car so it reads as a car (body, cabin, wheels), not a colour
   block, while keeping the 20 x 40 px footprint the assignment specifies.
3. Provide `src/`, `tests/` and `docs/` with pytest tests for the game logic
   and no runtime dependencies beyond the Python standard library.
4. Provide a README from the agreed template, a local `.venv` guide, a
   `Doxyfile`, CI and a wiki in English, Danish and Bahasa Malaysia.
5. Publish the repository with a description and topics.
6. Bring the finished project to the common baseline of the framework: the adopted framework release, the wiki in the framework's location `docs/wiki/`, the README in the framework template, complete licence metadata and review records for every document ([MIL-009]).

## Scope

### In Scope

- Player, car manager and scoreboard classes, `constants.py`, `main.py`.
- Car appearance drawn with the standard `turtle` module only.
- Unit tests for the logic that does not need a display.
- `pyproject.toml` (Python 3.13 or newer), Python `.gitignore`, Doxygen
  comments and `Doxyfile`.
- README, CI workflow, wiki pages in `en`, `da` and `ms`.
- Repository description and topics on the git host.
- The baseline milestone [MIL-009]: framework release, wiki moved to `docs/wiki/`, README in the framework template, licence metadata, review records and the shared continuous integration (CI) lint rules. It changes no behaviour of the game.

### Out of Scope

- Sound, images, sprite files or any third-party package at runtime.
- Menus, difficulty selection, high-score persistence, networking.
- Packaging for PyPI.
- Re-implementing the Hard and Expert course variants.
- Any change to `src/` or `tests/` in the baseline milestone [MIL-009].

## Expected Benefits

### Tangible Benefits

- A cloneable repository that runs with one command after the venv is set up.
- A passing automated test suite and a CI run on every pull request.
- Generated source documentation for the three classes.

### Intangible Benefits

- A readable example S02 can compare their own solution against.
- A documented course portfolio item for S01 with a visible review trail.

## Strategic Alignment

This is one project in the 100 Days of Code portfolio. It demonstrates the
same planning, review and pull-request discipline across the whole series.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Game plays as the assignment describes | All five Step 2 behaviours work | Manual play-through checklist in the final milestone |
| 2 | Cars look like cars | Each car shows a body, cabin and two wheels, 40 x 20 px | Visual check in the Cars milestone |
| 3 | Tests pass | 100 % of tests pass on Python 3.13 | `pytest` exit code 0 locally and in CI |
| 4 | No runtime dependencies | Zero entries under `dependencies` | `pyproject.toml` inspection |
| 5 | Run instructions work | A fresh clone runs following the README on Windows, Linux and macOS sections | S01 follows the README on a clean clone |
| 6 | Wiki in three languages | Every wiki page exists in `en`, `da`, `ms` | File listing of the wiki |
| 7 | Repository metadata | Description and at least 5 topics set | Repository page |
| 8 | The baseline milestone is done (objective 6) | Wiki pages in 3 languages in `docs/wiki/`, `framework/scripts/check-readme.sh` exits with code 0, 100 % of the CI checks of the pull request of [MIL-009] pass | Files in `docs/wiki/`, the script exit code and the pull request status on the git host |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Turtle needs a display, so CI and tests cannot open a window | Tests cannot cover rendering | Keep game logic free of the screen where possible; test it against a stub; verify rendering manually |
| Custom car shape renders differently across platforms | Cars look wrong for some viewers | Use `turtle.register_shape` with polygons only; check on Windows first and note limits in the README |
| Python 3.13 tkinter missing on some Linux installs | Participants cannot run the game | Document `python3-tk` in the Linux Debian section |
| Tokens in `.env` end up in the repository | Credential leak | `.env` in `.gitignore` before the first commit that adds files; the file is never read by project code |
| Scope creep from "nice to have" features | Delay | Out of Scope list; changes need a Business Case amendment |
| The documents of the baseline milestone [MIL-009] are reviewed by an AI stand-in for S01 | A defect is missed because the review is not independent | Every review record of the baseline says `Mode: autonomous, not independent`, and the end-of-run summary lists it for challenge |

## Assumptions

- S01 is Product Owner, developer and reviewer; reviews are not independent
  (supervised mode).
- The idea is a hunch, not validated by behaviour, and is cheap to build, so no
  riskiest-assumption test is run.
- S01 can reach S02 and S03 through the git host and the course forum.
- The git host `git.tirsystem.com` is available for the repository and wiki.
- S01 stated no deadline; the plan assumes two weeks (see PP-001 Open Issues).
- The baseline milestone [MIL-009] is finished within one week of its own start, 2026-11-15, by 2026-11-22. For that milestone only, an AI stand-in for S01 reviews and accepts the changed documents.

## Constraints

- Python 3.13 or newer, a local `.venv`, pytest for tests.
- Constants live in `constants.py`; configuration lives in `pyproject.toml`.
- Layout is `src/`, `tests/` and `docs/`.
- Only the standard library at runtime.
- The baseline milestone [MIL-009] is the exception to the rule of one reviewer: S01 has authorised the assistant to commit, push, open the pull request and merge it in autonomous mode.

## Cost–Benefit Assessment

Qualitative: the project is a learning exercise with no budget.

| Costs | Benefits |
| --- | --- |
| S01's time: about two weeks of evening work | Portfolio item, a reusable project template, a shareable solution |
| Review effort (S01 reviews own work) | Documented planning and review trail |

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Product Owner, developer and reviewer; wants a finished, well-planned portfolio piece |
| S02 | Udemy coursists; want readable, runnable code with the assignment's names and run instructions |
| S03 | GitHub viewers; want a clear description, topics and README, and no runtime dependencies |

## Recommendation

Proceed — the scope is small, cheap and fully specified by the course, and it
serves all three stakeholders.

---

[SA-001]: ./stakeholder-analysis.md
[PP-001]: ./project-plan.md
[93d8321]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/023-turtle-crossing/commit/93d83217622a6c555dca728fe10c83c35f8ac7e2
[MIL-009]: ./milestones/mil-009-framework-baseline.md
