# Configuration file for Sphinx + Sphinx-Needs
# Repo: Qorix Engineering Processes — root-level project docs.
#
# This is a SEPARATE Sphinx project from Needs/conf.py. Needs/ has its own
# conf.py and builds independently (sys/feat/comp/unit + sg/fsr/tsr — the
# product traceability graph). This root project covers everything that
# sits outside Needs/: organization-level requirements (org_req, used under
# organisation/governance/), plus plain narrative docs (doc/, management/, test/,
# organisation/verification/, organisation/strategy/).
#
# NOTE: this file previously contained Test_Dashboard's full conf.py
# (project = "product-x", a needs_types list with sys_req/hazard/threat/
# ssr/cyber_goal/etc., and source_repository pointing at Test_Dashboard's
# GitHub URL). None of that reflected this repo — it's been replaced with
# only what Qorix Engineering Processes root-level content actually uses.

project = "Qorix Engineering Processes"
master_doc = "index"
extensions = ["sphinx_needs", "sphinxcontrib.plantuml", "myst_parser"]

# sphinx-needs' needs_external_needs loader (used by needs/conf.py to pull
# this project's org_req/risk/problem/change/exception/tool/infra needs in
# as real, dead-link-checked citations instead of free text) requires a
# non-empty Sphinx `version`. Without one, sphinx-needs writes an
# empty-string current_version into needs.json and the loader raises
# NeedsExternalException("No version defined...") on every needs/ build —
# a hard failure unrelated to any actual traceability content, found while
# verifying the SYS_001 fix end-to-end with a real build instead of
# trusting static file inspection.
version = "1.0"
release = "1.0"

# CRITICAL: without this, `sphinx-build -b html . _build/html` run from the
# repo root (exactly what .github/workflows/docs.yml does) walks into
# Needs/ and tries to parse its sg/fsr/tsr/comp/feat/unit directives using
# THIS conf.py's schema (which only knows org_req) — 9 "Unknown directive
# type" errors, confirmed by testing the exact CI invocation locally.
# Needs/ is a separate Sphinx project with its own conf.py and its own CI
# job (ci-needs.yml, working-directory: Needs) — it must stay excluded here.
exclude_patterns = [
    "needs", "_build", "Thumbs.db", ".DS_Store",
    # 2026-08-21: myst_parser was just registered so doc/release_notes/
    # and source/*/README.md can build. Sphinx's source discovery has no
    # "only these specific files" mode -- registering a suffix makes
    # every matching file repo-wide a candidate document. These are
    # repo-management/meta files or content already migrated to real
    # needs directives elsewhere (see each area's own notes) -- excluded
    # so they don't turn into a wall of new "not included in any
    # toctree" orphan warnings that were never a problem while no
    # Markdown parser was registered at all.
    "README.md", "STANDARDS.md", "third_party_notices.md",
    "scripts/README.md", "testing/README.md", "doc/README.md",
    "testing/test cases/**/*.md",
    "decision records/*.md",
    "organisation/governance/README.md",
    "organisation/governance/coding guidelines/**",
    "user_guide_redirect.rst",
]

