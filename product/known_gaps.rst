Known Gaps
=============

Divergences between this "Product / Program" structure and the request
it was built from, disclosed rather than hidden. Split out of
``index.rst`` on 2026-08-21 so that page stays short.

- "Needs" is now a real nested group in *this* sidebar (see
  :doc:`needs_index`, added 2026-08-23 so the group would get a
  heading at all — see that page's own note), but each of its nine
  entries is still a plain redirect into the ``needs/`` project's own
  built site, not a real cross-project toctree inclusion. ``needs/`` is
  a separate Sphinx project (own ``conf.py``, own independently
  ``-W``-gated CI build) — its left sidebar is generated from its own
  toctree and can't literally share nesting with this one without
  merging the two builds into one, which was deliberately not done
  here.
- Following any of the nine "Needs" entries (or the "Needs Type
  Definitions" entry) lands you in the ``needs/`` project's own build,
  which has its own, different top tab bar (Needs Type Definitions /
  Pre-requirements input / System / Software / Safety / Security /
  Quality) and page title ("...Needs 1.0 documentation") instead of
  this project's (Getting Started / Organization / Product / Program /
  Decision Records / Changelog / "...1.0 documentation"). This is the
  same separate-build constraint as the point above, just visible in
  the header instead of the sidebar — not fixable without either
  merging the two builds or giving ``needs/conf.py`` the same tab
  toctree as this project's ``index.rst``, both undone here.
- "Testing" here is this repo's own top-level ``testing/`` folder (test
  cases, executions, reports, strategy, suites for this product) —
  distinct from ``organisation/testing/`` (the organization-level ISO
  29119 process, under "Organization") and from the previous, now-removed
  ``integration test/index`` toctree entry (that folder no longer exists
  on disk; still tracked as deleted in git, unresolved — see the
  separate flag on this in :doc:`/changelog`).
- "Docs" is ``doc/`` — manuals, release notes, and errata. The
  product/safety user manuals briefly moved to ``needs/user_guide/`` on
  2026-08-21 and back the same day, at a request to keep them here — see
  :doc:`/changelog` and ``doc/README.md`` for why.
