# Qorix Engineering Processes

Sphinx-Needs based repository for ASPICE / ISO 26262 / ISO/SAE 21434 /
ISO 29119 aligned development. See `STANDARDS.md` for the folder-to-standard
crosswalk.

This repo has **two independent Sphinx projects**:

- **Root** (this `conf.py`) — organizational governance (`organisation/governance/`,
  `organisation/verification/`), strategy (`organisation/strategy/`), and project management
  (`management/`, `test/`). Renders `org_req` needs only.
- **`Needs/`** (its own `conf.py`) — the product traceability graph:
  system/feature/component/unit requirements and the safety chain
  (`sg`/`fsr`/`tsr`). Build it separately from inside `Needs/`.

## One organization, one repo, one workspace

Everything — docs, product traceability, governance, and source for five
languages — lives in this single repository, opened in VS Code as a single
workspace root via `qorix-engg.code-workspace` (no multi-root, no separate
repos to juggle).

```
qorix-asr-ap-r20-11_temp/
├── .github/
│   └── workflows/
│       ├── ci-needs.yml
│       ├── ci-source-c.yml
│       ├── ci-source-cpp.yml
│       ├── ci-source-python.yml
│       ├── ci-source-rust.yml
│       ├── ci-source-typescript.yml
│       ├── ci.yml
│       └── docs.yml
├── .vscode/
│   ├── extensions.json
│   ├── settings.json
│   └── tasks.json
├── doc/
│   ├── errata/
│   │   └── .gitkeep
│   ├── manuals/
│   │   └── .gitkeep
│   ├── reference/
│   │   └── .gitkeep
│   ├── release_notes/
│   │   └── v0.1.0.md
│   ├── tutorials/
│   │   └── .gitkeep
│   └── README.md
├── management/
│   ├── change/
│   │   ├── change-register.yml
│   │   └── changes.rst
│   ├── exceptions/   (empty)
│   ├── planning/
│   │   ├── milestones.yml
│   │   └── project-plan.rst
│   ├── problem/
│   │   ├── problem-register.yml
│   │   └── problems.rst
│   └── risk/
│       ├── risk-register.yml
│       └── risks.rst
├── Needs/
│   ├── Communication/
│   │   ├── component/
│   │   │   ├── requirements/
│   │   │   │   └── index.rst
│   │   │   ├── comp_a_001.rst
│   │   │   └── index.rst
│   │   ├── feature/
│   │   │   ├── requirements/
│   │   │   │   └── index.rst
│   │   │   ├── feat_a_001.rst
│   │   │   └── index.rst
│   │   ├── unit design/
│   │   │   └── unit_a_001.rst
│   │   └── index.rst
│   ├── cybersecurity/
│   │   ├── tara/
│   │   │   └── index.rst
│   │   └── index.rst
│   ├── Diagnostics/
│   │   ├── component/
│   │   │   └── comp_z_001.rst
│   │   ├── feature/
│   │   │   └── feat_z_001.rst
│   │   ├── unit design/
│   │   │   └── unit_z_001.rst
│   │   └── index.rst
│   ├── quality/
│   │   ├── metrics/
│   │   │   └── index.rst
│   │   ├── reviews/
│   │   │   └── index.rst
│   │   └── index.rst
│   ├── safety/
│   │   ├── analyses/
│   │   │   ├── dependent-failure-analysis.rst
│   │   │   ├── fmea.rst
│   │   │   └── index.rst
│   │   ├── fsr_001.rst
│   │   ├── index.rst
│   │   ├── sg_001.rst
│   │   └── tsr_001.rst
│   ├── sys/
│   │   ├── index.rst
│   │   └── sys_001.rst
│   ├── business-needs.rst
│   ├── conf.py
│   ├── index.rst
│   ├── operational-needs.rst
│   ├── requirements.txt
│   └── stakeholder-needs.rst
├── organisation/common_framework/
│   ├── core lib/   (empty)
│   └── HAL/   (empty)
├── organisation/governance/
│   ├── aspice/
│   │   ├── index.rst
│   │   └── org_aspice_requirements.rst
│   ├── coding guidelines/
│   │   ├── c/
│   │   │   ├── c_MISRA2017.md
│   │   │   └── README.md
│   │   ├── cpp/
│   │   │   └── README.md
│   │   ├── markdown/
│   │   │   └── README.md
│   │   ├── python/
│   │   │   └── README.md
│   │   └── rust/
│   │       ├── crates/
│   │       │   └── example_crate/
│   │       │       ├── src/
│   │       │       │   └── lib.rs
│   │       │       └── Cargo.toml
│   │       ├── Cargo.toml
│   │       ├── README.md
│   │       └── rustfmt.toml
│   ├── cybersecurity/
│   │   ├── index.rst
│   │   └── org_cybsec_requirements.rst
│   ├── functionalsafety/
│   │   ├── index.rst
│   │   └── org_fusa_requirements.rst
│   ├── policies/
│   │   ├── cybersecurity.rst
│   │   ├── quality.rst
│   │   └── safety.rst
│   └── index.rst
├── organisation/strategy/
│   ├── roadmap.rst
│   └── strategy.rst
├── organisation/tools/
│   ├── index.rst
│   ├── policy.rst
│   └── tool_qualification_requirements.rst
├── organisation/verification/
│   └── iso29119/
│       ├── policy/   (empty)
│       ├── strategy/
│       │   └── product-verification-strategy.rst
│       ├── index.rst
│       └── organizational_requirements.rst
├── source/
│   ├── c/
│   │   ├── include/
│   │   │   ├── communication/
│   │   │   │   └── router.h.c
│   │   │   └── example.h
│   │   ├── src/
│   │   │   ├── communication/
│   │   │   │   └── router.c
│   │   │   └── example.c
│   │   ├── tests/
│   │   │   ├── communication/
│   │   │   │   └── test_router.c
│   │   │   └── CMakeLists.txt
│   │   ├── .clang-format
│   │   ├── CMakeLists.txt
│   │   └── README.md
│   ├── cpp/
│   │   ├── include/
│   │   │   └── example.hpp
│   │   ├── src/
│   │   │   └── example.cpp
│   │   ├── tests/
│   │   │   └── CMakeLists.txt
│   │   ├── .clang-format
│   │   ├── CMakeLists.txt
│   │   └── README.md
│   ├── markdown/
│   │   └── README.md
│   ├── python/
│   │   ├── src/
│   │   │   └── example_package/
│   │   │       └── __init__.py
│   │   ├── tests/
│   │   │   └── test_example.py
│   │   ├── .ruff.toml
│   │   ├── pyproject.toml
│   │   └── README.md
│   ├── rust/
│   │   ├── crates/
│   │   │   └── example_crate/
│   │   │       ├── src/
│   │   │       │   └── lib.rs
│   │   │       └── Cargo.toml
│   │   ├── Cargo.toml
│   │   ├── README.md
│   │   └── rustfmt.toml
│   └── typescript/
│       ├── src/
│       │   └── index.ts
│       ├── test/
│       │   └── index.test.ts
│       ├── eslint.config.js
│       ├── package.json
│       ├── README.md
│       └── tsconfig.json
├── test/
│   ├── executions/
│   │   ├── .gitkeep
│   │   └── exec_build_2026_081.yml
│   ├── testbasis/
│   │   ├── .gitkeep
│   │   └── basis.yml
│   ├── testcases/
│   │   ├── communication/
│   │   │   └── case_a_001.md
│   │   ├── .gitkeep
│   │   └── index.rst
│   ├── testconditions/
│   │   ├── .gitkeep
│   │   └── tcond_startup_001.yml
│   ├── testdesign/
│   │   └── .gitkeep
│   ├── testprocedures/
│   │   ├── .gitkeep
│   │   └── proc_sys_startup_001.yml
│   ├── testreports/
│   │   ├── .gitkeep
│   │   └── product-verification-report.rst
│   ├── teststrategy/
│   │   └── product-verification-strategy.rst
│   ├── testsuites/
│   │   ├── .gitkeep
│   │   └── suite_release_smoke.yml
│   ├── index.rst
│   └── README.md
├── tools/
│   ├── check_orphan_needs.py
│   ├── check_broken_links.py
│   └── orphan_baseline.json
├── .gitignore
├── .pre-commit-config.yaml
├── conf.py
├── getting_started.rst
├── index.rst
├── needs_overview.rst
├── qorix-engg.code-workspace
├── README.md
└── STANDARDS.md
```

