Needs Type Definitions
=======================

This (``Needs/``) Sphinx project registers eleven Sphinx-Needs directives in
``conf.py``'s ``needs_types``. Every ``.. sys::``, ``.. feat::``,
``.. eng_need::``, etc. in this project's content only renders and links
because it's registered here — an unregistered directive fails the build
with ``Unknown directive type`` (this happened for real: ``eng_need`` was
used in ``business-needs.rst``/``operational-needs.rst``/
``stakeholder-needs.rst`` before it was registered, and broke the build
until it was added below).

.. note::
   **2026-08-22:** every need ID in this project was lowercased (e.g.
   ``FEAT_A_001`` -> ``feat_a_001``, ``SYS_MSGDISC_001`` ->
   ``sys_msgdisc_001``) across all 326 defined needs and every
   ``:satisfies:``/``:verifies:``/``:links:``/prose reference to them,
   in ``needs/`` and ``testing/``. ``needs_id_regex`` below updated from
   ``^[A-Z]+_...`` to ``^[a-z]+_...`` to match and enforce it going
   forward; the "ID prefix" columns in the tables below updated to their
   lowercase form for the same reason. The one ID deliberately left
   untouched is ``ORG_SMS_001`` — that's a need from the separate,
   external ``qorix-gnc`` project (imported via
   ``needs_external_needs``), not one defined in this project, so it's
   out of scope for this rename.

ASPICE / ISO 15288 requirements chain
-----------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 15 15 55 15

   * - Directive
     - ID prefix
     - Standard mapping
     - Color
   * - ``sys``
     - ``sys_``
     - ASPICE SYS.2 / ISO 15288 System Requirements Definition
     - ``#BFD8D2``
   * - ``feat``
     - ``feat_``
     - ASPICE SWE.1 / ISO 15288 Requirements Definition
     - ``#FEDCD2``
   * - ``comp``
     - ``comp_``
     - ASPICE SWE.2 / ISO 15288 Architecture Definition
     - ``#DF744A``
   * - ``unit``
     - ``unit_``
     - ASPICE SWE.3 / ISO 15288 Design Definition
     - ``#DCB239``

ISO 26262 functional safety chain
-------------------------------------

Layered onto the same needs graph so a safety requirement can link
straight into the ``sys``/``feat``/``comp``/``unit`` chain above — not
covered by ASPICE or ISO 15288 on their own.

.. list-table::
   :header-rows: 1
   :widths: 15 15 55 15

   * - Directive
     - ID prefix
     - Standard mapping
     - Color
   * - ``sg``
     - ``sg_``
     - Safety Goal — ISO 26262-3 clause 6 (HARA)
     - ``#B71C1C``
   * - ``fsr``
     - ``fsr_``
     - Functional Safety Requirement — ISO 26262-3 clause 8
     - ``#D32F2F``
   * - ``tsr``
     - ``tsr_``
     - Technical Safety Requirement — ISO 26262-4 clause 6 / ISO 26262-6
     - ``#E57373``

Pre-requirements input layer
--------------------------------

Upstream of ``sys`` — raw stakeholder/business/operational needs that
system requirements are elicited from. Not part of the ASPICE/ISO 15288
requirements-definition chain itself.

.. list-table::
   :header-rows: 1
   :widths: 15 15 55 15

   * - Directive
     - ID prefix
     - Standard mapping
     - Color
   * - ``eng_need``
     - ``need_``
     - Stakeholder / Business / Operational Need (``stakeholder-needs.rst``,
       ``business-needs.rst``, ``operational-needs.rst``)
     - ``#8E9AAF``

ISO 26262-6 Safety User Manual (customer-deliverable) types
----------------------------------------------------------------

Model the safety feature / recommendation / restriction tables that used
to live only in ``Qorix_SafetyUserManual.docx``. Module-specific IDs
(e.g. ``SAFEFEAT_A_001``) still satisfy ``needs_id_regex`` below — the
prefix column is just the auto-id default, not enforced per module.

.. list-table::
   :header-rows: 1
   :widths: 15 15 55 15

   * - Directive
     - ID prefix
     - Standard mapping
     - Color
   * - ``safefeat``
     - ``safefeat_``
     - Module Safety Feature — ISO 26262-6 Safety User Manual
     - ``#7B1FA2``
   * - ``rec``
     - ``rec_``
     - Operational Recommendation — ISO 26262-6 Safety User Manual
     - ``#F57F17``
   * - ``res``
     - ``res_``
     - Operational Restriction — ISO 26262-6 Safety User Manual
     - ``#EF6C00``

