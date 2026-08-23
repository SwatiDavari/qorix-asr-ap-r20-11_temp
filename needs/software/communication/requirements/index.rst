Communication Module — Feature Requirements
===========================================

.. note::
   Imported from the eclipse-score reference (``eclipse-score/score``,
   ``docs/features/communication/``) supplied for this conversion, covering
   the top-level Communication feature plus its two sub-features (IPC,
   SOME/IP Gateway). All 58 source requirements are converted below
   1:1 as individual ``.. feat::`` needs (qorix-asr-ap-r20-11_temp has no ``feat_req``
   directive — feature-level requirement text is a ``feat::`` here, per
   ``feature/index.rst``'s existing ``feat_a_001`` example).

   Field mapping from the source, and why:

   - ``:status:`` — source status is uniformly ``valid`` (S-CORE's own
     review state). ``valid`` is not in this project's ``needs_statuses``
     vocabulary. Mapped to ``draft``: this is freshly imported reference
     material that has not been through *this* project's own review —
     using ``approved`` or ``proposed`` would overstate that.
   - ``:satisfies:`` — set to ``sys_msgdisc_001`` (the existing system requirement
     covering both messaging and service discovery), matching the pattern
     already used by ``feat_a_001``. The source's own richer
     ``:derived_from:`` chain into external S-CORE stakeholder
     requirements (``stkh_req__*``) isn't reproduced — those needs don't
     exist in this repo.
   - ``:derives_from:`` — carries the source need ID and the source's own
     ``safety``/``security``/``reqtype`` classification as free text,
     for provenance. Deliberately **not** written into this project's
     ``:asil:`` field: per ``needs/needs_types_definition.rst``, ``asil``
     is populated only where a real HARA outcome exists in *this*
     project, and no HARA has been performed for these imported
     requirements individually (only ``sg_001``/``fsr_001``/``tsr_001``
     and the chain they cover have one). Stamping ``ASIL_B`` here from
     the source's classification would assert a HARA outcome that
     didn't happen in this project.
   - Count correction: the project's own
     ``eclipse_score_communication_traceability_reference.md`` recorded
     47 top-level Communication requirements (24 ASIL_B / 23 QM); the
     source file actually defines 49 (re-counted directly from the
     ``.. feat_req::`` directives during this conversion). Fixed here.

Communication (top-level feature)
---------------------------------

.. feat:: Support for Time-based Architecture
   :id: feat_com_arch_001
   :version: 1.0.0
   :status: draft
   :satisfies: sys_msgdisc_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3
   :derives_from: eclipse-score/score docs/features/communication -- feat_req__com__time_based_arch (reqtype: Functional, source safety: ASIL_B, source security: NO)

   The communication framework shall provide API to support a time-based architecture.

.. feat:: Support for Data-driven Architecture
   :id: feat_com_arch_002
   :version: 1.0.0
   :status: draft
   :satisfies: sys_msgdisc_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3
   :derives_from: eclipse-score/score docs/features/communication -- feat_req__com__data_driven_arch (reqtype: Functional, source safety: QM, source security: NO)

   The communication framework shall provide API to support a data-driven architecture.

.. feat:: Support for Request-driven Architecture
   :id: feat_com_arch_003
   :version: 1.0.0
   :status: draft
   :satisfies: sys_msgdisc_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3
   :derives_from: eclipse-score/score docs/features/communication -- feat_req__com__request_driven_arch (reqtype: Functional, source safety: QM, source security: NO)

   The communication framework shall provide API to support a request-driven architecture.

.. feat:: Communication Interfaces
   :id: feat_com_ifc_001
   :version: 1.0.0
   :status: draft
   :satisfies: sys_msgdisc_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3
   :derives_from: eclipse-score/score docs/features/communication -- feat_req__com__interfaces (reqtype: Functional, source safety: ASIL_B, source security: NO)

   A communication interface consists of a combination of any number of the following elements:

      - Event-Types
      - Methods
      - Signals

.. feat:: Event Type
   :id: feat_com_ifc_002
   :version: 1.0.0
   :status: draft
   :satisfies: sys_msgdisc_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3
   :derives_from: eclipse-score/score docs/features/communication -- feat_req__com__event_type (reqtype: Functional, source safety: ASIL_B, source security: NO)

   An event-type is part of a communication interface and has:

      - a name
      - a data type

      The producer can assign a value to it. Consumers can subscribe to value-changed events of the element or poll unseen, cached events.

.. feat:: Method
   :id: feat_com_ifc_003
   :version: 1.0.0
   :status: draft
   :satisfies: sys_msgdisc_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3
   :derives_from: eclipse-score/score docs/features/communication -- feat_req__com__method (reqtype: Functional, source safety: ASIL_B, source security: NO)

   A method is part of a communication interface and has:

      - a name
      - a specified application routine with a given set of parameters and a return type

      When a communication partner issues a call to the method with the required parameters:

      #. it shall invoke the application routine with the provided parameters, and
      #. return its result to the communication partner

      A method call shall be possible both synchronously and asynchronously.

.. feat:: Signal
   :id: feat_com_ifc_004
   :version: 1.0.0
   :status: draft
   :satisfies: sys_msgdisc_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3
   :derives_from: eclipse-score/score docs/features/communication -- feat_req__com__signal (reqtype: Functional, source safety: QM, source security: NO)

   A signal is part of a communication interface and has:

      - a name

      A client can trigger the signal. The service instance offering the trigger can:

      - wait for the signal to be triggered
      - check if the signal was triggered

.. feat:: Producer-Consumer Pattern
   :id: feat_com_ifc_005
   :version: 1.0.0
   :status: draft
   :satisfies: sys_msgdisc_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3
   :derives_from: eclipse-score/score docs/features/communication -- feat_req__com__producer_consumer (reqtype: Functional, source safety: ASIL_B, source security: NO)

   Communication shall be cached based on the producer-consumer pattern.

.. feat:: Service Instance
   :id: feat_com_ifc_006
   :version: 1.0.0
   :status: draft
   :satisfies: sys_msgdisc_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3
   :derives_from: eclipse-score/score docs/features/communication -- feat_req__com__service_instance (reqtype: Functional, source safety: ASIL_B, source security: NO)

   Multiple service instances shall be able to offer the same interface.

.. feat:: Service Instance Names
   :id: feat_com_ifc_007
   :version: 1.0.0
   :status: draft
   :satisfies: sys_msgdisc_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3
   :derives_from: eclipse-score/score docs/features/communication -- feat_req__com__service_instance_names (reqtype: Functional, source safety: ASIL_B, source security: NO)

   A service instance is offered under one or more unique names by which it can be discovered. Names follow a POSIX path style.

.. feat:: Versioning
   :id: feat_com_ifc_008
   :version: 1.0.0
   :status: draft
   :satisfies: sys_msgdisc_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3
   :derives_from: eclipse-score/score docs/features/communication -- feat_req__com__versioning (reqtype: Functional, source safety: ASIL_B, source security: NO)

   The communication framework shall support versioning of service instances:

      - Version information of a service instance is binding-specific.
      - Version information is provided in the deployment configuration.

.. feat:: Service location transparency
   :id: feat_com_ifc_009
   :version: 1.0.0
   :status: draft
   :satisfies: sys_msgdisc_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3
   :derives_from: eclipse-score/score docs/features/communication -- feat_req__com__service_location_transparency (reqtype: Functional, source safety: ASIL_B, source security: NO)

   The interface to access service instances is agnostic to the binding used to communicate with the service.

.. feat:: Stateless communication
   :id: feat_com_ifc_010
   :version: 1.0.0
   :status: draft
   :satisfies: sys_msgdisc_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3
   :derives_from: eclipse-score/score docs/features/communication -- feat_req__com__stateless_communication (reqtype: Functional, source safety: ASIL_B, source security: NO)

   The communication framework shall support stateless communication.

.. feat:: Service instance granularity
   :id: feat_com_ifc_011
   :version: 1.0.0
   :status: draft
   :satisfies: sys_msgdisc_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3
   :derives_from: eclipse-score/score docs/features/communication -- feat_req__com__service_instance_granularity (reqtype: Functional, source safety: ASIL_B, source security: NO)

   The communication framework shall support multiple service instances per software architecture element.

.. feat:: Service discovery
   :id: feat_com_ifc_012
   :version: 1.0.0
   :status: draft
   :satisfies: sys_msgdisc_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3
   :derives_from: eclipse-score/score docs/features/communication -- feat_req__com__service_discovery (reqtype: Functional, source safety: ASIL_B, source security: NO)

   The communication framework shall provide service discovery to find available services during runtime. Service discovery shall consider version compatibility. Service discovery shall be handled implicitly (where possible).

Mixed-Criticality safety systems
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. feat:: Safe communication over criticality levels
   :id: feat_com_safety_001
   :version: 1.0.0
   :status: draft
   :satisfies: sys_msgdisc_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3
   :derives_from: eclipse-score/score docs/features/communication -- feat_req__com__safe_communication (reqtype: Functional, source safety: ASIL_B, source security: YES)

   The communication framework shall support safe communication involving communication partners on the same or multiple criticality levels.

.. feat:: Data Corruption
   :id: feat_com_safety_002
   :version: 1.0.0
   :status: draft
   :satisfies: sys_msgdisc_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3
   :derives_from: eclipse-score/score docs/features/communication -- feat_req__com__data_corruption (reqtype: Functional, source safety: ASIL_B, source security: YES)

   Consumers with lower criticality shall not be able to corrupt data consumed by partners with higher criticality.

.. feat:: Data Reordering
   :id: feat_com_safety_003
   :version: 1.0.0
   :status: draft
   :satisfies: sys_msgdisc_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3
   :derives_from: eclipse-score/score docs/features/communication -- feat_req__com__data_reordering (reqtype: Functional, source safety: ASIL_B, source security: YES)

   Consumers with lower criticality shall not be able to modify the order of data consumed by partners with higher criticality.

.. feat:: Data Repetition
   :id: feat_com_safety_004
   :version: 1.0.0
   :status: draft
   :satisfies: sys_msgdisc_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3
   :derives_from: eclipse-score/score docs/features/communication -- feat_req__com__data_repetition (reqtype: Functional, source safety: ASIL_B, source security: YES)

   Consumers with lower criticality shall not be able to duplicate data consumed by other communication partners with higher criticality.

.. feat:: Data Loss
   :id: feat_com_safety_005
   :version: 1.0.0
   :status: draft
   :satisfies: sys_msgdisc_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3
   :derives_from: eclipse-score/score docs/features/communication -- feat_req__com__data_loss (reqtype: Functional, source safety: ASIL_B, source security: YES)

   Consumers with lower criticality shall not be able to drop data before it is consumed by partners with higher criticality.

Performance
^^^^^^^^^^^

.. feat:: Zero-Copy Approach
   :id: feat_com_perf_001
   :version: 1.0.0
   :status: draft
   :satisfies: sys_msgdisc_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3
   :derives_from: eclipse-score/score docs/features/communication -- feat_req__com__zero_copy (reqtype: Functional, source safety: QM, source security: NO)

   The communication framework shall enable Zero-Copy communication without copying to-be-transferred data.

User friendly API for information exchange
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. feat:: Support for multiple programming languages
   :id: feat_com_binding_001
   :version: 1.0.0
   :status: draft
   :satisfies: sys_msgdisc_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3
   :derives_from: eclipse-score/score docs/features/communication -- feat_req__com__multi_lang (reqtype: Non-Functional, source safety: QM, source security: NO)

   The communication framework shall provide a public API for each supported programming language of S-CORE.

.. feat:: Support for programming language idioms
   :id: feat_com_binding_002
   :version: 1.0.0
   :status: draft
   :satisfies: sys_msgdisc_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3
   :derives_from: eclipse-score/score docs/features/communication -- feat_req__com__lang_idioms (reqtype: Non-Functional, source safety: QM, source security: NO)

   Each public API shall support the idioms of the programming language it is written in.

.. feat:: Use programming language infrastructure
   :id: feat_com_binding_003
   :version: 1.0.0
   :status: draft
   :satisfies: sys_msgdisc_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3
   :derives_from: eclipse-score/score docs/features/communication -- feat_req__com__lang_infra (reqtype: Non-Functional, source safety: QM, source security: NO)

   Each public API shall use core infrastructure of its programming language and accompanying standard libraries, whenever possible and meaningful.

Full testability for the user facing API
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. feat:: Fully mockable public API
   :id: feat_com_binding_004
   :version: 1.0.0
   :status: draft
   :satisfies: sys_msgdisc_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3
   :derives_from: eclipse-score/score docs/features/communication -- feat_req__com__testability_mock_api (reqtype: Non-Functional, source safety: QM, source security: NO)

   The public API shall be fully mockable.

.. feat:: Fake binding
   :id: feat_com_binding_005
   :version: 1.0.0
   :status: draft
   :satisfies: sys_msgdisc_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3
   :derives_from: eclipse-score/score docs/features/communication -- feat_req__com__testability_fake_binding (reqtype: Non-Functional, source safety: QM, source security: NO)

   The communication framework shall provide a fake binding.

Multi-binding support
^^^^^^^^^^^^^^^^^^^^^

.. feat:: Multi-binding support
   :id: feat_com_binding_006
   :version: 1.0.0
   :status: draft
   :satisfies: sys_msgdisc_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3
   :derives_from: eclipse-score/score docs/features/communication -- feat_req__com__multi_binding_support (reqtype: Functional, source safety: QM, source security: NO)

   The communication framework shall support multiple bindings.

.. feat:: Binding-agnostic public API
   :id: feat_com_binding_007
   :version: 1.0.0
   :status: draft
   :satisfies: sys_msgdisc_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3
   :derives_from: eclipse-score/score docs/features/communication -- feat_req__com__binding_agnostic_api (reqtype: Functional, source safety: QM, source security: NO)

   The public API of the communication framework shall be binding-agnostic.

.. feat:: Multi-binding deployment configuration
   :id: feat_com_binding_008
   :version: 1.0.0
   :status: draft
   :satisfies: sys_msgdisc_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3
   :derives_from: eclipse-score/score docs/features/communication -- feat_req__com__multi_binding_depl (reqtype: Functional, source safety: ASIL_B, source security: NO)

   The association of a service instance and the appropriate binding shall be specified in the deployment configuration.

Cross-VM Extensions
^^^^^^^^^^^^^^^^^^^

.. feat:: One-way data sharing into a VM
   :id: feat_com_vm_001
   :version: 1.0.0
   :status: draft
   :satisfies: sys_msgdisc_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3
   :derives_from: eclipse-score/score docs/features/communication -- feat_req__com__one_way_sharing (reqtype: Functional, source safety: QM, source security: NO)

   The system shall support one-way data sharing into a Virtual Machine (VM) for vehicle state read-only for the VM (snapshot state).

.. feat:: Read-only access for VM
   :id: feat_com_vm_002
   :version: 1.0.0
   :status: draft
   :satisfies: sys_msgdisc_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3
   :derives_from: eclipse-score/score docs/features/communication -- feat_req__com__readonly_vm (reqtype: Functional, source safety: QM, source security: NO)

   The consumer (VM) shall have read-only access to the shared data.

.. feat:: Consistent data-sets
   :id: feat_com_perf_002
   :version: 1.0.0
   :status: draft
   :satisfies: sys_msgdisc_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3
   :derives_from: eclipse-score/score docs/features/communication -- feat_req__com__consistent_data (reqtype: Functional, source safety: QM, source security: NO)

   The system shall support consistent data-sets, allowing the consumer to obtain a consistent version of related data items.

.. feat:: Lock-free access
   :id: feat_com_perf_003
   :version: 1.0.0
   :status: draft
   :satisfies: sys_msgdisc_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3
   :derives_from: eclipse-score/score docs/features/communication -- feat_req__com__lock_free_access (reqtype: Functional, source safety: QM, source security: NO)

   Consistent access to data must be lock-free.

.. feat:: Producer time stamps
   :id: feat_com_perf_004
   :version: 1.0.0
   :status: draft
   :satisfies: sys_msgdisc_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3
   :derives_from: eclipse-score/score docs/features/communication -- feat_req__com__producer_timestamps (reqtype: Functional, source safety: QM, source security: NO)

   Producer time stamps shall be available for related data-sets.

.. feat:: Streamed data based on shared queues
   :id: feat_com_perf_005
   :version: 1.0.0
   :status: draft
   :satisfies: sys_msgdisc_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3
   :derives_from: eclipse-score/score docs/features/communication -- feat_req__com__streamed_data (reqtype: Functional, source safety: QM, source security: NO)

   The system shall support streamed data based on shared queues (stream of events or data).

.. feat:: Configurable queues
   :id: feat_com_perf_006
   :version: 1.0.0
   :status: draft
   :satisfies: sys_msgdisc_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3
   :derives_from: eclipse-score/score docs/features/communication -- feat_req__com__configurable_queues (reqtype: Functional, source safety: QM, source security: NO)

   Queues shall be configurable by the client (VM), including the number of elements and buffer allocation.

.. feat:: Lock-free queue access
   :id: feat_com_perf_007
   :version: 1.0.0
   :status: draft
   :satisfies: sys_msgdisc_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3
   :derives_from: eclipse-score/score docs/features/communication -- feat_req__com__lock_free_queue (reqtype: Functional, source safety: QM, source security: NO)

   Queues shall support lock-free access to data elements.

.. feat:: Bi-directional communication
   :id: feat_com_perf_008
   :version: 1.0.0
   :status: draft
   :satisfies: sys_msgdisc_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3
   :derives_from: eclipse-score/score docs/features/communication -- feat_req__com__bi_directional_comm (reqtype: Functional, source safety: QM, source security: NO)

   The system shall support bi-directional communication via writable data elements by the client.

.. feat:: Asynchronous support
   :id: feat_com_perf_009
   :version: 1.0.0
   :status: draft
   :satisfies: sys_msgdisc_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3
   :derives_from: eclipse-score/score docs/features/communication -- feat_req__com__async_support (reqtype: Functional, source safety: QM, source security: NO)

   The system shall provide asynchronous bi-directional support via multiple queues.

.. feat:: Shared memory chunks
   :id: feat_com_perf_010
   :version: 1.0.0
   :status: draft
   :satisfies: sys_msgdisc_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3
   :derives_from: eclipse-score/score docs/features/communication -- feat_req__com__shared_memory (reqtype: Functional, source safety: QM, source security: NO)

   The system shall support multiple chunks of shared memory to allow required access control.

.. feat:: Data update notifications
   :id: feat_com_perf_011
   :version: 1.0.0
   :status: draft
   :satisfies: sys_msgdisc_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3
   :derives_from: eclipse-score/score docs/features/communication -- feat_req__com__data_notifications (reqtype: Functional, source safety: QM, source security: NO)

   Notifications for data updates shall be available (virtual IRQs in a VM).

.. feat:: Configurable notifications
   :id: feat_com_perf_012
   :version: 1.0.0
   :status: draft
   :satisfies: sys_msgdisc_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3
   :derives_from: eclipse-score/score docs/features/communication -- feat_req__com__config_notifications (reqtype: Functional, source safety: QM, source security: NO)

   Notifications shall be configurable by consumers of data (using flags or watermarks in shared memory from client to producer).

Dynamic deployment at runtime
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. feat:: Deployment configuration at runtime
   :id: feat_com_deploy_001
   :version: 1.0.0
   :status: draft
   :satisfies: sys_msgdisc_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3
   :derives_from: eclipse-score/score docs/features/communication -- feat_req__com__depl_config_runtime (reqtype: Functional, source safety: ASIL_B, source security: YES)

   Deployment configuration shall be read from an integrity-checked configuration file at runtime.

Tracing
^^^^^^^

.. feat:: Support for Tracing
   :id: feat_com_trace_001
   :version: 1.0.0
   :status: draft
   :satisfies: sys_msgdisc_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3
   :derives_from: eclipse-score/score docs/features/communication -- feat_req__com__tracing (reqtype: Functional, source safety: ASIL_B, source security: NO)

   The communication framework shall provide infrastructure to enable binding-agnostic, zero-copy, read-only tracing of communication.

Security Impact
^^^^^^^^^^^^^^^

.. feat:: Access Control List Placement
   :id: feat_com_acl_001
   :version: 1.0.0
   :status: draft
   :satisfies: sys_msgdisc_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3
   :derives_from: eclipse-score/score docs/features/communication -- feat_req__com__acl_placement (reqtype: Functional, source safety: QM, source security: YES)

   The communication framework shall support an Access Control Lists in the deployment configuration.

.. feat:: Access Control List per service instance
   :id: feat_com_acl_002
   :version: 1.0.0
   :status: draft
   :satisfies: sys_msgdisc_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3
   :derives_from: eclipse-score/score docs/features/communication -- feat_req__com__acl_per_service_instance (reqtype: Functional, source safety: QM, source security: YES)

   The communication framework shall support an Access Control List per service instance.

.. feat:: Access Control List for producer
   :id: feat_com_acl_003
   :version: 1.0.0
   :status: draft
   :satisfies: sys_msgdisc_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3
   :derives_from: eclipse-score/score docs/features/communication -- feat_req__com__acl_for_producer (reqtype: Functional, source safety: QM, source security: YES)

   The communication framework shall support an Access Control List for the communication partner offering a service instance (producer). An entry in the ACL corresponds to an allowed consumer.

.. feat:: Access Control List for consumer
   :id: feat_com_acl_004
   :version: 1.0.0
   :status: draft
   :satisfies: sys_msgdisc_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3
   :derives_from: eclipse-score/score docs/features/communication -- feat_req__com__acl_for_consumer (reqtype: Functional, source safety: QM, source security: YES)

   The communication framework shall support an Access Control List for the communication partner consuming a service instance. An entry in the ACL corresponds to an allowed producer.

Safety Impact
^^^^^^^^^^^^^

.. feat:: Communication ASIL level
   :id: feat_com_safety_006
   :version: 1.0.0
   :status: draft
   :satisfies: sys_msgdisc_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3
   :derives_from: eclipse-score/score docs/features/communication -- feat_req__com__asil (reqtype: Functional, source safety: ASIL_B, source security: YES)

   The communication framework shall support safe communication up to ASIL-B.

IPC (sub-feature)
-----------------

.. note::
   Source: ``ipc/requirements/index.rst``. All 4 are ``satisfied_by``
   the same single architecture element as the top-level Communication
   requirements in the source (no IPC-specific architecture satisfies
   them) — see ``component/index.rst``'s note on ``comp_a_001``.

.. feat:: Zero-Copy Approach (IPC)
   :id: feat_com_ipc_001
   :version: 1.0.0
   :status: draft
   :satisfies: sys_msgdisc_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3
   :derives_from: eclipse-score/score docs/features/communication -- feat_req__ipc__zero_copy (reqtype: Functional, source safety: QM, source security: NO)

   IPC communication shall be possible without copying to-be-transferred data.

.. feat:: IPC Confidentiality
   :id: feat_com_ipc_002
   :version: 1.0.0
   :status: draft
   :satisfies: sys_msgdisc_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3
   :derives_from: eclipse-score/score docs/features/communication -- feat_req__ipc__confidentiality (reqtype: Functional, source safety: QM, source security: YES)

   The IPC binding shall ensure confidentiality of its communication.

.. feat:: IPC Integrity
   :id: feat_com_ipc_003
   :version: 1.0.0
   :status: draft
   :satisfies: sys_msgdisc_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3
   :derives_from: eclipse-score/score docs/features/communication -- feat_req__ipc__integrity (reqtype: Functional, source safety: QM, source security: YES)

   The IPC binding shall ensure integrity of its communication.

.. feat:: IPC Availability
   :id: feat_com_ipc_004
   :version: 1.0.0
   :status: draft
   :satisfies: sys_msgdisc_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3
   :derives_from: eclipse-score/score docs/features/communication -- feat_req__ipc__availability (reqtype: Functional, source safety: QM, source security: YES)

   The IPC binding shall ensure availability of its communication, so that the availability is independent per criticality level.

SOME/IP Gateway (sub-feature)
-----------------------------

.. note::
   Source: ``some_ip_gateway/requirements/index.rst``. Like IPC, all 5
   are ``satisfied_by`` the top-level Communication architecture element
   in the source — the source itself has no SOME/IP-Gateway-specific
   architecture need at all (flagged as a gap in the source's own
   architecture and service-discovery pages, which define no need IDs).

.. feat:: Plug-In-IFC for SOME/IP protocol stacks
   :id: feat_com_someip_001
   :version: 1.0.0
   :status: draft
   :satisfies: sys_msgdisc_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3
   :derives_from: eclipse-score/score docs/features/communication -- feat_req__some_ip_gateway__stack_plugin_ifc (reqtype: Functional, source safety: QM, source security: NO)

   The SOME/IP Gateway shall support an interface to plug-in a SOME/IP stack implementation.

.. feat:: Plug-In-IFC for End-to-End protection modules
   :id: feat_com_someip_002
   :version: 1.0.0
   :status: draft
   :satisfies: sys_msgdisc_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3
   :derives_from: eclipse-score/score docs/features/communication -- feat_req__some_ip_gateway__e2e_plugin_ifc (reqtype: Functional, source safety: ASIL_B, source security: NO)

   The SOME/IP Gateway shall support an interface to plug-in a E2E protection service implementation.

.. feat:: Compatibility with Open SOME/IP Protocol Specification
   :id: feat_com_someip_003
   :version: 1.0.0
   :status: draft
   :satisfies: sys_msgdisc_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3
   :derives_from: eclipse-score/score docs/features/communication -- feat_req__some_ip_gateway__someip_protocol (reqtype: Functional, source safety: ASIL_B, source security: NO)

   The SOME/IP protocol implementation shall be fully compatible and complying with the SOME/IP protocol specification from Open SOME/IP.

.. feat:: Compatibility with some-ip.com E2E Protocol Specification
   :id: feat_com_someip_004
   :version: 1.0.0
   :status: draft
   :satisfies: sys_msgdisc_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3
   :derives_from: eclipse-score/score docs/features/communication -- feat_req__some_ip_gateway__e2e_specs (reqtype: Functional, source safety: ASIL_B, source security: NO)

   The E2E protection implementation shall be fully compatible and complying with the E2E protocol specification from some-ip.com.

.. feat:: Compatibility with Open SOME/IP Service Discovery Protocol Specification
   :id: feat_com_someip_005
   :version: 1.0.0
   :status: draft
   :satisfies: sys_msgdisc_001
   :standard: ASPICE SWE.1 / ISO 15288 6.4.3
   :derives_from: eclipse-score/score docs/features/communication -- feat_req__some_ip_gateway__someip_sd_protocol (reqtype: Functional, source safety: ASIL_B, source security: NO)

   The Service Discovery implementation shall be fully compatible and complying with the SOME/IP service discovery specification from Open SOME/IP.