`(empty)` marks directories that exist but currently hold no tracked
content — `management/exceptions/`, `organisation/common_framework/core lib/`,
`organisation/common_framework/HAL/`, and `organisation/verification/iso29119/policy/`.
They're scaffolded, not yet filled in.

## Build docs locally

```
pip install sphinx sphinx-needs
sphinx-build -b html . _build/html          # root project
cd Needs && sphinx-build -b html . _build/html   # Needs/ project
```

## Build & test code (per-language, under source/)

Each language under `source/<lang>/` has its own build tooling
(CMake for C/C++, Cargo for Rust, npm/tsc for TypeScript, pytest for
Python) — see `.github/workflows/` for the exact commands run in CI.

## Structure

- `Needs/` — product traceability, grouped by discipline: `software/`
  (`Communication/`, `Diagnostics/` — feature/component/unit design per
  module), `safety/` (safety chain + `analyses/`), `security/`,
  `quality/`, `systemslifecycle/` (system-level, its own discipline) —
  see `Needs/` for details.
- `organisation/governance/` — organization-level requirements per standard
  (ASPICE, ISO 26262, ISO/SAE 21434).
- `organisation/verification/` — ISO 29119 organization-level test-process
  requirements.
- `organisation/tools/` — tool qualification & usage governance (ISO 26262-8
  clause 11, ASPICE SUP.8/SUP.1) — see `organisation/tools/index.rst`.
