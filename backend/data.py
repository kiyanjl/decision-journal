SEED_REQUIREMENTS_BASELINES = [
    {
        "baseline_id": "BASELINE-2026-Q2-v1",
        "baseline_name": "Q2 2026 Core Requirements",
        "version": "1.0.0",
        "requirements": [
            {"req_id": "REQ-01", "req_version": "1.0", "name": "User Authentication", "description": "System must authenticate users via OAuth2",
                "status": "active", "test_file": "tests/auth/test_oauth.py", "doc_file": "docs/requirements/REQ-01-v1.0.md"},
            {"req_id": "REQ-02", "req_version": "1.0", "name": "Data Encryption", "description": "All data at rest must be encrypted with AES-256",
                "status": "active", "test_file": "tests/security/test_encryption.py", "doc_file": "docs/requirements/REQ-02-v1.0.md"},
            {"req_id": "REQ-03", "req_version": "1.0", "name": "API Rate Limiting", "description": "API requests limited to 1000/minute per user",
                "status": "active", "test_file": "tests/api/test_rate_limit.py", "doc_file": "docs/requirements/REQ-03-v1.0.md"},
            {"req_id": "REQ-06", "req_version": "1.0", "name": "User Profile Module", "description": "Basic user profile CRUD operations",
                "status": "active", "test_file": "tests/profile/test_profile.py", "doc_file": "docs/requirements/REQ-06-v1.0.md"}
        ],
        "status": "archived",
        "created_at": "2026-04-01T00:00:00",
        "superseded_by": "BASELINE-2026-Q2-v2"
    },
    {
        "baseline_id": "BASELINE-2026-Q2-v2",
        "baseline_name": "Q2 2026 Core Requirements (Updated)",
        "version": "2.0.0",
        "requirements": [
            {"req_id": "REQ-01", "req_version": "1.1", "name": "User Authentication", "description": "System must authenticate users via OAuth2 + MFA", "status": "active",
                "test_file": "tests/auth/test_oauth_mfa.py", "doc_file": "docs/requirements/REQ-01-v1.1.md", "change_reason": "Security audit required MFA addition"},
            {"req_id": "REQ-02", "req_version": "1.0", "name": "Data Encryption", "description": "All data at rest must be encrypted with AES-256",
                "status": "active", "test_file": "tests/security/test_encryption.py", "doc_file": "docs/requirements/REQ-02-v1.0.md"},
            {"req_id": "REQ-03", "req_version": "1.1", "name": "API Rate Limiting",
                "description": "API requests limited to 500/minute per user (reduced for security)", "status": "active", "test_file": "tests/api/test_rate_limit_v2.py", "doc_file": "docs/requirements/REQ-03-v1.1.md", "change_reason": "DDoS mitigation requirement"},
            {"req_id": "REQ-04", "req_version": "1.0", "name": "Audit Logging", "description": "All admin actions must be logged immutably",
                "status": "active", "test_file": "tests/audit/test_logging.py", "doc_file": "docs/requirements/REQ-04-v1.0.md"},
            {"req_id": "REQ-06", "req_version": "1.1", "name": "User Profile Module", "description": "Enhanced profile with privacy settings", "status": "active",
                "test_file": "tests/profile/test_profile_v2.py", "doc_file": "docs/requirements/REQ-06-v1.1.md", "change_reason": "GDPR compliance update"},
            {"req_id": "REQ-07", "req_version": "1.0", "name": "Email Notifications", "description": "System sends transactional emails via SMTP",
                "status": "active", "test_file": "tests/email/test_smtp.py", "doc_file": "docs/requirements/REQ-07-v1.0.md"}
        ],
        "status": "active",
        "created_at": "2026-04-15T00:00:00",
        "superseded_by": None
    },
    {
        "baseline_id": "BASELINE-2026-Q3-v1",
        "baseline_name": "Q3 2026 Preview Requirements",
        "version": "1.0.0",
        "requirements": [
            {"req_id": "REQ-05", "req_version": "1.0", "name": "Machine Learning Pipeline", "description": "Integration with ML models for prediction",
                "status": "draft", "test_file": "tests/ml/test_pipeline.py", "doc_file": "docs/requirements/REQ-05-v1.0.md"},
            {"req_id": "REQ-08", "req_version": "1.0", "name": "Real-time Analytics", "description": "WebSocket-based real-time data streaming",
                "status": "draft", "test_file": "tests/analytics/test_websocket.py", "doc_file": "docs/requirements/REQ-08-v1.0.md"},
            {"req_id": "REQ-09", "req_version": "1.0", "name": "Mobile App API", "description": "REST endpoints optimized for mobile clients",
                "status": "draft", "test_file": "tests/mobile/test_api.py", "doc_file": "docs/requirements/REQ-09-v1.0.md"}
        ],
        "status": "draft",
        "created_at": "2026-05-01T00:00:00",
        "superseded_by": None
    }
]

