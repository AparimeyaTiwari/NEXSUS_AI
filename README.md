NEXSUS AI

Agent-Based Provider Data Validation & Confidence Scoring Platform

EY Techathon 6.0 – Detailed Solution Submission 

692ab8680198f_EY_Techathon_6 (1)

Overview

NEXSUS AI is an agent-based, workflow-driven platform designed to solve one of the most persistent challenges in the healthcare payer ecosystem: inaccurate, outdated, and fragmented provider directory data.

The solution targets insurance providers and third-party administrators (TPAs) who rely on accurate provider information for compliance, operations, and patient experience. By automating provider data validation and introducing confidence-based decisioning, NEXSUS AI enables a single, continuously verified source of truth for provider directories 

692ab8680198f_EY_Techathon_6 (1)

.

Problem Statement

Provider directories across major healthcare payers suffer from severe data quality issues:

40–80% of provider contact data is inaccurate

Manual verification achieves only 60–70% accuracy

Fully corrected data can take 117–280 days

Patients frequently encounter providers who no longer accept their plan, causing delays and unexpected costs

These issues stem from manual, periodic verification processes that do not scale across multiple directories and data sources, leading to inconsistencies, compliance risk (e.g., No Surprises Act), and poor patient experience 

692ab8680198f_EY_Techathon_6 (1)

.

Target Users

Primary Users:

Payer Operations Staff

Provider Relations Teams

Compliance and Quality Assurance Teams

Secondary Users:

Healthcare providers (for direct verification in low-confidence cases)

Solution Overview & Value Proposition

NEXSUS AI replaces slow, manual audits with continuous, automated provider data validation:

Establishes a single source of truth for provider data

Uses agentic workflows to mimic real-world human verification steps

Automatically flags incorrect or outdated records

Explains why data was changed using explainable AI

Escalates only high-risk cases to human review or provider outreach

This approach significantly reduces operational effort while improving accuracy, consistency, and regulatory readiness 

692ab8680198f_EY_Techathon_6 (1)

.

Methodology / Approach

The system follows a sequential, deterministic agent-based workflow, orchestrated using LangGraph:

Data Ingestion

NPI + basic provider details submitted via user action or scheduler

Async Processing Queue

Tasks routed through Celery + Redis for scalable execution

AI Agent 1 – Data Validation

Validates provider details against NPI registry and trusted web sources

AI Agent 2 – Data Enrichment

Fetches additional attributes (licenses, affiliations, credentials)

AI Agent 3 – Confidence Scoring

Uses XGBoost to compute a confidence score

SHAP provides explainability for decisions

Decision Routing

≥ 88–90% confidence: Auto-approved and updated

60–90% confidence: Acceptable, monitored

< 60% confidence: Escalated to automated calling agent or human review

Directory Update & Reporting

Canonical database updated

Audit logs and validation reports generated

(Refer to architecture and flowchart diagrams on pages 7–8) 

692ab8680198f_EY_Techathon_6 (1)

.

Impact Metrics

The solution’s effectiveness is measured using:

Data Accuracy

High-confidence provider records

Reduction in duplicate and inconsistent entries

Operational Efficiency

Time to validate 100 provider records

Reduction in manual verification workload

Update Velocity

Faster onboarding of new providers

Faster propagation of updates across systems

Technology Stack
Core Technologies

Languages: Python, SQL

Backend: FastAPI

Database: PostgreSQL (canonical provider database)

Agent Orchestration: LangGraph (workflow-based execution)

Async Processing: Celery + Redis

Machine Learning & AI

Model: XGBoost (confidence scoring)

Explainability: SHAP

Data Sources

Web scraping (trusted provider websites)

External registries (NPI, state licensing sources)

Infrastructure

Containerized deployment using Docker

Cloud-ready, horizontally scalable architecture

Assumptions & Constraints
Assumptions

Initial deployment limited to one state (e.g., Massachusetts)

Provider data is accessible via public registries or websites

Constraints

Inconsistent data quality across directories

Rate limits and compliance constraints for scraping and outreach

Regulatory requirements for auditability and transparency

Security, Scalability & Governance

Confidence-based escalation ensures human-in-the-loop control

Full audit logs for all data changes

Secure access and encrypted storage

Horizontally scalable using asynchronous workers

Modular agent design allows easy extension to:

New states

New data sources

Additional agents (e.g., calling, retraining)

Components Demonstrated / Planned

XGBoost-based confidence scoring engine

Explainable AI layer showing reasoning behind updates

Automated calling agent for low-confidence records

Geospatial confidence map visualizing provider reliability

Project Status

🚧 Prototype / Proof of Concept

This repository represents an early-stage implementation developed for EY Techathon 6.0, with core logic implemented in notebooks and workflow design validated through diagrams and demonstrations 

692ab8680198f_EY_Techathon_6 (1)

.

Team

Team Name: NEXSUS AI

Aparimeya Tiwari – Database & Confidence Scoring (XGBoost)

Harshalee Malu – Provider Ingestion & Directory Management

Sahil Adit – Data Validation, Enrichment & Orchestration

(Details from page 3) 

692ab8680198f_EY_Techathon_6 (1)

License

License to be added.