- `organisation/strategy/`, `organisation/common_framework/` — not yet reviewed as part of
  this documentation pass.
- `source/` — implementation, one folder per language.
- `test/` — test basis, conditions, design, procedures, cases, suites,
  reports, executions.
- `management/` — change, planning, problem, and risk registers.
- `doc/` — published documentation (manuals, tutorials, reference,
  release notes, errata).

## Need ID naming convention

Adopted 2026-08-21, currently applied to the **Communication** module and
to the shared `sys` tier only — see the scope note below before assuming
it holds repo-wide.

Format: `<TYPE>_<MODULE>_<TOPIC>_NNN` (the `sys` tier omits `<MODULE>`,
since a system requirement spans modules by definition).

| Tier | Format | Example |
|---|---|---|
| `sys` | `sys_<topic>_nnn` | `sys_msgdisc_001` |
| `feat` | `feat_<module>_<topic>_nnn` | `feat_com_someip_005` |
| `comp` | `comp_<module>_<topic>_nnn` | `comp_com_sd_001` |
| `unit` | `unit_<module>_<topic>_nnn` | `unit_com_sd_004` |

Segment breakdown for that same chain — `sys` has 3 segments (no module),
the other three tiers have 4:

| ID | Type | Module | Topic | NNN |
|---|---|---|---|---|
| `sys_msgdisc_001` | `sys` | — | `msgdisc` | `001` |
| `feat_com_someip_005` | `feat` | `com` | `someip` | `005` |
| `comp_com_sd_001` | `comp` | `com` | `sd` | `001` |
| `unit_com_sd_004` | `unit` | `com` | `sd` | `004` |

Reading an ID top to bottom tells you what it's about without opening the
file — a real `:satisfies:` chain from this repo, not a hypothetical:

| Tier | ID | Title | Satisfies |
|---|---|---|---|
| `sys` | `sys_msgdisc_001` | Inter-application communication and service discovery | — |
| `feat` | `feat_com_someip_005` | Compatibility with Open SOME/IP Service Discovery Protocol Specification | `sys_msgdisc_001` |
| `comp` | `comp_com_sd_001` | SOME/IP Service Discovery Protocol | `feat_com_someip_005` |
| `unit` | `unit_com_sd_004` | SOME/IP FindService message | `comp_com_sd_001` |

Module codes in use: `com` (Communication). Topic codes are assigned per
tier based on what the need is actually about — they don't have to match
between tiers (a feature can be broader than the component that
implements it, as in the example above: `SOMEIP` at the feat tier,
`SD` at the comp/unit tier, because the component is more specific than
the feature it satisfies).

**Scope, as of this pass — read before citing an ID:**

- Every `feat`/`comp`/`unit` id introduced for the Communication module
  during this pass follows this scheme in full, including the 49
  top-level Communication features, which were grouped into 9 topic
  buckets (`arch`, `ifc`, `safety`, `perf`, `binding`, `vm`, `deploy`,
  `trace`, `acl`) precisely so no id would be left topic-less.
- `SYS_001` was renamed to `sys_msgdisc_001` since it's the one `sys`
  requirement that exists today; every file that referenced it
  (`needs/systemslifecycle/index.rst`, `needs/stakeholder-needs.rst`,
  `needs/index.rst`, `needs/diagnostics/feature/index.rst`,
  `needs/quality/metrics/index.rst`) was updated to match.
- **Diagnostics has not been converted.** `feat_z_001`, `comp_z_001`,
  `unit_z_001` still use the original flat, module-only style with no
  topic code — applying this scheme there is separate, not-yet-done
  work.
- **Three pre-existing Communication ids were deliberately left
  unrenamed**: `feat_a_001`, `comp_a_001`, `UNIT_A_001`. They predate
  this pass and anchor the established ISO 26262 safety chain
  (`sg_001`→`fsr_001`→`tsr_001`→`comp_a_001`→`UNIT_A_001`,
  `itc_comp_a_001_001`) — renumbering them was out of scope. Expect the
  Communication module to mix both styles (3 old-style ids alongside the
  new-style ones) rather than read that as an oversight.
- New Communication needs going forward should follow this scheme
  (assign the real topic the need belongs to — don't leave the topic
  segment out to avoid the choice).