SEED_DECISIONS = [
    # v1.0.0 decisions
    {"decision_id": "DEC-2026-000", "brief_description": "Initial system architecture approval", "object_affected": "document", "previous_state": "Draft architecture", "new_state": "Approved baseline", "trigger_event": "Architecture review meeting", "reasoning": "Microservices architecture approved for scalability and team autonomy.",
        "proposed_by": "Chief Architect G", "approved_by": "CTO - Maria Rossi", "source_evidence": ["file:docs/architecture/ADR-001.md", "email:arch-review-2026-03-15@company.com"], "timestamp": "2026-03-20T10:00:00", "status": "approved", "version": "v1.0.0", "baseline_id": "BASELINE-2026-Q2-v1"},
    {"decision_id": "DEC-2026-000A", "brief_description": "Approve OAuth2 as authentication standard", "object_affected": "requirement", "previous_state": "No auth standard", "new_state": "REQ-01 v1.0 - OAuth2", "trigger_event": "Security standards committee", "reasoning": "OAuth2 is industry standard and supports SSO integration with corporate identity provider.",
        "proposed_by": "Security Engineer H", "approved_by": "CTO - Maria Rossi", "source_evidence": ["file:docs/security/auth-standards.pdf", "pr:https://github.com/company/repo/pull/200"], "timestamp": "2026-03-25T14:00:00", "status": "approved", "version": "v1.0.0", "baseline_id": "BASELINE-2026-Q2-v1"},

    # v1.1.0 decisions
    {"decision_id": "DEC-2026-000B", "brief_description": "Add user profile module to v1.1.0 scope", "object_affected": "release", "previous_state": "Not in scope", "new_state": "REQ-06 v1.0 - In scope", "trigger_event": "Product roadmap update Q2", "reasoning": "Customer feedback strongly requested profile management. Low risk addition with existing patterns.",
        "proposed_by": "Product Manager E", "approved_by": "Manager Y", "source_evidence": ["email:roadmap-update-2026-04-02@company.com", "file:docs/roadmap/Q2-2026.pdf"], "timestamp": "2026-04-05T09:30:00", "status": "approved", "version": "v1.1.0", "baseline_id": "BASELINE-2026-Q2-v1"},
    {"decision_id": "DEC-2026-000C", "brief_description": "Delay data encryption enhancement to v1.2.0", "object_affected": "requirement", "previous_state": "REQ-02 v1.1 - Planned", "new_state": "REQ-02 v1.0 - Maintained", "trigger_event": "Resource constraint mid-sprint", "reasoning": "Team capacity insufficient for encryption enhancement. Current AES-256 meets compliance. Enhancement postponed.",
        "proposed_by": "Engineering Lead I", "approved_by": "Manager Y", "source_evidence": ["email:capacity-planning-2026-04-08@company.com", "message:slack:#eng-leads"], "timestamp": "2026-04-09T11:00:00", "status": "superseded", "version": "v1.1.0", "baseline_id": "BASELINE-2026-Q2-v1"},

    # v1.2.0 decisions
    {"decision_id": "DEC-2026-001", "brief_description": "Add Multi-Factor Authentication to login flow", "object_affected": "requirement", "previous_state": "REQ-01 v1.0 - OAuth2 only", "new_state": "REQ-01 v1.1 - OAuth2 + MFA", "trigger_event": "Security audit finding AUTH-2026-042", "reasoning": "Security audit identified single-factor authentication as insufficient for production data access. MFA reduces breach risk by 99.9%.",
        "proposed_by": "Security Engineer A", "approved_by": "CTO - Maria Rossi", "source_evidence": ["email:security-audit-2026-04-05@company.com", "pr:https://github.com/company/repo/pull/234", "file:docs/security/AUTH-2026-042.pdf"], "timestamp": "2026-04-10T09:00:00", "status": "approved", "version": "v1.2.0", "baseline_id": "BASELINE-2026-Q2-v2"},
    {"decision_id": "DEC-2026-002", "brief_description": "Reduce API rate limit due to DDoS vulnerability", "object_affected": "requirement", "previous_state": "REQ-03 v1.0 - 1000 req/min", "new_state": "REQ-03 v1.1 - 500 req/min", "trigger_event": "Penetration test finding PEN-2026-018", "reasoning": "Penetration test demonstrated ability to overwhelm API at 1000 req/min. Reducing to 500 req/min with burst allowance maintains usability while mitigating risk.",
        "proposed_by": "DevOps Engineer B", "approved_by": "CTO - Maria Rossi", "source_evidence": ["email:pen-test-results-2026-04-08@company.com", "pr:https://github.com/company/repo/pull/235", "file:tests/api/test_rate_limit_v2.py"], "timestamp": "2026-04-11T14:30:00", "status": "approved", "version": "v1.2.0", "baseline_id": "BASELINE-2026-Q2-v2"},
    {"decision_id": "DEC-2026-003", "brief_description": "Add immutable audit logging for admin actions", "object_affected": "requirement", "previous_state": "No audit logging requirement", "new_state": "REQ-04 v1.0 - Full audit logging", "trigger_event": "Compliance requirement GDPR Article 30", "reasoning": "GDPR Article 30 requires records of processing activities. Immutable audit logs satisfy this and provide forensic capability.",
        "proposed_by": "Compliance Officer C", "approved_by": "CTO - Maria Rossi", "source_evidence": ["email:gdpr-compliance-2026-04-01@company.com", "pr:https://github.com/company/repo/pull/230", "file:docs/compliance/GDPR-Article-30.pdf"], "timestamp": "2026-04-12T11:00:00", "status": "approved", "version": "v1.2.0", "baseline_id": "BASELINE-2026-Q2-v2"},
    {"decision_id": "DEC-2026-003A", "brief_description": "Add email notification service", "object_affected": "requirement", "previous_state": "No email capability", "new_state": "REQ-07 v1.0 - Email service", "trigger_event": "User story US-2026-089", "reasoning": "Users need password reset and notification emails. SMTP integration is standard and low risk.",
        "proposed_by": "Backend Engineer J", "approved_by": "Product Manager E", "source_evidence": ["email:user-stories-2026-04-10@company.com", "pr:https://github.com/company/repo/pull/238"], "timestamp": "2026-04-13T10:00:00", "status": "approved", "version": "v1.2.0", "baseline_id": "BASELINE-2026-Q2-v2"},
    {"decision_id": "DEC-2026-004", "brief_description": "Delay ML Pipeline integration to Q3", "object_affected": "release", "previous_state": "Planned for v1.2.0", "new_state": "Postponed to v2.0.0 (Q3)", "trigger_event": "Performance test failure PERF-2026-003", "reasoning": "ML pipeline adds 300ms latency per request, exceeding SLA of 100ms. Requires optimization before release.", "proposed_by": "ML Engineer D", "approved_by": "Product Manager E", "source_evidence": [
        "email:perf-test-failure-2026-04-14@company.com", "file:tests/performance/PERF-2026-003-report.pdf", "message:slack:#ml-team"], "timestamp": "2026-04-14T16:45:00", "status": "approved", "version": "v1.2.0", "baseline_id": "BASELINE-2026-Q2-v2"},
    {"decision_id": "DEC-2026-005", "brief_description": "Reject deployment due to memory overflow in congestion test", "object_affected": "release", "previous_state": "Ready for production", "new_state": "REJECTED - Requires fix", "trigger_event": "Test T-02 failure - memory overflow", "reasoning": "Congestion test T-02 failed with memory overflow at 10k concurrent users. Risk of production outage unacceptable.",
        "proposed_by": "QA Engineer F", "approved_by": "Manager D", "source_evidence": ["file:tests/results/T-02-failure.log", "email:stakeholder-c-claim-fix@external.com", "pr:https://github.com/company/repo/pull/240"], "timestamp": "2026-04-15T10:25:00", "status": "rejected", "version": "v1.2.0", "baseline_id": "BASELINE-2026-Q2-v2"},
    {"decision_id": "DEC-2026-006", "brief_description": "Supersede DEC-2026-005 after verified fix", "object_affected": "approval_criterion", "previous_state": "REJECTED", "new_state": "APPROVED (superseded)", "trigger_event": "Fix verified in test T-02-retry", "reasoning": "Memory leak fixed in commit abc1234. Retest T-02 passed with 15k concurrent users. Original rejection superseded.", "proposed_by": "QA Engineer F", "approved_by": "Manager D", "source_evidence": [
        "file:tests/results/T-02-retry-passed.log", "email:qa-signoff-2026-04-16@company.com", "pr:https://github.com/company/repo/pull/241"], "timestamp": "2026-04-16T09:00:00", "status": "superseded", "version": "v1.2.0", "baseline_id": "BASELINE-2026-Q2-v2"}
]

