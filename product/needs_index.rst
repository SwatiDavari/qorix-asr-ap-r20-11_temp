Needs
========

This repo's own traceability needs (``org_req``/``risk``/``problem``/
``change``/``exception``/``tool``/``infra``/``decision`` — see
:doc:`/needs_types_definition`), plus one entry per discipline that
redirects into the separate ``needs/`` Sphinx project (own ``conf.py``,
own build, own sidebar — see :doc:`known_gaps` for why these are
same-trick meta-refresh stubs rather than a real cross-project toctree
inclusion).

This page exists only so "Needs" gets a real parent row in the
Product / Program sidebar: sphinx-immaterial's global nav does not
render a bare toctree ``:caption:`` as a heading — the entries need a
single wrapper page to attach to, the same way ``doc/index`` gives
"Docs" its heading and ``testing/index`` gives "Product Verification"
its heading. Before this page existed, the nine entries below rendered
as flat, unheaded siblings of Docs/Architecture/etc. directly under
Product / Program.

.. toctree::
   :maxdepth: 1

   /needs_types_definition
   Overview <needs_redirect>
   Pre-requirements <needs_prerequirements_redirect>
   System <needs_system_redirect>
   Communication <needs_software_communication_redirect>
   Diagnostics <needs_software_diagnostics_redirect>
   Safety <needs_safety_redirect>
   Security <needs_security_redirect>
   Quality <needs_quality_redirect>