**2026-08-22 addendum:** every ID in this document (and every real ID in
`needs/`) was lowercased repo-wide — see `needs/needs_types_definition.rst`'s
own dated note. `UNIT_A_001` above is left as-is deliberately: it isn't a
naming-scheme exception any more, it's simply retired — it was removed
outright on 2026-08-21 (superseded by `unit_com_evttrig_019`; see
`needs/software/communication/component/unit test/test cases/index.rst`'s
history note) and never re-added, so there's no live ID to lowercase.

## File naming convention

**Rule, adopted 2026-08-22: every `.rst` and `.yml` file name in this repo
is lowercase.** No exceptions for otherwise-uppercase IDs — a file named
after a need or a test artifact ID takes the lowercased form of that ID,
matching the ID casing rule above (e.g. `sys_msgdisc_001` the need, not
just the file). Directory names aren't covered by this rule (existing
ones like `test cases/`, `test basis/` were already lowercase and aren't
otherwise in scope here), but new directories should follow the same
practice unless there's a specific reason not to.

This was a real gap as of 2026-08-22: six `.yml` files had uppercase
names —

- `needs/software/diagnostics/component/unit test/test conditions/TCOND_UNIT_Z_001.yml`
- `needs/software/diagnostics/component/unit test/test procedures/PROC_UNIT_Z_001.yml`
- `testing/test conditions/TCOND_STARTUP_001.yml`
- `testing/test executions/EXEC_BUILD_2026_081.yml`
- `testing/test procedures/PROC_SYS_STARTUP_001.yml`
- `testing/test suites/SUITE_RELEASE_SMOKE.yml`

All six renamed to lowercase (`tcond_unit_z_001.yml`, `proc_unit_z_001.yml`,
`tcond_startup_001.yml`, `exec_build_2026_081.yml`,
`proc_sys_startup_001.yml`, `suite_release_smoke.yml`), their internal
`id:` fields lowercased to match, and every file that referenced the old
names or IDs updated in the same pass. Every `.rst` file in the repo was
already lowercase before this rule was written down — nothing to rename
there.

No automated check enforces this yet — it's a documented convention, not
a CI gate. Worth adding a lint step alongside `tools/check_broken_links.py`
/ `tools/check_orphan_needs.py` if repeat violations show up; not done
here since one wasn't asked for.

## Known gaps (disclosed, not yet resolved)

**Resolved since the last pass** (kept here briefly for the audit trail,
not as open items):

- `SYS_001` was a dead link on both `feat_a_001` and `feat_z_001` — fixed
  by adding `needs/systemslifecycle/sys_001.rst`, the missing parent both
  features already pointed at.
- `needs/conf.py` registering `eng_need` was previously reported as
  missing; it is in fact registered (see the `eng_need` entry in
  `needs_types`, added specifically to fix a past "Unknown directive type"
  failure). The `feat_req`/`business-needs.rst`/`org_req`-in-`needs/`
  claims below them were stale — `org_req` is a **root-project** type
  (`conf.py`, not `needs/conf.py`) by design; the two are deliberately
  separate Sphinx projects (see `STANDARDS.md`). No `feat_req` directive
  or `business-needs.rst` file exists anywhere in the current tree — this
  section had drifted from the repo it describes.

**Found and fixed while verifying the SYS_001 fix with a real build**
(static file inspection had missed all of these):