SEED_NULLA_OSTA = [
    {"decision_id": "DEC-2026-000", "operator_role": "System Architect", "nulla_osta_date": "2026-03-20T12:00:00", "operator": "Chief Architect G",
        "electronic_signature_ref": "sig://chief.architect@company.com/20260320", "version": "v1.0.0", "status": "granted"},
    {"decision_id": "DEC-2026-000A", "operator_role": "Security Lead", "nulla_osta_date": "2026-03-25T16:00:00", "operator": "Security Lead K",
        "electronic_signature_ref": "sig://security.lead@company.com/20260325", "version": "v1.0.0", "status": "granted"},
    {"decision_id": "DEC-2026-000B", "operator_role": "Product Lead", "nulla_osta_date": "2026-04-05T11:00:00", "operator": "Product Manager E",
        "electronic_signature_ref": "sig://product.manager@company.com/20260405", "version": "v1.1.0", "status": "granted"},
    {"decision_id": "DEC-2026-000C", "operator_role": "Engineering Manager", "nulla_osta_date": "2026-04-09T14:00:00",
        "operator": "Engineering Lead I", "electronic_signature_ref": "sig://eng.lead@company.com/20260409", "version": "v1.1.0", "status": "granted"},
    {"decision_id": "DEC-2026-001", "operator_role": "Security Lead", "nulla_osta_date": "2026-04-10T10:00:00", "operator": "Marco Bianchi",
        "electronic_signature_ref": "sig://marco.bianchi@company.com/20260410", "version": "v1.2.0", "status": "granted"},
    {"decision_id": "DEC-2026-002", "operator_role": "Infrastructure Lead", "nulla_osta_date": "2026-04-11T15:30:00", "operator": "Laura Verdi",
        "electronic_signature_ref": "sig://laura.verdi@company.com/20260411", "version": "v1.2.0", "status": "granted"},
    {"decision_id": "DEC-2026-003", "operator_role": "Compliance Officer", "nulla_osta_date": "2026-04-12T12:00:00", "operator": "Giulia Neri",
        "electronic_signature_ref": "sig://giulia.neri@company.com/20260412", "version": "v1.2.0", "status": "granted"},
    {"decision_id": "DEC-2026-003A", "operator_role": "Backend Lead", "nulla_osta_date": "2026-04-13T14:00:00", "operator": "Backend Lead L",
        "electronic_signature_ref": "sig://backend.lead@company.com/20260413", "version": "v1.2.0", "status": "granted"},
    {"decision_id": "DEC-2026-004", "operator_role": "Product Lead", "nulla_osta_date": "2026-04-14T17:30:00", "operator": "Paolo Gialli",
        "electronic_signature_ref": "sig://paolo.gialli@company.com/20260414", "version": "v1.2.0", "status": "granted"},
    {"decision_id": "DEC-2026-005", "operator_role": "QA Manager", "nulla_osta_date": "2026-04-15T11:00:00", "operator": "Manager D",
        "electronic_signature_ref": "sig://manager.d@company.com/20260415", "version": "v1.2.0", "status": "denied"},
    {"decision_id": "DEC-2026-006", "operator_role": "QA Manager", "nulla_osta_date": "2026-04-16T10:00:00", "operator": "Manager D",
        "electronic_signature_ref": "sig://manager.d@company.com/20260416", "version": "v1.2.0", "status": "granted"}
]