needs_types = [
    dict(directive="org_req", prefix="ORG_", color="#B8003D", style="node",
         title="Organizational Requirement — ISO 26262 Part 2 / "
                "ISO/SAE 21434 Clause 5 / ASPICE org-level / ISO 29119 "
                "org-level / ISO/IEC/IEEE 15288 clause 6.2"),

    # Management registers (management/) and the tool register (organisation/tools/).
    # Previously each entry lived only in a .yml file this Sphinx build
    # never read (risk-register.yml, problem-register.yml,
    # change-register.yml, tool_register.yml) with an .rst stub pointing at
    # it. Migrated in-place to real needs, one per existing YAML record —
    # same ids, same field values — so each gets dead-link checking and is
    # queryable via needtable instead of living outside the build.
    dict(directive="risk", prefix="RISK_", color="#B71C1C", style="node",
         title="Organizational or Project Risk"),
    dict(directive="problem", prefix="PRB_", color="#D32F2F", style="node",
         title="Problem Report"),
    dict(directive="change", prefix="CR_", color="#5C6BC0", style="node",
         title="Change Request"),
    dict(directive="exception", prefix="EXC_", color="#8E24AA", style="node",
         title="Tailoring Exception — deviation from the org-level process "
                "described in organisation/governance/framework/process_metamodel"),
    dict(directive="tool", prefix="TOOL_", color="#00838F", style="node",
         title="Qualified Tool — invoked by a CI workflow or pre-commit hook, "
                "per ASPICE SUP.8/SUP.9 tool qualification"),
    dict(directive="infra", prefix="INFRA_", color="#455A64", style="node",
         title="Infrastructure Element — ISO/IEC/IEEE 15288 clause 6.2.2, "
                "outcome (b): infrastructure identified and specified"),

    # decision records/ (repo root) — same migration shape as tool above:
    # a lightweight ADR/MADR-style record, now a real need instead of a
    # loose Markdown file this build never parses (no myst_parser/
    # recommonmark is registered in extensions above, so a bare .md under
    # "decision records/" would sit outside the build entirely). Body text
    # carries the ADR's Context / Decision drivers / Options considered /
    # Decision outcome / Consequences sections as ordinary RST prose inside
    # the directive, the same way org_req and tool bodies already do.
    dict(directive="decision", prefix="DEC_", color="#F9A825", style="node",
         title="Decision Record — architecture/engineering decision, "
                "proposed or accepted, with context and options considered"),

    # doc/manuals/safety/safety_user_manual.rst — ISO 26262-6 Safety User
    # Manual content. Copied verbatim from needs/conf.py (that project's
    # own needs_types), where this schema was originally defined, so this
    # page can build here without "Unknown directive type" errors. Its
    # :links:/:need: references to TSR_001/SG_001/FSR_001/COMP_A_001 are
    # real needs, but they're defined in the separate needs/ project, not
    # here -- this project has no way to validate or resolve them without
    # a two-way needs-import pipeline (needs/ already imports THIS
    # project's org_req etc. one way; the reverse doesn't exist), so they
    # show as "linked need not found" warnings -- disclosed in
    # doc/README.md, not fixed here.
    dict(directive="safefeat", prefix="SAFEFEAT_", color="#7B1FA2", style="node",
         title="Module Safety Feature — ISO 26262-6 Safety User Manual"),
    dict(directive="rec", prefix="REC_", color="#F57F17", style="node",
         title="Operational Recommendation — ISO 26262-6 Safety User Manual"),
    dict(directive="res", prefix="RES_", color="#EF6C00", style="node",
         title="Operational Restriction — ISO 26262-6 Safety User Manual"),
]

# Same treatment as Needs/conf.py: `derives_from` is used inconsistently in
# the org_req content as both a real need ID (e.g. ORG_SMS_001) and a
# free-text external standard-clause citation (e.g. ISO26262_2_5_4_2_1)
# with no matching need. Registering it as a needs_extra_links option would
# fail the dead-link gate on every clause citation. Kept as a free-text
# field instead — same rationale as Needs/conf.py.
#
# Closed status vocabulary, enforced on the built-in `status` field via
# needs_fields.status.schema.enum (below) rather than the older
# needs_statuses list config — this installed sphinx-needs (8.3.1) logs
# 'Config option "needs_statuses" is deprecated. Please use
# "needs_fields.status.schema.enum"...' the moment needs_statuses is
# non-empty (confirmed by an actual -W build), so needs_statuses was
# never committed here. Combines two things that were previously both
# free text: (a) the document-maturity states used by every requirement-
# shaped need (draft/approved today, 70/35 real usages respectively),
# copied from qorix-ik-main's qik-axon scaffold; and (b) the issue-
# lifecycle states used by this project's own registers (risk/problem/
# change), where `open` is the one real example in use today
# (management/problem/problems.rst). Folded into one enum rather than
# kept separate because the status field has no per-type schema — one
# list, applying repo-wide, is all the mechanism allows. `open` is kept
# distinct from `draft`: a problem/risk/change register entry being
# "open" describes whether the issue itself is still active, not
# whether its *text* has been reviewed. Kept identical to the same
# constant in Needs/conf.py.
NEEDS_STATUS_ENUM = [
    "none", "draft", "proposed", "approved", "released", "deprecated",
    "retired", "open", "closed", "resolved",
]