- Root `conf.py` had no Sphinx `version` set, which made
  `needs_external_needs` (the mechanism `needs/conf.py` uses to import
  this project's needs as checked link targets) fail on every run with
  `NeedsExternalException: No version defined` — independent of any real
  content. Fixed by setting `version`/`release`.
- `needs/index.rst` did not exist even though `needs/conf.py` sets
  `master_doc = "index"` — every build of `needs/`, hard-gated or not,
  crashed with "Sphinx is unable to load the master document," so the
  `-W` gate in `ci-needs.yml` had never actually completed a run. Fixed
  by adding `needs/index.rst` with a toctree over the existing content.
- `organisation/tools/tool_register.rst`: all 20 `tool` needs declared
  `:links: ORG_TOOLREG_001`, which didn't exist — the same dead-link
  pattern as `SYS_001`, one layer up, in the organizational graph. Fixed
  by adding `ORG_TOOLREG_001` (the parent the file's own opening line
  already asserted).
- `organisation/governance/aspice/process_description.rst`: placeholder
  text `FEAT_/COMP_/UNIT_` was parsed by docutils as three broken
  hyperlink targets (trailing `_`), producing real build errors on every
  run. Fixed by escaping as inline literals.

**Found and fixed in the follow-up pass** (the org-graph/product-graph
citation link — the specific gap flagged as invalidating the repo's
traceability claim, so fixed before anything else):

- `needs_external_needs` was disabled after the pass above, because
  `needs/conf.py`'s `needs_types`/`needs_fields` didn't recognize the
  root project's 7 external types
  (`org_req`/`risk`/`problem`/`change`/`exception`/`tool`/`infra`) or
  their fields — every external need failed to load with "Unknown need
  type" / "Unknown keys in external need source". Fixed by adding
  matching `needs_types`/`needs_fields` entries to `needs/conf.py`
  (copied from root `conf.py`, both files carry a comment to keep them
  in sync) and re-enabling the import. Re-verified with a real `-W`
  build of `needs/` with all 52 needs (product + imported org-level)
  loading clean — a product need can now cite an org-level id as a
  real, dead-link-checked `:links:` target instead of free-text prose
  that could silently stop resolving to anything.
- `ORG_TOOLCFG_001` and `ORG_TOOLQUAL_001`, referenced in
  `tool_register.rst`'s prose but never created, now exist in the new
  `organisation/tools/tool_qualification_requirements.rst`, each linked
  to `ORG_TOOLREG_001` — turning three previously disconnected top-level
  asserts into a proper 3-node subtree (register exists → version
  pinning policy, TCL/qualification policy). Both are `:status: draft`
  and disclose the real, still-open work (most tools unpinned, no TCL
  determined for any tool) rather than claiming it's done.

**Correction (this pass): the "~10 missing documents" claim above was
wrong.** It was based on an incomplete local working copy — only files
individually pulled in over the course of this engagement, not the real
repository — not on the actual repo. Every one of
`organisation/testing/iso29119/`, `organisation/tools/`,
`organisation/strategy/`, `organisation/common_framework/`,
`management/**`, and `integration test/` already has real, authored
content on disk (cybersecurity, functional safety, and quality
organizational requirements included — none of that existed in the
picture this README gave before this pass). Re-verified against a
complete pull of the real tree and a real build. The false claim is left
struck through in spirit by this note rather than silently deleted, so
the correction itself is part of the audit trail.

**Found and fixed once the real, complete tree was actually built**
(these were real defects, just previously invisible behind the
incomplete-copy problem above):

- `organisation/governance/systemslifecycle/org_project_enabling_requirements.rst`
  cited four org-level ids with an `ORG_ASPICE_*` prefix
  (`ORG_ASPICE_APPRAISAL_001`, `ORG_ASPICE_COMPETENCE_001`,
  `ORG_ASPICE_SUP1_001`, `ORG_ASPICE_CL_POLICY_001`) that don't exist —
  the real needs were created under an `ORG_QUALITY_*` prefix in
  `organisation/governance/quality/org_quality_requirements.rst`. Same
  shape of bug as `SYS_001` and `ORG_TOOLREG_001`: content moved, the
  citing prose's ids weren't updated to match. Fixed by correcting the
  four `:need:` targets to the real `ORG_QUALITY_*` ids.
- `integration test/index.rst`'s toctree pointed at `teststrategy/`,
  `testcases/`, `testreports/` (no space) — the real folders are
  `test strategy/`, `test cases/`, `test reports/` (with a space). Fixed
  by correcting the three toctree entries; all three real documents are
  now actually reachable in the build instead of silently orphaned.
- `organisation/governance/systemslifecycle/index.rst` was real on disk
  but had never been pulled into this working copy either, so
  `organisation/governance/index.rst`'s reference to it looked broken —
  it wasn't. Pulling it in resolved the warning with no content change.

**Added this pass: named link semantics (`needs_links`).** Both `conf.py`
and `needs/conf.py` now register seven named link types
(`derived_from`/`satisfies`/`fulfils`/`implements`/`verifies`/
`belongs_to`/`consists_of`), copied from `qorix-ik-main`'s `qik-axon`
scaffold so this repo's link vocabulary aligns with that tooling. This is
purely additive — no existing id, type, or format changed. The
unambiguous ASPICE requirement/architecture/design/test chain now uses
them: `feat` `:satisfies:` `sys`, `comp` `:satisfies:` `feat`, `unit`
`:satisfies:` `comp`, `tc` `:verifies:` `unit`, `itc` `:verifies:`
`comp` (10 files). The ISO 26262 `sg`/`fsr`/`tsr` chain intentionally
still uses plain `:links:` — ISO 26262's own language leans toward
"derived from" rather than "satisfies" there, and picking the exactly
right verb wasn't obvious enough to guess, so it's left generic rather
than asserted. See `needs/needs_types_definition.rst`'s new "Link types"
section for the full table.

Discovered while making this change, and fixed in the same pass: sphinx-
needs stores each named link type under its own `needs.json` key (e.g.
`satisfies`/`satisfies_back`), separate from `links`/`links_back` —
verified directly against a real build's `needs.json`, not assumed.
`tools/check_broken_links.py` and `tools/check_orphan_needs.py` predate
this and only inspected `links`/`links_back`; unchanged, they would have
stopped dead-link-checking the 10 retrofitted needs and misreported them
as new orphans the moment `:satisfies:`/`:verifies:` replaced their
`:links:` field. Both scripts now check every field in the same
`LINK_FIELDS` list (kept in sync with `needs_links` in both `conf.py`
files) — re-verified with a real build afterward showing 0 broken links
and no new orphans.

**Added this pass: closed `status` vocabulary + `:version: 1.0.0` on
requirement-shaped needs.** Both `conf.py` and `needs/conf.py` now
constrain the built-in `status` field to a fixed 10-value enum (`none`/
`draft`/`proposed`/`approved`/`released`/`deprecated`/`retired`, the qik
document-maturity states, folded together with `open`/`closed`/
`resolved`, this project's own issue-lifecycle states used by the
`risk`/`problem`/`change` registers). The two sets had to be one list:
sphinx-needs has no per-type status schema, so a status field is either
unconstrained repo-wide or constrained repo-wide.

This is enforced as `needs_fields["status"]["schema"]["enum"]`
(`NEEDS_STATUS_ENUM` in both `conf.py` files), **not** the
`needs_statuses` config option the qik scaffold uses — the installed
sphinx-needs here (8.3.1) logs `Config option "needs_statuses" is
deprecated. Please use "needs_fields.status.schema.enum"...` under a
real `-W` build the moment `needs_statuses` is non-empty. Caught by
actually building, not by copying the qik pattern uncritically. Every
existing `:status:` value in the repo (`draft` ×70, `approved` ×35,
`open` ×1) is a member of the enum, so this is non-breaking today; it
only starts rejecting anything going forward that isn't one of the ten.

`:version: 1.0.0` was added to every need of a native, requirement-
shaped type — `sys`/`feat`/`comp`/`unit`/`sg`/`fsr`/`tsr`/`eng_need`/
`safefeat`/`rec`/`res`/`tc`/`itc` in `needs/`, `org_req` in the root
project — 82 needs across 26 files, mechanically via a script that
inserts the field right after each need's `:status:` line and reports
what it touched (verified against the printed report before trusting
it: 0 needs of a target type had no `:status:` line to anchor on, 0
already had a `version`). Deliberately **not** added to `risk`/
`problem`/`change`/`exception`/`infra` (issue-register entries, not
versioned requirement text) or to `tool` (where `version` already means
the tool's own pinned version, per the field's pre-existing
description — adding a baseline "1.0.0" there would read as a false
claim that a tool's version is pinned when for most tools it isn't, see
`ORG_TOOLCFG_001`). The `version` field's description in both `conf.py`
files was updated to spell out this dual meaning, since it previously
only documented the tool-pinned-version half. Re-verified with real
`-W` builds of both projects afterward: `needs/` builds with 0
warnings (19 native needs, all 19 carrying `version`); the root
project's own count is 67 versioned needs (54 `org_req` newly
versioned this pass, plus 6 more from `organizational_requirements.rst`,
plus 7 `tool` needs that already had a pinned `version` from before,
left untouched).