SEED_RELEASE_DECLARATIONS = [
    {"version": "v1.0.0", "person": "Manager Z", "role": "Release Manager", "place": "Data Center Milan", "timestamp": "2026-04-10T10:30:00",
     "declaration_text": "Io sottoscritto/a, Manager Z, in qualita di Operatore Autorizzato, confermo di aver esaminato le modifiche e i relativi risultati dei test, e di ritenere che la versione v1.0.0 del sistema sia pronta per il rilascio in produzione. Il rilascio avverra presso Data Center Milan in conformita con la procedura standard di deployment.",
     "signature_ref": "sig://manager.z@company.com/20260410"},
    {"version": "v1.1.0", "person": "Manager Y", "role": "Release Manager", "place": "Data Center Rome", "timestamp": "2026-04-12T15:00:00",
     "declaration_text": "Io sottoscritto/a, Manager Y, in qualita di Operatore Autorizzato, confermo di aver esaminato le modifiche e i relativi risultati dei test, e di ritenere che la versione v1.1.0 del sistema sia pronta per il rilascio in produzione. Il rilascio avverra presso Data Center Rome in conformita con la procedura standard di deployment.",
     "signature_ref": "sig://manager.y@company.com/20260412"},
    {"version": "v1.2.0", "person": "CTO - Maria Rossi", "role": "Chief Technology Officer", "place": "Data Center Milan", "timestamp": "2026-04-16T12:00:00",
     "declaration_text": "Io sottoscritta, Maria Rossi, in qualita di Operatore Autorizzato, confermo di aver esaminato le modifiche e i relativi risultati dei test, e di ritenere che la versione v1.2.0 del sistema sia pronta per il rilascio in produzione. Il rilascio avverra presso Data Center Milan in conformita con la procedura standard di deployment.",
     "signature_ref": "sig://maria.rossi@company.com/20260416"}
]