needs_fields = {
    "status": {
        "description": "Need status. Enum enforced via schema, not the "
                        "deprecated needs_statuses config — see the "
                        "comment above NEEDS_STATUS_ENUM.",
        "schema": {"enum": NEEDS_STATUS_ENUM},
        "nullable": True,
    },
    "standard": {
        "description": "Standard/clause this need satisfies",
        "schema": {"type": "string"},
        "nullable": True,
    },
    "derives_from": {
        "description": "Upstream ID or external standard clause this "
                        "requirement derives from (free text — not "
                        "dead-link-checked)",
        "schema": {"type": "string"},
        "nullable": True,
    },
    "likelihood": {
        "description": "Risk likelihood (from risk-register.yml)",
        "schema": {"type": "string"},
        "nullable": True,
    },
    "impact": {
        "description": "Risk impact (from risk-register.yml)",
        "schema": {"type": "string"},
        "nullable": True,
    },
    "mitigation": {
        "description": "Risk mitigation plan (from risk-register.yml)",
        "schema": {"type": "string"},
        "nullable": True,
    },
    "affected_needs": {
        "description": "Need IDs a problem/change affects, as recorded in "
                        "problem-register.yml / change-register.yml. Kept "
                        "as free text, not a real link — these ids "
                        "(SWR_*, SYSR_*) are illustrative placeholders used "
                        "elsewhere in the repo (see test/teststrategy/) "
                        "and don't resolve to any actual need, so "
                        "registering this as a needs_extra_links option "
                        "would fail the dead-link gate.",
        "schema": {"type": "string"},
        "nullable": True,
    },
    "pinned": {
        "description": "Whether the tool's version is pinned in CI "
                        "(from tool_register.yml: version_pinned)",
        "schema": {"type": "string"},
        "nullable": True,
    },
    "version": {
        "description": "Two distinct uses, disambiguated by need type: for "
                        "`tool` needs, the pinned version string when known "
                        "(from tool_register.yml) — most tools still have "
                        "none, a real disclosed gap, see ORG_TOOLCFG_001. "
                        "For every other requirement-shaped need type "
                        "(org_req/sys/feat/comp/unit/sg/fsr/tsr/eng_need/"
                        "safefeat/rec/res/tc/itc), a baseline content "
                        "version (currently 1.0.0 on all of them, added in "
                        "the same pass as the `status` enum above) — not "
                        "a tool's version, the requirement text's own "
                        "revision.",
        "schema": {"type": "string"},
        "nullable": True,
    },
    "toolchain_step": {
        "description": "build / static_analysis / test_execution / "
                        "traceability (from tool_register.yml)",
        "schema": {"type": "string"},
        "nullable": True,
    },
    "used_in": {
        "description": "Module(s) or project(s) this tool is used in "
                        "(from tool_register.yml)",
        "schema": {"type": "string"},
        "nullable": True,
    },
    "ci_workflow": {
        "description": "Workflow file(s) that invoke this tool "
                        "(from tool_register.yml)",
        "schema": {"type": "string"},
        "nullable": True,
    },
    "tcl": {
        "description": "Tool Confidence Level, ISO 26262-8 clause "
                        "11.4.5-11.4.7 (from tool_register.yml — TBD for "
                        "every tool, no determination made yet)",
        "schema": {"type": "string"},
        "nullable": True,
    },
    "qualification_status": {
        "description": "Tool qualification status (from tool_register.yml)",
        "schema": {"type": "string"},
        "nullable": True,
    },
    "provider": {
        "description": "Who provides/hosts this infrastructure element "
                        "(e.g. GitHub Actions, GitHub Pages, local machine)",
        "schema": {"type": "string"},
        "nullable": True,
    },
    "acquisition": {
        "description": "How this infrastructure element was acquired "
                        "(SaaS subscription, self-hosted, checked-in config "
                        "file, etc.) — ISO/IEC/IEEE 15288 clause 6.2.2 "
                        "outcome (c)",
        "schema": {"type": "string"},
        "nullable": True,
    },
    "availability_note": {
        "description": "What guarantees availability today, and what "
                        "monitors it — ISO/IEC/IEEE 15288 clause 6.2.2 "
                        "outcome (d). Free text; disclose 'none' rather "
                        "than implying monitoring that doesn't exist.",
        "schema": {"type": "string"},
        "nullable": True,
    },

    # --- Fields used by the safefeat/rec/res types above (doc/manuals/
    # safety/safety_user_manual.rst). Copied verbatim from needs/conf.py;
    # keep both in sync if either changes.
    "rationale": {
        "description": "safefeat: rationale for claiming safety in this feature",
        "schema": {"type": "string"},
        "nullable": True,
    },
    "use_case": {
        "description": "safefeat: use case for the safety feature",
        "schema": {"type": "string"},
        "nullable": True,
    },
    "dependency": {
        "description": "safefeat: internal or external dependency, if any",
        "schema": {"type": "string"},
        "nullable": True,
    },
    "input_reference": {
        "description": "rec/res: Safety Requirement ID or Safety Analysis "
                        "ID (e.g. a DFMEA action ID) this entry originates "
                        "from",
        "schema": {"type": "string"},
        "nullable": True,
    },
    "req_type": {
        "description": "rec/res: Timing, Execution Sequence, Resource, "
                        "Performance, Implementation, External Dependency, "
                        "Configuration, etc.",
        "schema": {"type": "string"},
        "nullable": True,
    },
    "actions": {
        "description": "rec/res: recommended action for the integrator",
        "schema": {"type": "string"},
        "nullable": True,
    },
}

