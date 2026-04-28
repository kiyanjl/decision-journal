# Decision Journal System - Prototype

This is the fully mocked, end-to-end prototype of the **Decision Journal Layer**, designed as a read-only, non-intrusive final traceability and audit system.

## 🧠 What's inside?

This repository contains the full stack implementation based on your requirements:

1.  **Frontend Dashboard (`frontend/`)**: A responsive UI built with React (CDN-based for immediate execution, zero build step required). It features:
    *   Dynamic summary cards
    *   A problem-highlighting pane
    *   A detailed decision reasoning view
    *   An interactive event timeline
    *   A test coverage graph (using Chart.js)
    *   Historical version navigation.

2.  **Backend API (`backend/`)**: A FastAPI Python service that connects the UI to the database. It handles routing and querying for decisions, events, timelines, and history.

3.  **Database layer (`docker-compose.yml`)**: MongoDB schema configuration to persist the decision journal and events, ensuring full traceability across pipeline runs.

4.  **Mock Seed Script (`backend/main.py -> /seed`)**: A script built into the API that automatically provisions the MongoDB with realistic, interconnected data representing an AI Verification Pipeline that resulted in a `REJECTED` state (Version v1.2.0).

---

## 🚀 How to Run It

This mock is designed to run easily on your Windows machine with minimal setup.

### Prerequisites:
- Python 3
- Docker (to run MongoDB locally)

### Step 1: Start MongoDB
Open a terminal in this folder and start the database container:
```bash
docker-compose up -d
```

### Step 2: Run the Backend & Seed Data
Simply execute the batch script provided:
```cmd
run.bat
```
*This will set up a Python virtual environment, install FastAPI and PyMongo, start the server on port `8000`, and instantly seed the database with mock events.*

### Step 3: Open the Dashboard
Just double-click on `frontend/index.html` in your file explorer. It will open in your web browser and automatically fetch the data from the running backend.

---

## 💡 Key Design Principles Realized

*   **Non-intrusive:** The `Decision Journal` does not modify data; it merely queries MongoDB where pipeline events were collected.
*   **Traceability First:** The timeline effectively links `REQ-05` and `T-02` failures directly to the final decision.
*   **Zero-friction mock:** The frontend uses CDN links for React, Babel, and Tailwind so you can run the UI perfectly by just opening an HTML file, bypassing any local NPM/Node execution policy issues.
