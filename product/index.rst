Product / Program
=====================

Product- and program-level content for this repo: published docs,
project management records, architecture, product verification/testing,
per-language source scaffolding, and this repo's own traceability needs
(``org_req``/``risk``/``problem``/``change``/``exception``/``tool``/
``infra``/``decision`` — see ``needs_types_definition.rst``). Added
2026-08-21 to collapse what used to be separate top-level sidebar
entries (``management``, a broken ``integration test`` reference) into
one "Product / Program" entry with everything nested underneath as
collapsible sub-menus, the same pattern used for "Organization".

See :doc:`known_gaps` for divergences between this structure and the
request it was built from.

**2026-08-22: expanded the "Needs" entry from one generic redirect to
one per discipline.** ``needs/`` is still a genuinely separate Sphinx
project (own ``conf.py``, own build, own sidebar — see
``needs_redirect.rst``'s note on why a true nested toctree entry isn't
possible across two independent Sphinx builds), so each entry below is
still a same-trick meta-refresh stub, not a real cross-project toctree
inclusion. What changed is granularity: instead of a single "Needs" link
that dropped you on the needs/ landing page, there's now one named entry
per discipline (mirroring ``needs/index.rst``'s own caption structure),
so Communication and Diagnostics in particular — the two Software
features covered earlier in this repo's traceability work — are each
one click away instead of buried behind a generic link plus in-page
navigation.

**2026-08-23: gave "Needs" a real sidebar heading.** The nine entries
above were, until now, listed directly in this page's own
``:caption: Needs`` toctree — but sphinx-immaterial's global sidebar
does not render a bare toctree caption as a heading; it only shows the
title of the page(s) the toctree points at. Docs/Project
Management/Product Verification/Source each name exactly one wrapper
page (``doc/index``, ``management/index``, etc.), so that page's own
title stands in as the group's heading. "Needs" named nine pages
directly with no wrapper, so it had no page to hang a heading off —
the nine entries rendered as flat, unheaded siblings of Docs/
Architecture/etc., confirmed on the built site. Fixed by moving them
into :doc:`needs_index`, a wrapper page following the exact same
pattern as the other four groups, and pointing this toctree at that one
page instead.

.. toctree::
   :caption: Docs
   :maxdepth: 1

   /doc/index

.. toctree::
   :caption: Project Management
   :maxdepth: 1

   /management/index

.. toctree::
   :caption: Architecture
   :maxdepth: 1

   architecture/index

.. toctree::
   :caption: Product Verification
   :maxdepth: 1

   /testing/index

.. toctree::
   :caption: Source
   :maxdepth: 1

   /source/index

.. toctree::
   :caption: Needs
   :maxdepth: 1

   needs_index

.. toctree::
   :hidden:

   known_gaps