# Named link types, additive alongside the default `:links:` field — nothing
# existing is renamed or required to use these. Copied verbatim from
# qorix-ik-main's qik-axon scaffold (rust/qik-axon/templates/needs/conf.py)
# so this project's link vocabulary aligns with the org's own tooling if it
# is ever adopted here. sphinx-needs dead-link-checks every field listed
# here exactly like the built-in `links` field (verified with a real -W
# build before this was added) — but tools/check_broken_links.py and
# tools/check_orphan_needs.py, which pre-date this, only inspected the
# `links`/`links_back` keys in needs.json. Both were updated in the same
# change (see their own comments) so a need connected only via one of
# these named fields is neither missed by the dead-link gate nor
# misreported as an orphan.
needs_links = {
    "derived_from": {"incoming": "gives rise to",     "outgoing": "derived_from"},
    "satisfies":    {"incoming": "is satisfied by",   "outgoing": "satisfies"},
    "fulfils":      {"incoming": "is fulfilled by",   "outgoing": "fulfils"},
    "implements":   {"incoming": "is implemented by", "outgoing": "implements"},
    "verifies":     {"incoming": "is verified by",    "outgoing": "verifies"},
    "belongs_to":   {"incoming": "consists of",       "outgoing": "belongs_to"},
    "consists_of":  {"incoming": "belongs to",        "outgoing": "consists_of"},
}

needs_id_required = True
needs_id_regex = r"^[A-Z]+_[A-Za-z0-9_]+"
needs_report_dead_links = True