Found while verifying this change, not caused by it, and **not fixed**
(out of scope — see the next section): the root project's own `-W`
build errors on `doc/manuals/safety/safety_user_manual.rst` with
`Unknown directive type "safefeat"` (and `"rec"`/`"res"`) — that file
lives in the root project's tree (`doc/`, not excluded) but uses need
types that are only registered in `needs/conf.py`, not in root
`conf.py`. Every `:need:`/`:need:` cross-reference in that file to
`tsr_001`/`SAFEFEAT_A_001` renders as "Unknown need" rather than a real
link as a result. This predates this pass — the `:version:`/`:status:`
edits made to that file's `safefeat`/`rec`/`res` entries didn't create
or worsen it — and was never caught before because no prior pass had
actually run a real `-W` build of the root project's full tree
(`doc/manuals/`) end to end; the `docs.yml` CI workflow that would have
caught it is intentionally not `-W` yet either (see below).

**Added this pass: `asil` and `cal` fields.** Both registered in
`needs/conf.py`'s `needs_fields`, nullable, each constrained to a real
schema enum (`asil`: `QM`/`ASIL A`/`ASIL B`/`ASIL C`/`ASIL D`; `cal`:
`CAL 1`–`CAL 4`). Deliberately **not** stamped across every requirement —
only where a real HARA or TARA outcome exists to back the value up,
following the same standard's-own-rigor discipline as the rest of this
pass. `:asil: ASIL B` is set on the seven needs that make up the
determined safety chain and what it links into: `sg_001`, `fsr_001`,
`tsr_001`, `comp_a_001`, `UNIT_A_001`, `tc_unit_a_001`,
`itc_comp_a_001_001`. Diagnostics is deliberately left unset —
`functionalsafety/analyses/dependent-failure-analysis.rst` already
records it as "not yet assessed," and setting an ASIL there would
assert a HARA outcome that never happened. `cal` is registered but
populated on nothing: `needs/cybersecurity/tara/index.rst` is an
explicit empty stub with no `cyber_req`/`threat` need type yet, so
there is no TARA-derived cybersecurity goal anywhere in this project
for a CAL to attach to. See `needs/needs_types_definition.rst`'s new
"Safety and cybersecurity classification" section for the full table
and rationale. Re-verified with a real `-W` build afterward: `needs/`
still builds with 0 warnings.

