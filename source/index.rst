Source
=========

Per-language scaffolding and coding-guideline notes for this repo's
source code (C, C++, Python, Rust, TypeScript, and a ``markdown/``
folder for working drafts) — as distinct from ``needs/`` (traceable
requirements) and ``doc/`` (published documentation deliverables). Each
language folder's own ``README.md`` below is real content already on
disk; this page and its ``myst_parser`` toctree just make them
browsable here for the first time, rather than only readable by opening
the folder directly.

Actual per-language *coding style rules* (as opposed to this
scaffolding) live in the separate ``qorix-gnc`` repo, under
``governance/coding guidelines/`` — deliberately not linked from here or
anywhere else in this build: that folder is plain Markdown too, but
belongs to a different repo/project (this page's ``myst_parser``
registration doesn't reach it), and pulling it in wasn't part of this
change.

.. toctree::
   :maxdepth: 1

   c/README
   cpp/README
   python/README
   rust/README
   typescript/README
   markdown/README