See ``software/communication/safety_user_manual.rst`` for a worked example that
links a ``safefeat`` into the existing ``tsr_001``/``sg_001`` chain.

Extra fields
--------------

Registered in ``needs_fields`` alongside the types above:

- ``standard`` — the standard/clause this need satisfies.
- ``derives_from`` — the upstream need ID or external standard clause this
  requirement derives from. Kept as free text, not a real Sphinx-Needs
  link — same rationale as the root project's ``conf.py``: a real link
  type would fail the dead-link gate on any citation without a matching
  need, even though every ``derives_from`` usage inside ``Needs/`` today
  happens to cite a real ``eng_need`` ID.
- ``kind`` — need classification used by ``eng_need``, e.g. ``need``.
- ``domain`` — requirement/need domain, e.g. ``functional``,
  ``operational``, ``business``.
- ``lifecycle_stage`` — lifecycle stage this need belongs to, e.g.
  ``stakeholder_needs``.
- ``rationale``, ``use_case``, ``dependency`` — ``safefeat`` fields.
- ``input_reference``, ``req_type``, ``actions``, ``impact`` — `rec``/
  ``res`` fields. ``input_reference`` is free text (not a real link) for
  the same reason as ``derives_from``: it frequently cites a DFMEA action
  ID that has no matching need.

Link types
------------

Beyond the built-in ``:links:`` field, ``needs_links`` in this project's
``conf.py`` (and the root project's) registers seven named, directional
link types — additive, not a replacement; nothing existing had to be
renamed to adopt them. Copied verbatim from ``qorix-ik-main``'s
``qik-axon`` scaffold so this repo's link vocabulary aligns with that
tooling if it's ever adopted here.

.. list-table::
   :header-rows: 1
   :widths: 20 30 50

   * - Field
     - Meaning (outgoing)
     - Used so far for
   * - ``derived_from``
     - derived from
     - not yet used
   * - ``satisfies``
     - satisfies
     - the ASPICE requirement/architecture/design chain: ``feat``
       satisfies ``sys``, ``comp`` satisfies ``feat``, ``unit``
       satisfies ``comp``
   * - ``fulfils``
     - fulfils
     - not yet used
   * - ``implements``
     - implements
     - not yet used
   * - ``verifies``
     - verifies
     - test cases: ``tc`` verifies ``unit``, ``itc`` verifies ``comp``
   * - ``belongs_to``
     - belongs to
     - not yet used
   * - ``consists_of``
     - consists of
     - not yet used

The ISO 26262 ``sg``/``fsr``/``tsr`` chain deliberately still uses plain
``:links:`` — which of the above verbs is exactly right there (ISO
26262's own language leans toward "derived from" rather than
"satisfies") wasn't obvious enough to guess, so it's left as a disclosed
gap rather than asserted. Every field above is dead-link-checked
identically to ``:links:`` (verified with a real ``-W`` build), and
``tools/check_broken_links.py`` / ``tools/check_orphan_needs.py`` were
updated in the same change to inspect all of them, not just ``links``.

Status and version
---------------------

``needs_statuses`` (``conf.py``) is a closed vocabulary, combined from two
sources because sphinx-needs' status list is global rather than scoped
per need type: the qik document-maturity states, and the issue-lifecycle
states this project's imported ``risk``/``problem``/``change`` types use.

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Status
     - Meaning
   * - ``none``
     - No status has been set yet.
   * - ``draft``
     - Drafted, not yet reviewed.
   * - ``proposed``
     - Reviewed and proposed for approval.
   * - ``approved``
     - Approved; considered ready to implement against.
   * - ``released``
     - Released as part of a baselined revision.
   * - ``deprecated``
     - Superseded; kept for traceability, no longer to be implemented
       against.
   * - ``retired``
     - No longer applicable; retained for historical record only.
   * - ``open``
     - Issue-register entry (risk/problem/change) still
       active/unresolved.
   * - ``closed``
     - Issue-register entry closed without a recorded resolution outcome.
   * - ``resolved``
     - Issue-register entry closed with a recorded resolution outcome.

Only ``draft``, ``approved``, and ``open`` are actually in use today (70,
35, and 1 real occurrences respectively) — the rest of the list exists so
a future status change doesn't require a ``conf.py`` edit, not because
those states are already exercised. ``open`` is kept distinct from
``draft`` deliberately: it describes whether a register entry is still
active, not whether its text has been reviewed.

``:version:`` (``needs_fields``) now carries ``1.0.0`` on every native
requirement-shaped need in this project (``sys``/``feat``/``comp``/
``unit``/``sg``/``fsr``/``tsr``/``eng_need``/``safefeat``/``rec``/``res``/
``tc``/``itc``) — a content baseline version, distinct from the pinned
tool-version meaning the same field already had for the external ``tool``
type. Deliberately not added to the imported ``risk``/``problem``/
``change``/``exception``/``infra`` types, or to ``tool`` (which already
uses ``version`` for something else) — see the field's description in
``conf.py`` for the exact split.

Safety and cybersecurity classification
-------------------------------------------

``asil`` (ISO 26262 Automotive Safety Integrity Level) and ``cal``
(ISO/SAE 21434 Cybersecurity Assurance Level) are registered in
``needs_fields``, both nullable, both **populated only where a real
HARA or TARA outcome exists** — not stamped across every need of a
given type.

``asil`` is set today on exactly six needs — the determined safety
chain and what it links into:

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Need
     - ASIL
     - Why
   * - ``sg_001``
     - ``ASIL B``
     - The Safety Goal itself — HARA output.
   * - ``fsr_001``
     - ``ASIL B``
     - Functional Safety Concept, inherits from ``sg_001``.
   * - ``tsr_001``
     - ``ASIL B``
     - Technical Safety Concept, inherits from ``fsr_001``.
   * - ``comp_a_001``
     - ``ASIL B``
     - Architecture ``tsr_001`` is allocated to.
   * - ``tc_unit_a_001``
     - ``ASIL B``
     - Verifies ``unit_com_evttrig_019``.
   * - ``itc_comp_a_001_001``
     - ``ASIL B``
     - Verifies ``comp_a_001``.

.. note::
   **2026-08-22:** this table previously had a seventh row,
   ``UNIT_A_001`` (``ASIL B``, "design implementing that architecture"),
   with ``tc_unit_a_001`` listed as verifying it. ``UNIT_A_001`` doesn't
   exist anywhere in this project (retired 2026-08-21 — see
   ``component/unit test/test cases/index.rst``'s own history note) and
   never actually carried an ``:asil:`` field itself, so "seven" was
   already wrong before that row is even removed. ``tc_unit_a_001`` now
   verifies ``unit_com_evttrig_019`` (corrected above) — but that unit
   has no ``:asil:`` of its own and satisfies ``comp_com_evttrig_001``,
   not ``comp_a_001``. So the ASIL-B chain currently ends at
   ``comp_a_001``/``itc_comp_a_001_001`` (component level) plus
   ``tc_unit_a_001`` (which self-declares ``ASIL B`` on the test case
   itself) — there is no unit-level design need in this chain carrying
   an ``:asil:`` value right now. Disclosed here as a real gap, not
   asserted or silently patched.

Diagnostics (``comp_z_001``/``unit_z_001``/their test cases) is
deliberately **not** given an ASIL: ``safety/analyses/
dependent-failure-analysis.rst`` records Diagnostics as "not yet
assessed." Setting an ASIL there would assert a HARA outcome that
hasn't happened. The same discipline applies to every other need type
(``eng_need``, the external ``org_req``/``risk``/``problem``/
``change``/``tool``/etc.) — none of them are safety requirements, and
none carry an ``asil`` value.

``cal`` is registered but **populated nowhere yet**: ``needs/
security/tara/index.rst`` is an explicit empty stub ("Nothing
captured yet") — there is no TARA-derived cybersecurity goal in this
project for a CAL to attach to. The field exists so it's ready the
moment ``cyber_req``/``threat`` need types are added (see that file's
own "Pending" list) and a real TARA produces one; putting ``CAL 3`` on
an organizational Clause 5 requirement in the meantime would misrepresent
an org policy as a TARA-derived cybersecurity goal, which it isn't.

Where the ID format comes from
---------------------------------

``needs_id_regex = r"^[A-Z]+_[A-Za-z0-9_]+"`` enforces the
``PREFIX_rest`` shape for every need ID in this project — the same shape
each prefix column above defines per type. ``needs_id_required = True``
and ``needs_report_dead_links = True`` mean a missing ID, or a
``:links:``/named-link field pointing at an ID that doesn't exist, fails
the build (``-W``) rather than just warning.

Not this project's types
---------------------------

The root project (one level up) is a **separate** Sphinx project with its
own ``conf.py`` and its own single need type (``org_req``) — see
``../needs_types_definition.rst``, built independently from the repo
root. See ``../STANDARDS.md`` for the full folder-to-standard crosswalk
across both projects.
