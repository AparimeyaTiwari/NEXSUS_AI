# NEXSUS AI  
### Agent-Based Provider Data Validation & Confidence Scoring Platform  

**EY Techathon 6.0 – Detailed Solution Submission**

---

## 🚀 Overview

**NEXSUS AI** is an agent-based, workflow-driven platform built to solve a critical problem in the healthcare payer ecosystem: **inaccurate, outdated, and fragmented provider directory data**.

Insurance providers and third-party administrators (TPAs) depend on provider data for compliance, operations, and patient experience. However, manual and periodic verification methods fail to scale.  
NEXSUS AI enables a **single, continuously validated source of truth** using confidence-based automation and human-in-the-loop governance.

---

## ❗ Problem Statement

Provider directories across major healthcare payers suffer from systemic data quality issues:

- **40–80%** of provider contact data is inaccurate  
- Manual verification achieves only **60–70% accuracy**  
- Fully corrected data can take **117–280 days**  
- Patients often visit providers who no longer accept their plan, causing delays and unexpected costs  

These challenges arise from **manual, fragmented, and non-scalable verification processes**, increasing compliance risk (e.g., *No Surprises Act*) and degrading patient trust.

---

## 👥 Target Users

### Primary Users
- Payer Operations Teams  
- Provider Relations Teams  
- Compliance & Quality Assurance Teams  

### Secondary Users
- Healthcare Providers (for direct verification in low-confidence cases)

---

## 💡 Solution Overview & Value Proposition

NEXSUS AI replaces slow, manual audits with **continuous, automated provider data validation**:

- Establishes a **single source of truth** for provider directories  
- Uses **agentic workflows** to mimic real-world human verification steps  
- Automatically flags outdated or inconsistent records  
- Explains *why* data was changed using **Explainable AI**  
- Escalates only **high-risk records** to human review or provider outreach  

This approach reduces operational overhead while improving **accuracy, consistency, and regulatory readiness**.

---

## ⚙️ Methodology & Approach

The platform follows a **sequential, deterministic agent-based workflow**, orchestrated using **LangGraph**.

### Workflow

1. **Data Ingestion**  
   - NPI and basic provider details submitted via user action or scheduler  

2. **Asynchronous Processing**  
   - Tasks routed through **Celery + Redis**  

3. **AI Agent 1 – Data Validation**  
   - Cross-verifies data against NPI registry and trusted web sources  

4. **AI Agent 2 – Data Enrichment**  
   - Fetches licenses, affiliations, and credentials  

5. **AI Agent 3 – Confidence Scoring**  
   - Uses **XGBoost** to compute confidence score  
   - **SHAP** provides explainability  

6. **Decision Routing**
   - **≥ 88–90%** → Auto-approved and updated  
   - **60–90%** → Acceptable, monitored  
   - **< 60%** → Escalated to automated calling agent or human review  

7. **Directory Update & Reporting**
   - Canonical database updated  
   - Audit logs and validation reports generated  

---

## 📊 Impact Metrics

### Data Accuracy
- High-confidence provider records  
- Reduced duplicate and inconsistent entries  

### Operational Efficiency
- Time to validate 100 records  
- Reduced manual verification workload  

### Update Velocity
- Faster provider onboarding  
- Faster update propagation  

---

## 🧱 Technology Stack

### Core
- **Languages:** Python, SQL  
- **Backend:** FastAPI  
- **Database:** PostgreSQL (canonical provider database)  
- **Agent Orchestration:** LangGraph  
- **Async Processing:** Celery + Redis  

### Machine Learning & AI
- **Model:** XGBoost  
- **Explainability:** SHAP  

### Data Sources
- Web scraping (trusted provider websites)  
- External registries (NPI, state licensing sources)  

### Infrastructure
- Docker-based containerization  
- Cloud-ready, horizontally scalable design  

---

## 📌 Assumptions & Constraints

### Assumptions
- Initial deployment limited to one state (e.g., Massachusetts)  
- Provider data available via public registries or websites  

### Constraints
- Variable data quality across directories  
- Rate limits and compliance constraints  
- Regulatory requirements for auditability  

---

## 🔐 Security, Scalability & Governance

- Confidence-based escalation ensures **human-in-the-loop control**  
- Full audit logs for all data changes  
- Secure access and encrypted storage  
- Horizontally scalable via asynchronous workers  
- Modular agents allow easy extension to:
  - New states  
  - New data sources  
  - Additional agents (e.g., calling, retraining)

---

## 🧩 Components Demonstrated / Planned

- XGBoost-based confidence scoring engine  
- Explainable AI layer for decision transparency  
- Automated calling agent for low-confidence records  
- Geospatial confidence map for provider reliability  

---

## 🚧 Project Status

**Prototype / Proof of Concept**

Developed for **EY Techathon 6.0**, with core logic implemented in notebooks and workflow validated through architecture and flow diagrams.

---

## 👨‍💻 Team

**Team Name:** NEXSUS AI  

- **Aparimeya Tiwari** – Database & Confidence Scoring (XGBoost)  
- **Harshalee Malu** – Provider Ingestion & Directory Management  
- **Sahil Adit** – Data Validation, Enrichment & Orchestration  

---

## 📄 License

License to be added.