**Added this pass: every requirement-shaped need set to `:status:
proposed`.** All 82 needs in the same scope as the `:version: 1.0.0`
pass above (`sys`/`feat`/`comp`/`unit`/`sg`/`fsr`/`tsr`/`eng_need`/
`safefeat`/`rec`/`res`/`tc`/`itc` in `needs/`, `org_req` in the root
project) were set to `proposed`, overwriting whatever they held before
— unconditionally, per the instruction, not just moving `draft` forward.
Worth being explicit about the consequence, since it's a real governance
change, not just a label swap: **35 of these had been `approved`**, and
that set includes the entire determined ISO 26262 safety chain
(`sg_001`, `fsr_001`, `tsr_001`, `comp_a_001`, `UNIT_A_001`,
`tc_unit_a_001`, `itc_comp_a_001_001` — the same seven needs that just
got `asil: ASIL B` above) and every stakeholder/business/operational
`eng_need`. Those are now `proposed` again, i.e. reviewed-but-not-yet-
approved, not draft. `risk`/`problem`/`change`/`exception`/`tool`/
`infra` needs were deliberately left untouched — `proposed` is a
document-maturity state and doesn't fit an issue-lifecycle entry like
`CR_001` (`change`, still `approved`) or `PRB_001` (`problem`, still
`open`). Re-verified afterward: both projects still build the same as
before this change (`needs/` 0 warnings; root project's pre-existing 26
warnings, all already disclosed above, unchanged), 0 broken links, no
new orphans.

**Still open (out of scope of a link/toctree fix — flagged, not fixed):**

- Five identical "Process Description" template stubs
  (`organisation/governance/{aspice,cybersecurity,functionalsafety,quality,systemslifecycle}/process_description.rst`)
  build successfully but aren't included in any toctree — consistent
  across all five, so this reads as deliberate (placeholders awaiting
  real per-process content, not wired in yet) rather than an oversight.
- `getting_started.rst` links to `:doc:`needs_overview`` — a page that
  was never created. Left disclosed rather than authored a placeholder
  for it; a real organizational-requirements overview page is content
  work, not a link fix.
- 59 organizational requirements across `org_project_enabling_requirements.rst`,
  `org_cybsec_requirements.rst`, `org_fusa_requirements.rst`,
  `org_quality_requirements.rst`, `organizational_requirements.rst`
  (ISO 29119), plus one each of `CR_`/`PRB_`/`RISK_` register entries,
  are legitimate top-of-hierarchy orphans — org-level policy asserted
  ahead of any product-level work that would cite it, exactly the same
  shape as the original 29. Captured in `tools/orphan_baseline.json`
  (regenerated this pass from the real, complete graph — 86 needs total,
  0 broken links); the CI gate fails only on **new** orphans beyond this
  disclosed set. `ORG_INFRA_002` came off the baseline this pass — real
  content now links to it.
