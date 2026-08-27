Getting Started
================

This page gets a new clone of this repository building — both the
documentation and, briefly, where the per-language source lives. It
assumes a Windows machine with VS Code, matching the primary development
setup for this repo.

Prerequisites
-------------

- Git
- Python 3.11 (the version ``.github/workflows/docs.yml`` builds with;
  ``ci-needs.yml`` uses 3.12 — either works locally)
- VS Code, with the recommended extensions in ``.vscode/extensions.json``
  (in particular ``lextudio.restructuredtext`` for ``.rst`` editing)

Clone and set up a virtual environment
---------------------------------------

.. code-block:: bat

   git clone <this-repo-url>
   cd qorix-asr-ap-r20-11_temp
   python -m venv .venv
   .venv\Scripts\activate.bat

Install documentation dependencies
------------------------------------

This repo builds **two independent Sphinx projects** — the root project
(this one) and ``Needs/`` — each with its own dependency set, matching
what their respective CI jobs install:

.. code-block:: bat

   :: root project (.github/workflows/docs.yml)
   pip install sphinx sphinx-needs furo sphinxcontrib-plantuml Pillow

   :: Needs/ project (Needs/requirements.txt, used by ci-needs.yml)
   pip install -r Needs\requirements.txt

``sphinxcontrib-plantuml`` also needs PlantUML itself (Java + Graphviz) to
render ``.. uml::`` diagrams. Skip this unless you're editing one:

.. code-block:: bat

   winget install EclipseAdoptium.Temurin.17.JRE
   winget install Graphviz.Graphviz

Then point ``conf.py``'s ``plantuml`` setting at your downloaded
``plantuml.jar``.

Populate organisation/ (governance content, from qorix-gnc + qorix-vnv)
------------------------------------------------------------------------

``organisation/`` is no longer committed to this repo — it's owned by two
sibling repos, each the single source of truth for its own slice:
`qorix-gnc <https://github.com/SwatiDavari/qorix-gnc>`_ (governance,
strategy, infrastructure, learning management, common framework, tools)
and `qorix-vnv <https://github.com/SwatiDavari/qorix-vnv>`_ (``testing/``
— ISO 29119 org-level test-process governance, split out of qorix-gnc on
2026-08-23). Both are only ever generated on disk locally, never checked
in. **CI does this automatically** — both ``.github/workflows/docs.yml``
and ``ci-needs.yml`` check out ``qorix-gnc`` and ``qorix-vnv`` and run
``scripts/sync_org_content.sh`` before building, so a fresh CI run no
longer needs anything extra from you.

Locally, this is still a manual step. ``qorix-engg.code-workspace``
mounts sibling checkouts named ``qorix-gnc`` and ``qorix-vnv``, matching
their own names on GitHub. ``scripts/sync_org_content.sh`` defaults to
looking for ``../qorix-gnc`` and ``../qorix-vnv``, so either clone both
repos using those exact local folder names, or pass their real paths
explicitly:

.. note::
   The workspace opens both as ``(read-only reference)`` roots — each
   sibling repo carries its own ``.vscode/settings.json`` setting
   ``files.readonlyInclude`` so VS Code blocks accidental edits there.
   They're owned upstream (``qorix-gnc``/``qorix-vnv`` on GitHub);
   change their content in those repos, not through this workspace.

.. code-block:: bat

   :: if you cloned either repo as a sibling folder under a different name
   scripts\sync_org_content.sh ..\qorix-gnc ..\qorix-vnv

   :: or, matching the workspace file's assumed names
   scripts\sync_org_content.sh

Run this before building the root project or refreshing
``needs/_external_needs/org_needs.json`` — both need
``organisation/governance/`` physically present.

.. note::
   ``qorix-gnc`` (and ``qorix-vnv``) link their own child governance pages via prose
   (``:doc:`` references) rather than a toctree — a leftover workaround
   for Furo's sidebar rendering at full depth regardless of
   ``:maxdepth:``, from before this repo switched themes. Synced in here
   unchanged, so several of its leaf requirement pages will show as
   "document isn't included in any toctree" warnings on this project's
   own build — harmless (this build isn't ``-W``-gated), see
   ``index.rst`` for the full explanation.

Build the documentation
-------------------------

Each project builds from its own directory, exactly as CI runs it:

.. code-block:: bat

   :: root project — mirrors docs.yml
   sphinx-build -b html . _build\html
   start _build\html\index.html

   :: Needs/ project — mirrors ci-needs.yml (warnings fail the build)
   cd Needs
   sphinx-build -b html -W . _build\html
   start _build\html\index.html
   cd ..

Re-run the relevant command after edits; delete the project's ``_build``
folder first for a clean rebuild.

In VS Code, the ``Needs`` build is also wired up as a task — press
``Ctrl+Shift+B`` and pick **Needs: build (sphinx-needs)**. There's no
equivalent task for the root project yet.

Continuous integration
------------------------

Pushing to ``main`` or opening a pull request runs both docs builds
automatically:

- ``docs.yml`` builds the root project, runs the orphan-needs
  traceability gate, and deploys to GitHub Pages on ``main``.
- ``ci-needs.yml`` builds ``Needs/`` with ``-W`` (any warning fails the
  job) whenever a push or PR touches ``Needs/**``.

Check the **Actions** tab on GitHub for build status.

Beyond the docs
------------------

This repository also contains real, independently buildable source for
five languages under ``source/`` (``c``, ``cpp``, ``python``, ``rust``,
``typescript``), each with its own README and VS Code build/test task —
see ``source/<lang>/README.md`` for language-specific setup.

Where to go next
-------------------

- ``STANDARDS.md`` — how each folder maps onto ASPICE / ISO 15288 /
  ISO 26262 / ISO 29119 terminology
- :doc:`needs_overview` — organizational requirement traceability for
  this (root) project
- ``Needs/index`` — the product traceability graph
  (system/feature/component/unit, safety chain)
- ``README.md`` — full repository structure
