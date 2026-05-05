# Decision Journal Dashboard — Implementation Plan

## ✅ PHASE 1: Backend Database Schema & API (COMPLETE)

- [x] All collections: decisions_ledger, nulla_osta, release_declarations, requirements_baselines, conflicts_resolved, published_versions, stop_signals
- [x] All API endpoints working
- [x] Dashboard served at localhost:8000/

## ✅ PHASE 2: Frontend 3-Layer Dashboard (COMPLETE)

- [x] Layer 1: Current State — Version, baseline, stats, key changes, conflicts, current decisions, Dichiarazione di Rilascio
- [x] Layer 2: Details — Full Decision Ledger table, detailed records, Requirements Baseline with versions & files, Nulla Osta, Conflicts, Dichiarazione
- [x] Layer 3: History — Searchable archive, version cards, all decisions with filters
- [x] Left Sidebar: Event timeline with layers and related items
- [x] Trace buttons on every item → Modal popup with full JSON
- [x] Stop Signal banner when active
- [x] Red/black professional theme

## ✅ PHASE 3: run.bat & seed.bat (COMPLETE)

- [x] run.bat: Starts backend + opens dashboard directly
- [x] seed.bat: Seeds comprehensive demo data

## ✅ PHASE 4: GitHub Actions (COMPLETE)

- [x] .github/workflows/decision-journal.yml

---

## 🚀 STARTUP INSTRUCTIONS

```batch
Step 1: docker-compose up -d     ← MongoDB
Step 2: run.bat                  ← Backend + Dashboard
Step 3: seed.bat                 ← Demo data
```