- Several narrative sections of this README (including the full repo
  tree diagram's `Needs/` subtree) describe an earlier, more elaborate
  intended structure — `business-needs.rst`, `operational-needs.rst`,
  `stakeholder-needs.rst`, `FEAT_DIAGNOSTICS_001` — that doesn't match
  the current `needs/` tree (`systemslifecycle/`, `communication/`,
  `diagnostics/`). Disclosed here rather than silently left inconsistent;
  reconciling the tree diagram with reality is separate follow-up work.

**Found and fixed while verifying the named-link change with a real
build** (this project's own `-W` gate had not actually completed a clean
run in some time — these were real, currently-failing defects, not
theoretical):

- `needs/index.rst`'s toctree only wired in `systemslifecycle/index` plus
  one leaf document each from Communication and Diagnostics. Every other
  real page — both modules' own `index.rst`, `cybersecurity/index.rst`,
  `functionalsafety/index.rst`, `quality/index.rst`, the three
  pre-requirements pages, `needs_types_definition.rst` — built but was
  unreachable from the master document, which fails `-W` on
  `toc.not_included` for each one (9 separate warnings). Fixed by wiring
  in the module-level index pages (which already cascade to their own
  children) instead of individual leaves, plus the previously-orphaned
  standalone pages.
- `needs/communication/index.rst`'s toctree referenced `unit
  design/unit_a_001` and `unit test/index` directly — but those files
  live one level deeper, under `component/`, not at the module level
  (`diagnostics/component/index.rst` already had an explicit note saying
  as much, describing a migration that, for communication, only half
  happened). Fixed by removing the two stale entries from
  `communication/index.rst` and wiring them into
  `communication/component/index.rst` instead, matching diagnostics'
  already-correct layout exactly.
- `needs/communication/component/unit test/index.rst`'s toctree read
  `test-cases/index` / `test-reports/unit-test-report` (hyphenated); the
  real folders are `test cases/` / `test reports/` (with a space) — the
  same shape bug already fixed once in `integration test/index.rst`.
  Fixed by correcting both entries.
- `needs/communication/component/unit test/test cases/index.rst` had a
  `:doc:` reference one directory level too shallow
  (``../../feature/feat_a_001`` instead of
  ``../../../feature/feat_a_001``) — comparing against diagnostics'
  equivalent, correctly-written reference caught it. Fixed.

Re-verified afterward with a real `sphinx-build -b html -W` of `needs/`
against a representative external-needs stub: **0 warnings, build
succeeded** (previously this exact command failed with 19 warnings
treated as errors, none of which were caught by any prior pass because
no one had actually re-run the full `-W` build since the tree was
completed).

**Correction to the "CI gates" claim below:** `.github/workflows/ci-needs.yml`
on disk today does match what's described — verified by reading it
directly, its `-W` build plus the org-level export steps are live and
correct. `.github/workflows/docs.yml`, however, is **not** — the updated
version (split `check_broken_links.py` / `check_orphan_needs.py --baseline`
steps, both unconditional) exists only as a file delivered separately;
`device_commit_files` rejects GitHub Actions workflow files as
protected, so it was never actually placed. The docs.yml live on disk
right now still has the single, older, `|| echo "::warning::..."`-softened
orphan-check step and no `check_broken_links.py` step at all. Until
someone with write access places the delivered version, the root
project's traceability gate is exactly as soft as it was before that
work — this correction exists so that claim isn't taken at face value.

**CI gates, as of this pass:**

- `.github/workflows/ci-needs.yml` (`needs/` project): `-W` +
  `needs_report_dead_links = True` — a real, verified hard gate,
  including the re-enabled org-level import. A `SYS_001`-style dead link
  now fails the build, and so does a broken named link (`:satisfies:`,
  `:verifies:`, etc.) — verified directly, not assumed.
- `.github/workflows/docs.yml` (root project, **as delivered, not yet
  placed** — see the correction above): the main `html` build is
  intentionally not `-W` (see the three disclosed content gaps above —
  the two pre-existing ones plus the newly-found `safefeat`/`rec`/`res`
  registration gap — turning `-W` on would fail on those, not on
  anything link-related), but two dedicated, unconditional steps gate
  the traceability graph specifically — `tools/check_broken_links.py`
  (any dead link-type field target fails, no exceptions — verified
  clean across all 86 needs) and
  `tools/check_orphan_needs.py --baseline tools/orphan_baseline.json`
  (any orphan not already in the baseline fails). Neither is wrapped in
  `|| echo "::warning::..."` anymore. Both scripts now check every field
  in `needs_links` (see the named-link section above), not just the
  built-in `links` field.

**Added this pass: `THIRD_PARTY_NOTICES.md`.** A technical inventory of
the third-party software this repo's own manifests and CI workflows name
directly (Sphinx, sphinx-needs, furo, sphinxcontrib-plantuml, Pillow,
PlantUML, Graphviz, the OpenJDK JRE, each `source/<language>/`
sub-project's dev/test tooling, Bazel, and the GitHub Actions used),
with each license taken from that package's own published metadata —
checked directly (installed package metadata, apt `copyright` files, and
upstream `LICENSE` files), not recalled from memory. Deliberately does
**not** enumerate the full transitive dependency tree (e.g.
`sphinx-needs`'s own further runtime dependencies) — none of this repo's
manifests pin exact versions, so that tree isn't fixed or reproducible
today, and the file says so explicitly rather than faking completeness.
Marked as draft, mirroring `LICENSE`'s own "not yet reviewed by Legal/IP
counsel" status — this is a starting inventory for that review, not a
substitute for it.
