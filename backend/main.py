from fastapi import FastAPI, HTTPException, Body
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from pymongo import MongoClient
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime
import os
import uuid

try:
    from backend.data import (
        SEED_REQUIREMENTS_BASELINES, SEED_DECISIONS, SEED_NULLA_OSTA,
        SEED_RELEASE_DECLARATIONS, SEED_CONFLICTS, SEED_PUBLISHED_VERSIONS,
        SEED_EVENTS, SEED_TRACEABILITY, SEED_HUMAN_TRACEABILITY,
        SEED_AI_TRACEABILITY, SEED_STOP_SIGNALS, SEED_DECISION_JOURNAL
    )
except ImportError:
    from data import (
        SEED_REQUIREMENTS_BASELINES, SEED_DECISIONS, SEED_NULLA_OSTA,
        SEED_RELEASE_DECLARATIONS, SEED_CONFLICTS, SEED_PUBLISHED_VERSIONS,
        SEED_EVENTS, SEED_TRACEABILITY, SEED_HUMAN_TRACEABILITY,
        SEED_AI_TRACEABILITY, SEED_STOP_SIGNALS, SEED_DECISION_JOURNAL
    )


app = FastAPI(title="Decision Journal API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)
db = client["decision_journal_db"]


class StopSignal(BaseModel):
    process_id: str
    reason: str
    requested_by: str
    timestamp: Optional[str] = None

# ============================================================================
# EXISTING ENDPOINTS (Backward Compatibility)
# ============================================================================


# Serve frontend static files
app.mount("/static", StaticFiles(directory="../frontend"), name="static")


@app.get("/", response_class=HTMLResponse)
def serve_dashboard():
    try:
        with open(os.path.join(os.path.dirname(__file__), "..", "frontend", "index.html"), "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"<html><body><h1>Dashboard Error</h1><p>{str(e)}</p><p>Please open frontend/index.html directly</p></body></html>"


@app.get("/decision/{version}")
def get_decision(version: str):
    decision = db.decision_journal.find_one({"version": version}, {"_id": 0})
    if not decision:
        raise HTTPException(status_code=404, detail="Decision not found")
    return decision


@app.get("/events/{version}")
def get_events(version: str):
    return list(db.events.find({"version": version}, {"_id": 0}))


@app.get("/timeline/{version}")
def get_timeline(version: str):
    return list(db.events.find({"version": version}, {"_id": 0}).sort("timestamp", 1))


@app.get("/history")
def get_history():
    return list(db.decision_journal.find({}, {"_id": 0, "version": 1, "status": 1, "timestamp": 1}).sort("timestamp", -1))


@app.get("/trace/{req_id}")
def get_traceability(req_id: str):
    trace = db.traceability.find_one({"req_id": req_id}, {"_id": 0})
    if not trace:
        raise HTTPException(status_code=404, detail="Traceability not found")
    events = list(db.events.find(
        {"event_id": {"$in": trace.get("events", [])}}, {"_id": 0}))
    trace["events_details"] = events
    return trace


@app.get("/traceable_items/{version}")
def get_traceable_items(version: str):
    items = {item['req_id'] for item in db.traceability.find(
        {"decision": version, "req_id": {"$ne": None}}, {"_id": 0, "req_id": 1})}
    return sorted(list(items))


@app.get("/trace/human/{version}")
def get_human_trace(version: str):
    return list(db.human_traceability.find({"version": version}, {"_id": 0}))


@app.get("/trace/ai/{version}")
def get_ai_trace(version: str):
    return list(db.ai_traceability.find({"version": version}, {"_id": 0}))

# ============================================================================
# NEW ENDPOINTS - DECISION LEDGER
# ============================================================================


@app.get("/decisions/{version}")
def get_decisions_ledger(version: str):
    decisions = list(db.decisions_ledger.find(
        {"version": version}, {"_id": 0}))
    return {"version": version, "count": len(decisions), "decisions": decisions}


@app.get("/decision_record/{decision_id}")
def get_decision_record(decision_id: str):
    decision = db.decisions_ledger.find_one(
        {"decision_id": decision_id}, {"_id": 0})
    if not decision:
        raise HTTPException(
            status_code=404, detail="Decision record not found")
    return decision


@app.get("/decision_history/{decision_id}")
def get_decision_history(decision_id: str):
    decision = db.decisions_ledger.find_one(
        {"decision_id": decision_id}, {"_id": 0})
    if not decision:
        raise HTTPException(status_code=404, detail="Decision not found")
    history = list(db.decisions_ledger.find(
        {"brief_description": decision["brief_description"]}, {"_id": 0}).sort("timestamp", 1))
    events = list(db.events.find({"related_to": decision_id}, {
                  "_id": 0}).sort("timestamp", 1))
    return {"decision": decision, "historical_versions": history, "related_events": events}

# ============================================================================
# NEW ENDPOINTS - NULLA OSTA
# ============================================================================


@app.get("/nulla_osta/{decision_id}")
def get_nulla_osta(decision_id: str):
    nulla_osta = db.nulla_osta.find_one(
        {"decision_id": decision_id}, {"_id": 0})
    if not nulla_osta:
        raise HTTPException(status_code=404, detail="Nulla Osta not found")
    return nulla_osta


@app.get("/nulla_osta/version/{version}")
def get_nulla_osta_by_version(version: str):
    records = list(db.nulla_osta.find({"version": version}, {"_id": 0}))
    return {"version": version, "count": len(records), "nulla_osta_records": records}

# ============================================================================
# NEW ENDPOINTS - RELEASE DECLARATION
# ============================================================================


@app.get("/release_declaration/{version}")
def get_release_declaration(version: str):
    declaration = db.release_declarations.find_one(
        {"version": version}, {"_id": 0})
    if not declaration:
        raise HTTPException(
            status_code=404, detail="Release declaration not found")
    return declaration

# ============================================================================
# NEW ENDPOINTS - REQUIREMENTS BASELINES
# ============================================================================


@app.get("/requirements/baselines")
def get_all_baselines():
    return {"count": db.requirements_baselines.count_documents({}), "baselines": list(db.requirements_baselines.find({}, {"_id": 0}))}


@app.get("/requirements/baseline/{baseline_id}")
def get_baseline(baseline_id: str):
    baseline = db.requirements_baselines.find_one(
        {"baseline_id": baseline_id}, {"_id": 0})
    if not baseline:
        raise HTTPException(status_code=404, detail="Baseline not found")
    decisions = list(db.decisions_ledger.find(
        {"baseline_id": baseline_id}, {"_id": 0}))
    return {"baseline": baseline, "linked_decisions": decisions}


@app.get("/requirements/baseline/{baseline_id}/requirements")
def get_baseline_requirements(baseline_id: str):
    baseline = db.requirements_baselines.find_one(
        {"baseline_id": baseline_id}, {"_id": 0})
    if not baseline:
        raise HTTPException(status_code=404, detail="Baseline not found")
    return {"baseline_id": baseline_id, "requirements": baseline.get("requirements", [])}

# ============================================================================
# NEW ENDPOINTS - CONFLICTS
# ============================================================================


@app.get("/conflicts/{version}")
def get_conflicts(version: str):
    return {"version": version, "count": db.conflicts_resolved.count_documents({"version": version}), "conflicts": list(db.conflicts_resolved.find({"version": version}, {"_id": 0}))}


@app.get("/conflicts/all")
def get_all_conflicts():
    return {"count": db.conflicts_resolved.count_documents({}), "conflicts": list(db.conflicts_resolved.find({}, {"_id": 0}))}

# ============================================================================
# NEW ENDPOINTS - PUBLISHED VERSIONS
# ============================================================================


@app.get("/published_versions")
def get_published_versions():
    return {"count": db.published_versions.count_documents({}), "versions": list(db.published_versions.find({}, {"_id": 0}).sort("publication_date", -1))}


@app.get("/published_versions/latest")
def get_latest_published():
    latest = db.published_versions.find_one(
        {}, {"_id": 0}, sort=[("publication_date", -1)])
    if not latest:
        raise HTTPException(
            status_code=404, detail="No published versions found")
    version = latest["version"]
    return {
        "overview": latest,
        "decisions": list(db.decisions_ledger.find({"version": version}, {"_id": 0})),
        "conflicts": list(db.conflicts_resolved.find({"version": version}, {"_id": 0})),
        "nulla_osta": list(db.nulla_osta.find({"version": version}, {"_id": 0})),
        "release_declaration": db.release_declarations.find_one({"version": version}, {"_id": 0}),
        "baseline": db.requirements_baselines.find_one({"baseline_id": latest.get("baseline_id")}, {"_id": 0}),
        "events": list(db.events.find({"version": version}, {"_id": 0}).sort("timestamp", 1))
    }


@app.get("/published_versions/{version}")
def get_published_version(version: str):
    published = db.published_versions.find_one(
        {"version": version}, {"_id": 0})
    if not published:
        raise HTTPException(
            status_code=404, detail="Published version not found")
    return {
        "overview": published,
        "decisions": list(db.decisions_ledger.find({"version": version}, {"_id": 0})),
        "conflicts": list(db.conflicts_resolved.find({"version": version}, {"_id": 0})),
        "nulla_osta": list(db.nulla_osta.find({"version": version}, {"_id": 0})),
        "release_declaration": db.release_declarations.find_one({"version": version}, {"_id": 0}),
        "baseline": db.requirements_baselines.find_one({"baseline_id": published.get("baseline_id")}, {"_id": 0}),
        "events": list(db.events.find({"version": version}, {"_id": 0}).sort("timestamp", 1))
    }

# ============================================================================
# NEW ENDPOINTS - STOP SIGNAL
# ============================================================================


@app.post("/stop_signal")
def create_stop_signal(signal: StopSignal):
    signal_data = signal.dict()
    if not signal_data.get("timestamp"):
        signal_data["timestamp"] = datetime.utcnow().isoformat()
    result = db.stop_signals.insert_one(signal_data)
    return {"message": "Stop signal received", "signal_id": str(result.inserted_id), "process_id": signal.process_id, "timestamp": signal_data["timestamp"], "status": "analysis_halted"}


@app.get("/stop_signals")
def get_stop_signals():
    return {"count": db.stop_signals.count_documents({}), "signals": list(db.stop_signals.find({}, {"_id": 0}).sort("timestamp", -1))}


@app.get("/stop_signals/active")
def get_active_stop_signals():
    return {"count": db.stop_signals.count_documents({"resolved": {"$ne": True}}), "signals": list(db.stop_signals.find({"resolved": {"$ne": True}}, {"_id": 0}).sort("timestamp", -1))}

# ============================================================================
# AI AGENT ORGANIZATION ENDPOINTS
# ============================================================================


@app.get("/ai_agent/status")
def get_ai_agent_status():
    latest_decision = db.decisions_ledger.find_one(
        {}, {"_id": 0}, sort=[("timestamp", -1)])
    return {
        "status": "active",
        "organized_data": {
            "decisions": db.decisions_ledger.count_documents({}),
            "baselines": db.requirements_baselines.count_documents({}),
            "published_versions": db.published_versions.count_documents({}),
            "conflicts_resolved": db.conflicts_resolved.count_documents({})
        },
        "latest_activity": latest_decision,
        "timestamp": datetime.utcnow().isoformat()
    }


@app.get("/ai_agent/activity_log")
def get_ai_activity_log():
    return {"count": db.ai_traceability.count_documents({}), "activities": list(db.ai_traceability.find({}, {"_id": 0}).sort("timestamp", -1))}

# ============================================================================
# GITHUB ACTIONS INTEGRATION
# ============================================================================


@app.post("/github/webhook/decision")
def github_webhook_decision(payload: Dict[str, Any] = Body(...)):
    version = payload.get("version", "unknown")
    decision_data = payload.get("decision", {})
    decision_record = {
        "decision_id": f"DEC-{uuid.uuid4().hex[:8].upper()}",
        "version": version,
        "timestamp": datetime.utcnow().isoformat(),
        "source": "github_actions",
        "payload": payload,
        **decision_data
    }
    db.decisions_ledger.insert_one(decision_record)
    return {"message": "Decision recorded from GitHub Actions", "decision_id": decision_record["decision_id"]}


@app.get("/github/status")
def get_github_integration_status():
    return {
        "integration_status": "ready",
        "recent_github_decisions": list(db.decisions_ledger.find({"source": "github_actions"}, {"_id": 0}).sort("timestamp", -1).limit(5)),
        "webhook_endpoint": "/github/webhook/decision",
        "supported_events": ["release", "pull_request", "workflow_run"]
    }

# ============================================================================
# AI PIPELINE INGESTION ENDPOINT (For upcoming pipeline JSON files)
# ============================================================================


@app.post("/ai_pipeline/ingest")
def ingest_ai_pipeline_data(payload: Dict[str, Any] = Body(...)):
    """
    Receives flexible JSON payloads from the AI pipeline.
    Automatically logs them as traceability events and extracts decision data if present.
    """
    event_record = {
        "event_id": f"EV-AI-{uuid.uuid4().hex[:8].upper()}",
        "version": payload.get("version", "pending_version"),
        "type": payload.get("type", "AI_PIPELINE_UPDATE"),
        "layer": payload.get("layer", "AI Processing"),
        "timestamp": datetime.utcnow().isoformat(),
        "description": payload.get("description", "Received structured JSON from AI pipeline."),
        "raw_payload": payload
    }
    db.events.insert_one(event_record)

    if "decision" in payload:
        decision_data = payload["decision"]
        decision_data["source"] = "ai_pipeline"
        db.decisions_ledger.insert_one(decision_data)

    return {"message": "AI Pipeline JSON ingested successfully", "event_id": event_record["event_id"], "status": "processed"}

# ============================================================================
# COMPREHENSIVE SEED DATA
# ============================================================================


@app.post("/seed")
def seed_mock_data():
    for col in [db.decision_journal, db.events, db.traceability, db.human_traceability,
                db.ai_traceability, db.decisions_ledger, db.nulla_osta,
                db.requirements_baselines, db.release_declarations,
                db.conflicts_resolved, db.published_versions, db.stop_signals]:
        col.drop()

    db.requirements_baselines.insert_many(SEED_REQUIREMENTS_BASELINES)
    db.decisions_ledger.insert_many(SEED_DECISIONS)
    db.nulla_osta.insert_many(SEED_NULLA_OSTA)
    db.release_declarations.insert_many(SEED_RELEASE_DECLARATIONS)
    db.conflicts_resolved.insert_many(SEED_CONFLICTS)
    db.published_versions.insert_many(SEED_PUBLISHED_VERSIONS)
    db.events.insert_many(SEED_EVENTS)
    db.traceability.insert_many(SEED_TRACEABILITY)
    db.human_traceability.insert_many(SEED_HUMAN_TRACEABILITY)
    db.ai_traceability.insert_many(SEED_AI_TRACEABILITY)
    db.stop_signals.insert_many(SEED_STOP_SIGNALS)
    db.decision_journal.insert_many(SEED_DECISION_JOURNAL)
    return {"message": "Comprehensive mock data seeded successfully!", "collections": {
        "requirements_baselines": len(SEED_REQUIREMENTS_BASELINES),
        "decisions_ledger": len(SEED_DECISIONS),
        "nulla_osta": len(SEED_NULLA_OSTA),
        "release_declarations": len(SEED_RELEASE_DECLARATIONS),
        "conflicts_resolved": len(SEED_CONFLICTS),
        "published_versions": len(SEED_PUBLISHED_VERSIONS),
        "events": len(SEED_EVENTS),
        "traceability": len(SEED_TRACEABILITY),
        "human_traceability": len(SEED_HUMAN_TRACEABILITY),
        "ai_traceability": len(SEED_AI_TRACEABILITY),
        "stop_signals": len(SEED_STOP_SIGNALS),
        "decision_journal": len(SEED_DECISION_JOURNAL)
    }}