# --- Theme: match the Performance Documentation site's navigation, with a
#     sharper UI than pydata-sphinx-theme (side-by-side comparison requested
#     and reviewed 2026-08-21; sphinx-immaterial + navigation.tabs chosen).
# extensions was set once above (needs/plantuml) — appended to, not
# replaced, so this stays additive if this file is edited again later.
#
# 2026-08-21: added the Score (score.dev) documentation UX patterns that
# translate directly onto this theme's real, supported feature flags —
# verified against the installed sphinx_immaterial package's own templates
# rather than assumed, since not every mkdocs-material feature made it into
# this Sphinx port (e.g. "navigation.path" breadcrumbs did NOT — see the
# "Known gaps" note below):
#   - content.action.edit / content.action.view: pencil + eye icons at the
#     top of the content area, linking to this page's source on GitHub —
#     same purpose as Score's "Edit this page" / "View page source" links.
#     Needs a real edit_uri (was "", which disables both icons entirely).
#   - search.suggest: autocomplete-style search suggestions, closer to the
#     instant Algolia search Score's docs use.
#   - navigation.top: back-to-top button on long pages.
extensions = extensions + ["sphinx_immaterial"]
html_theme = "sphinx_immaterial"
html_static_path = ["_static"]
html_css_files = ["custom.css"]

# 2026-08-21: replaced sphinx-immaterial's default logo (a generic white
# book-icon glyph on a colored square, not a Qorix asset) with the real
# Qorix logo. html_logo (top-level Sphinx setting, not a theme option) is
# what sphinx-immaterial actually reads for the header logo -- verified by
# checking the installed theme's own layout template rather than assumed.
# Same file kept in sync across both Sphinx projects' own _static/ (root
# and needs/), the same pattern already used for custom.css.
html_logo = "_static/qorix_logo.png"
html_theme_options = {
    "icon": {"repo": "fontawesome/brands/github"},
    "site_url": "https://swatidavari.github.io/qorix-asr-ap-r20-11_temp/",
    "repo_url": "https://github.com/SwatiDavari/qorix-asr-ap-r20-11_temp",
    "repo_name": "qorix-asr-ap-r20-11_temp",
    # Root project's srcdir IS the repo root, so doc2path() already returns
    # paths relative to the repo root (e.g. "index.rst") — edit_uri just
    # needs the branch. Verified against a real build's rendered edit-link
    # href, not assumed (see needs/conf.py for why this project's needs a
    # "/needs" suffix instead).
    "edit_uri": "edit/main",
    # Disables sphinx_immaterial.google_fonts's live fetch to
    # fonts.google.com at build time — required in CI, where GitHub
    # Actions runners can't reach it (confirmed: build fails with
    # ExtensionError / ProxyError without this).
    "font": False,
    # Light/dark toggle - genuinely supported by this theme (unlike
    # breadcrumbs / the Ctrl+K search hint, checked directly against the
    # installed sphinx-immaterial 0.13.9 package source and confirmed
    # absent there). "default" keeps the Qorix navy/purple palette
    # already defined in custom.css; "slate" is the theme's own built-in
    # dark palette, left un-overridden deliberately - picking Qorix's own
    # dark-mode brand colors is a brand-team decision, not mine to make
    # unilaterally.
    "palette": [
        {
            "media": "(prefers-color-scheme: light)",
            "scheme": "default",
            "toggle": {"icon": "material/toggle-switch-off-outline", "name": "Switch to dark mode"},
        },
        {
            "media": "(prefers-color-scheme: dark)",
            "scheme": "slate",
            "toggle": {"icon": "material/toggle-switch", "name": "Switch to light mode"},
        },
    ],
    "features": [
        "navigation.tabs",
        "navigation.tabs.sticky",
        "navigation.sections",
        "navigation.top",
        "search.share",
        "search.suggest",
        "toc.follow",
        "content.action.edit",
        "content.action.view",
    ],
    # Sidebar (left-nav global TOC) is hardcoded by sphinx-immaterial to
    # maxdepth=-1 (see nav_adapt.py) - the toctree ":maxdepth:" directive
    # only controls the in-page bullet list, not the sidebar. Default
    # True collapses the sidebar to only the active page's ancestor
    # chain; False keeps every level expandable so every nested page is
    # reachable from the sidebar without drilling through intermediate
    # landing pages first. Verified via real build + screenshot.
    "globaltoc_collapse": False,
}