SEED_CONFLICTS = [
    {"conflict_id": "CONF-2026-001", "version": "v1.2.0", "description": "Stakeholder C claimed T-02 issue was fixed via email, but no verification data existed in test system.", "severity": "high",
     "resolution": "Rejected the claim. Required formal test verification before approval. Stakeholder provided test results in follow-up.", "resolved_by": "Manager D", "resolved_at": "2026-04-15T14:00:00", "related_decisions": ["DEC-2026-005"], "related_requirements": ["REQ-02"]},
    {"conflict_id": "CONF-2026-002", "version": "v1.2.0", "description": "ML Pipeline requirement REQ-05 was planned for v1.2.0 but performance tests showed 300ms latency, exceeding 100ms SLA.", "severity": "critical",
     "resolution": "Decision made to postpone ML Pipeline to Q3 (v2.0.0) to allow optimization without blocking current release.", "resolved_by": "Product Manager E", "resolved_at": "2026-04-14T17:00:00", "related_decisions": ["DEC-2026-004"], "related_requirements": ["REQ-05"]},
    {"conflict_id": "CONF-2026-003", "version": "v1.2.0", "description": "Security audit required MFA (breaking change) mid-release cycle. Risk of delaying release vs security compliance.", "severity": "medium",
     "resolution": "Approved MFA addition with expedited testing. Allocated additional QA resources to maintain schedule.", "resolved_by": "CTO - Maria Rossi", "resolved_at": "2026-04-10T12:00:00", "related_decisions": ["DEC-2026-001"], "related_requirements": ["REQ-01"]},
    {"conflict_id": "CONF-2026-004", "version": "v1.1.0", "description": "User profile module conflicted with existing authentication flow during integration testing.", "severity": "medium",
     "resolution": "Refactored auth middleware to support profile context. Added integration tests covering both flows.", "resolved_by": "Engineer X", "resolved_at": "2026-04-11T16:00:00", "related_decisions": ["DEC-2026-000B"], "related_requirements": ["REQ-06"]},
    {"conflict_id": "CONF-2026-005", "version": "v1.0.0", "description": "OAuth2 implementation conflicted with legacy API key authentication during migration.", "severity": "low",
     "resolution": "Maintained backward compatibility with API keys for 30 days. Added deprecation warnings and migration guide.", "resolved_by": "Security Engineer H", "resolved_at": "2026-04-08T10:00:00", "related_decisions": ["DEC-2026-000A"], "related_requirements": ["REQ-01"]}
]

