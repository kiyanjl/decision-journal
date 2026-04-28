from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
import os

app = FastAPI(title="Decision Journal API")

# Allow frontend to access API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Connect to MongoDB
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)
db = client["decision_journal_db"]


@app.get("/decision/{version}")
def get_decision(version: str):
    decision = db.decision_journal.find_one({"version": version}, {"_id": 0})
    if not decision:
        raise HTTPException(status_code=404, detail="Decision not found")
    return decision


@app.get("/events/{version}")
def get_events(version: str):
    events = list(db.events.find({"version": version}, {"_id": 0}))
    return events


@app.get("/timeline/{version}")
def get_timeline(version: str):
    events = list(db.events.find({"version": version}, {
                  "_id": 0}).sort("timestamp", 1))
    return events


@app.get("/history")
def get_history():
    history = list(db.decision_journal.find(
        {}, {"_id": 0, "version": 1, "status": 1, "timestamp": 1}).sort("timestamp", -1))
    return history


@app.get("/trace/{req_id}")
def get_traceability(req_id: str):
    trace = db.traceability.find_one({"req_id": req_id}, {"_id": 0})
    if not trace:
        raise HTTPException(status_code=404, detail="Traceability not found")

    # Enrich with actual events
    events = list(db.events.find(
        {"event_id": {"$in": trace.get("events", [])}}, {"_id": 0}))
    trace["events_details"] = events
    return trace


@app.get("/traceable_items/{version}")
def get_traceable_items(version: str):
    """Gets all traceable requirement IDs for a given version."""
    # Using a set to ensure uniqueness of req_ids
    items = {
        item['req_id'] for item in db.traceability.find(
            {"decision": version, "req_id": {"$ne": None}},
            {"_id": 0, "req_id": 1}
        )
    }
    return sorted(list(items))


@app.get("/trace/human/{version}")
def get_human_trace(version: str):
    """Gets the human traceability records for a given version."""
    traces = list(db.human_traceability.find({"version": version}, {"_id": 0}))
    return traces


@app.get("/trace/ai/{version}")
def get_ai_trace(version: str):
    """Gets the AI traceability records for a given version."""
    traces = list(db.ai_traceability.find({"version": version}, {"_id": 0}))
    return traces


@app.post("/seed")
def seed_mock_data():
    """Seeds the MongoDB with mock data for demonstration purposes."""
    db.decision_journal.drop()
    db.events.drop()
    db.traceability.drop()

    db.human_traceability.drop()
    db.ai_traceability.drop()

    db.decision_journal.insert_many([
        {
            "version": "v1.0.0",
            "status": "APPROVED",
            "risk_level": "LOW",
            "summary": {"total_req": 20, "tested": 20, "passed": 20, "failed": 0, "missing": 0},
            "problems": [],
            "decision": {
                "change": "Initial release of the core system.",
                "impact": "Low, establishes baseline functionality.",
                "assumption": "All core requirements are met and tested.",
                "alternatives": "N/A for initial release.",
                "recommendation": "Approve"
            },
            "timestamp": "2026-04-10T10:00:00"
        },
        {
            "version": "v1.1.0",
            "status": "REJECTED",
            "risk_level": "MEDIUM",
            "summary": {"total_req": 22, "tested": 21, "passed": 21, "failed": 0, "missing": 1},
            "problems": ["REQ-02 missing test coverage."],
            "decision": {
                "change": "Added new user profile module.",
                "impact": "Medium, affects user data handling.",
                "assumption": "The untested requirement is non-critical for this build.",
                "alternatives": "Proceed with risk, Delay for test creation.",
                "recommendation": "Delay"
            },
            "timestamp": "2026-04-12T14:30:00"
        },
        {
            "version": "v1.2.0",
            "status": "REJECTED",
            "risk_level": "HIGH",
            "summary": {"total_req": 25, "tested": 22, "passed": 20, "failed": 2, "missing": 3},
            "problems": [
                "REQ-05: Missing test coverage for new validation logic.",
                "T-02: Congestion test failed with memory overflow.",
                "Conflict: Email from Stakeholder C claims issue is fixed, but no verification data exists."
            ],
            "decision": {
                "change": "Refactor of the input processing module for performance.",
                "impact": "High safety risk due to potential for system congestion.",
                "assumption": "An external email claiming a fix is not sufficient evidence.",
                "alternatives": "Proceed with high risk, Delay release until verified fix, Rollback change.",
                "recommendation": "Delay"
            },
            "timestamp": "2026-04-15T10:25:00"
        }
    ])

    db.events.insert_many([
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
            "layer": "Decision", "timestamp": "2026-04-15T10:25:00", "description": "Manager D confirmed REJECTED status."}
    ])

    db.human_traceability.insert_many([
        {"version": "v1.2.0",
            "role": "Requirement Creator (REQ-05)", "person": "Engineer A"},
        {"version": "v1.2.0",
            "role": "Test Executor (T-02)", "person": "Automated System"},
        {"version": "v1.2.0", "role": "Failure Reviewer", "person": "QA Engineer B"},
        {"version": "v1.2.0",
            "role": "External Communicator (Email)", "person": "Stakeholder C"},
        {"version": "v1.2.0", "role": "Final Approver", "person": "Manager D"},
        {"version": "v1.1.0",
            "role": "Requirement Creator (REQ-02)", "person": "Engineer X"},
        {"version": "v1.1.0", "role": "Final Approver", "person": "Manager Y"},
        {"version": "v1.0.0", "role": "Final Approver", "person": "Manager Z"},
    ])

    db.traceability.insert_many([
        {
            "req_id": "REQ-05",
            "test_id": None,
            "events": ["EV_05"],
            "decision": "v1.2.0"
        },
        {
            "req_id": "REQ-10",
            "test_id": "T-02",
            "events": ["EV_01", "EV_02", "EV_04"],
            "decision": "v1.2.0"
        }
    ])

    db.ai_traceability.insert_many([
        {"version": "v1.2.0", "step": "Input received",
            "details": "Structured JSON parsed from test results and stakeholder emails."},
        {"version": "v1.2.0", "step": "Context retrieved via RAG",
            "details": "Historical safety failures related to REQ-05 retrieved."},
        {"version": "v1.2.0", "step": "Reasoning generated",
            "details": "Conflict identified between failed test T-02 and unverified email claim."},
        {"version": "v1.2.0", "step": "Recommendation produced",
            "details": "Delay release due to HIGH safety risk and lack of verified fixes."}
    ])

    return {"message": "Mock data seeded successfully with revised model!"}