SEED_PUBLISHED_VERSIONS = [
    {"version": "v1.0.0", "publication_date": "2026-04-10T10:30:00", "status": "published", "key_changes": ["Initial system release", "Core authentication and encryption", "API rate limiting implemented"], "conflicts_addressed": [
        "CONF-2026-005: OAuth2 migration resolved"], "decision_ids": ["DEC-2026-000", "DEC-2026-000A"], "baseline_id": "BASELINE-2026-Q2-v1", "release_declaration_id": "v1.0.0", "previous_version": None},
    {"version": "v1.1.0", "publication_date": "2026-04-12T15:00:00", "status": "published", "key_changes": ["User profile module added", "REQ-02 test coverage improved"], "conflicts_addressed": [
        "CONF-2026-004: Profile auth integration resolved"], "decision_ids": ["DEC-2026-000B", "DEC-2026-000C"], "baseline_id": "BASELINE-2026-Q2-v1", "release_declaration_id": "v1.1.0", "previous_version": "v1.0.0"},
    {"version": "v1.2.0", "publication_date": "2026-04-16T12:00:00", "status": "published", "key_changes": ["Multi-Factor Authentication added (REQ-01 v1.1)", "API rate limit reduced to 500/min (REQ-03 v1.1)", "Immutable audit logging implemented (REQ-04 v1.0)", "Email notification service (REQ-07 v1.0)", "ML Pipeline postponed to Q3"], "conflicts_addressed": [
        "CONF-2026-001: Unverified stakeholder claim resolved", "CONF-2026-002: ML Pipeline performance conflict resolved", "CONF-2026-003: MFA mid-cycle addition resolved"], "decision_ids": ["DEC-2026-001", "DEC-2026-002", "DEC-2026-003", "DEC-2026-003A", "DEC-2026-004", "DEC-2026-005", "DEC-2026-006"], "baseline_id": "BASELINE-2026-Q2-v2", "release_declaration_id": "v1.2.0", "previous_version": "v1.1.0"}
]

SEED_EVENTS = [
    # v1.0.0 events
    {"event_id": "EV_V1_01", "version": "v1.0.0", "type": "ARCHITECTURE_APPROVED", "related_to": "DEC-2026-000",
        "layer": "Architecture", "timestamp": "2026-03-20T10:00:00", "description": "Microservices architecture approved by CTO."},
    {"event_id": "EV_V1_02", "version": "v1.0.0", "type": "SECURITY_STANDARD_SET", "related_to": "DEC-2026-000A",
        "layer": "Security", "timestamp": "2026-03-25T14:00:00", "description": "OAuth2 selected as authentication standard."},
    {"event_id": "EV_V1_03", "version": "v1.0.0", "type": "TEST_EXECUTION", "related_to": "T-Auth-01", "layer": "Testing",
        "timestamp": "2026-04-08T09:00:00", "description": "All core tests passed - 20/20 requirements verified."},
    {"event_id": "EV_V1_04", "version": "v1.0.0", "type": "NULLA_OSTA_GRANTED", "related_to": "DEC-2026-000",
        "layer": "Approval", "timestamp": "2026-04-10T10:30:00", "description": "Manager Z granted Nulla Osta for v1.0.0 release."},

    # v1.1.0 events
    {"event_id": "EV_V2_01", "version": "v1.1.0", "type": "REQUIREMENT_ADDED", "related_to": "REQ-06", "layer": "Requirements",
        "timestamp": "2026-04-05T09:30:00", "description": "User profile module added to scope per roadmap update."},
    {"event_id": "EV_V2_02", "version": "v1.1.0", "type": "CONFLICT_DETECTED", "related_to": "CONF-2026-004", "layer": "Integration",
        "timestamp": "2026-04-10T14:00:00", "description": "Profile module conflicted with auth flow during integration."},
    {"event_id": "EV_V2_03", "version": "v1.1.0", "type": "FIX_COMMITTED", "related_to": "CONF-2026-004", "layer": "Development",
        "timestamp": "2026-04-11T12:00:00", "description": "Auth middleware refactored to support profile context."},
    {"event_id": "EV_V2_04", "version": "v1.1.0", "type": "NULLA_OSTA_GRANTED", "related_to": "DEC-2026-000B",
        "layer": "Approval", "timestamp": "2026-04-12T15:00:00", "description": "Manager Y granted Nulla Osta for v1.1.0 release."},

    # v1.2.0 events
    {"event_id": "EV_01", "version": "v1.2.0", "type": "TEST_EXECUTION", "related_to": "T-02",
        "layer": "Testing", "timestamp": "2026-04-15T10:00:00", "description": "Congestion test T-02 executed."},
    {"event_id": "EV_02", "version": "v1.2.0", "type": "TEST_FAILED", "related_to": "T-02", "layer": "Testing",
        "timestamp": "2026-04-15T10:01:00", "description": "Test T-02 failed: memory overflow detected."},
    {"event_id": "EV_03", "version": "v1.2.0", "type": "EMAIL_RECEIVED", "related_to": "Stakeholder C", "layer": "Ingestion",
        "timestamp": "2026-04-15T10:05:00", "description": "Email from Stakeholder C received, claiming 'issue fixed'."},
    {"event_id": "EV_04", "version": "v1.2.0", "type": "CONFLICT_DETECTED", "related_to": "AI Processing", "layer": "AI Processing",
        "timestamp": "2026-04-15T10:10:00", "description": "AI detected conflict: test T-02 failed but email claims it is fixed."},
    {"event_id": "EV_05", "version": "v1.2.0", "type": "MISSING_COVERAGE", "related_to": "REQ-05", "layer": "AI Verification",
        "timestamp": "2026-04-15T10:15:00", "description": "AI detected missing test coverage for requirement REQ-05."},
    {"event_id": "EV_06", "version": "v1.2.0", "type": "AI_RECOMMENDATION", "related_to": "AI Processing", "layer": "AI Processing",
        "timestamp": "2026-04-15T10:20:00", "description": "AI generated 'Delay' recommendation based on test failure and missing coverage."},
    {"event_id": "EV_07", "version": "v1.2.0", "type": "HUMAN_DECISION", "related_to": "Manager D",
        "layer": "Decision", "timestamp": "2026-04-15T10:25:00", "description": "Manager D confirmed REJECTED status."},
    {"event_id": "EV_08", "version": "v1.2.0", "type": "FIX_COMMITTED", "related_to": "T-02", "layer": "Development",
        "timestamp": "2026-04-15T18:00:00", "description": "Developer committed fix for memory leak in PR #241."},
    {"event_id": "EV_09", "version": "v1.2.0", "type": "TEST_PASSED", "related_to": "T-02-retry", "layer": "Testing",
        "timestamp": "2026-04-16T08:00:00", "description": "Retest T-02 passed with 15k concurrent users."},
    {"event_id": "EV_10", "version": "v1.2.0", "type": "NULLA_OSTA_GRANTED", "related_to": "DEC-2026-006", "layer": "Approval",
        "timestamp": "2026-04-16T10:00:00", "description": "Manager D granted Nulla Osta for superseded decision."},
    {"event_id": "EV_11", "version": "v1.2.0", "type": "RELEASE_DECLARED", "related_to": "v1.2.0", "layer": "Release",
        "timestamp": "2026-04-16T12:00:00", "description": "CTO Maria Rossi signed Dichiarazione di Rilascio for v1.2.0."}
]

SEED_TRACEABILITY = [
    {"req_id": "REQ-01", "test_id": "T-Auth-01",
        "events": ["EV_V1_02", "EV_V1_03"], "decision": "v1.0.0"},
    {"req_id": "REQ-02", "test_id": "T-Encrypt-01",
        "events": ["EV_V1_03"], "decision": "v1.0.0"},
    {"req_id": "REQ-03", "test_id": "T-Rate-01",
        "events": ["EV_V1_03"], "decision": "v1.0.0"},
    {"req_id": "REQ-06", "test_id": "T-Profile-01",
        "events": ["EV_V2_02", "EV_V2_03"], "decision": "v1.1.0"},
    {"req_id": "REQ-05", "test_id": None,
        "events": ["EV_05"], "decision": "v1.2.0"},
    {"req_id": "REQ-10", "test_id": "T-02",
        "events": ["EV_01", "EV_02", "EV_04"], "decision": "v1.2.0"},
    {"req_id": "REQ-04", "test_id": "T-Audit-01",
        "events": ["EV_01"], "decision": "v1.2.0"},
    {"req_id": "REQ-07", "test_id": "T-Email-01",
        "events": ["EV_01"], "decision": "v1.2.0"}
]

SEED_HUMAN_TRACEABILITY = [
    {"version": "v1.0.0", "role": "System Architect", "person": "Chief Architect G"},
    {"version": "v1.0.0", "role": "Security Lead", "person": "Security Lead K"},
    {"version": "v1.0.0", "role": "Final Approver", "person": "Manager Z"},
    {"version": "v1.1.0", "role": "Product Manager", "person": "Product Manager E"},
    {"version": "v1.1.0", "role": "Integration Lead", "person": "Engineer X"},
    {"version": "v1.1.0", "role": "Final Approver", "person": "Manager Y"},
    {"version": "v1.2.0",
        "role": "Requirement Creator (REQ-05)", "person": "Engineer A"},
    {"version": "v1.2.0",
        "role": "Test Executor (T-02)", "person": "Automated System"},
    {"version": "v1.2.0", "role": "Failure Reviewer", "person": "QA Engineer B"},
    {"version": "v1.2.0",
        "role": "External Communicator (Email)", "person": "Stakeholder C"},
    {"version": "v1.2.0", "role": "Backend Developer",
        "person": "Backend Engineer J"},
    {"version": "v1.2.0", "role": "ML Engineer", "person": "ML Engineer D"},
    {"version": "v1.2.0", "role": "Final Approver", "person": "Manager D"},
    {"version": "v1.2.0", "role": "CTO", "person": "Maria Rossi"}
]

SEED_AI_TRACEABILITY = [
    {"version": "v1.0.0", "step": "Architecture validation",
        "details": "AI validated microservices architecture against 12-factor app criteria."},
    {"version": "v1.0.0", "step": "Security assessment",
        "details": "AI assessed OAuth2 implementation against OWASP standards."},
    {"version": "v1.1.0", "step": "Integration risk analysis",
        "details": "AI predicted auth/profile integration conflict with 78% confidence."},
    {"version": "v1.2.0", "step": "Input received",
        "details": "Structured JSON parsed from test results and stakeholder emails."},
    {"version": "v1.2.0", "step": "Context retrieved via RAG",
        "details": "Historical safety failures related to REQ-05 retrieved."},
    {"version": "v1.2.0", "step": "Reasoning generated",
        "details": "Conflict identified between failed test T-02 and unverified email claim."},
    {"version": "v1.2.0", "step": "Recommendation produced",
        "details": "Delay release due to HIGH safety risk and lack of verified fixes."},
    {"version": "v1.2.0", "step": "Post-fix verification",
        "details": "AI verified T-02 retry results meet acceptance criteria."}
]

SEED_STOP_SIGNALS = [
    {"process_id": "PROC-2026-Q2-CAP-001", "reason": "Resource constraint detected during sprint planning. Need to reprioritize features.", "requested_by": "Engineering Lead I",
        "timestamp": "2026-04-08T09:00:00", "resolved": True, "resolved_at": "2026-04-09T11:00:00", "resolution": "Encryption enhancement delayed to v1.2.0"},
    {"process_id": "PROC-2026-Q3-ML-001", "reason": "New requirement REQ-05 v1.1 received while evaluating ML pipeline performance. Need to update baseline.",
        "requested_by": "Product Manager E", "timestamp": "2026-05-02T09:00:00", "resolved": False},
    {"process_id": "PROC-2026-Q3-ANALYTICS-001", "reason": "Real-time analytics requirement REQ-08 needs WebSocket infrastructure not yet provisioned.",
        "requested_by": "DevOps Engineer B", "timestamp": "2026-05-10T14:00:00", "resolved": False}
]

SEED_DECISION_JOURNAL = [
    {"version": "v1.0.0", "status": "APPROVED", "risk_level": "LOW", "summary": {"total_req": 20, "tested": 20, "passed": 20, "failed": 0, "missing": 0}, "problems": [], "decision": {"change": "Initial release of the core system.",
                                                                                                                                                                                       "impact": "Low, establishes baseline functionality.", "assumption": "All core requirements are met and tested.", "alternatives": "N/A for initial release.", "recommendation": "Approve"}, "timestamp": "2026-04-10T10:00:00"},
    {"version": "v1.1.0", "status": "REJECTED", "risk_level": "MEDIUM", "summary": {"total_req": 22, "tested": 21, "passed": 21, "failed": 0, "missing": 1}, "problems": ["REQ-02 missing test coverage."], "decision": {
        "change": "Added new user profile module.", "impact": "Medium, affects user data handling.", "assumption": "The untested requirement is non-critical for this build.", "alternatives": "Proceed with risk, Delay for test creation.", "recommendation": "Delay"}, "timestamp": "2026-04-12T14:30:00"},
    {"version": "v1.2.0", "status": "REJECTED", "risk_level": "HIGH", "summary": {"total_req": 25, "tested": 22, "passed": 20, "failed": 2, "missing": 3}, "problems": ["REQ-05: Missing test coverage for new validation logic.", "T-02: Congestion test failed with memory overflow.", "Conflict: Email from Stakeholder C claims issue is fixed, but no verification data exists."], "decision": {
        "change": "Refactor of the input processing module for performance.", "impact": "High safety risk due to potential for system congestion.", "assumption": "An external email claiming a fix is not sufficient evidence.", "alternatives": "Proceed with high risk, Delay release until verified fix, Rollback change.", "recommendation": "Delay"}, "timestamp": "2026-04-15T10:25:00"}
]
