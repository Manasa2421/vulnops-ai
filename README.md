# VulnOps AI

AI-powered vulnerability operations platform for scanning software repositories, tracking security findings, and supporting vulnerability triage workflows.

**Project Status:** Active Development

## Overview

VulnOps AI is a security engineering portfolio project designed to explore how modern vulnerability management platforms can combine automated security scanning, asynchronous processing, structured finding management, and AI-assisted triage.

The platform is being built incrementally with production-oriented engineering practices including automated testing, relational data modeling, background workers, containerization, and CI/CD.

## Why This Project?

Large engineering organizations may operate thousands of repositories and continuously receive security findings from multiple scanning systems.

Managing those findings introduces challenges such as:

- tracking scan execution and failures
- normalizing findings from different scanners
- identifying duplicate vulnerabilities
- maintaining finding lifecycle state
- attributing findings to repositories and owners
- processing scans asynchronously
- prioritizing security findings
- providing engineers with actionable vulnerability information

VulnOps AI is being built to demonstrate solutions to these types of vulnerability operations problems.

## Technology Stack

### Currently Implemented

| Area | Technology |
|---|---|
| Programming Language | Python 3.12 |
| Backend Framework | FastAPI |
| API Design | REST API, OpenAPI / Swagger |
| Application Server | Uvicorn |
| Testing | pytest, FastAPI TestClient, HTTPX |
| Version Control | Git, GitHub |

### Planned / In Development

| Area | Technology |
|---|---|
| Database | PostgreSQL, SQLAlchemy |
| Asynchronous Processing | Redis, Celery |
| Security Scanning | Bandit, extensible scanner integrations |
| AI / LLM | LLM APIs, agent-assisted vulnerability triage |
| Frontend | React, TypeScript |
| Containerization | Docker, Docker Compose |
| Orchestration | Kubernetes |
| CI/CD | GitHub Actions |
| Configuration & Secrets | Environment variables, secret-management patterns |

## Engineering Skills

### Currently Demonstrated

- Python backend development
- FastAPI REST API development
- OpenAPI / Swagger documentation
- Automated API testing with pytest
- HTTP endpoint testing with FastAPI TestClient
- Git and GitHub version-control workflow
- Incremental, test-driven development practices

### Project Roadmap Skills

As the platform develops, the project will demonstrate:

- PostgreSQL and relational data modeling
- SQL-based data reconciliation
- Repository and asset inventory management
- Vulnerability scanning
- Finding normalization
- Vulnerability lifecycle management
- Finding fingerprinting and deduplication
- Asynchronous worker and job-queue architecture
- Retry and failure handling
- LLM-assisted vulnerability analysis and triage
- React and TypeScript frontend development
- Docker containerization
- Kubernetes orchestration
- CI/CD automation

## Current Architecture

```text
Repository
    |
    v
FastAPI Backend
    |
    +---- Health & API Endpoints
    |
    +---- Automated Tests

Planned Architecture

Repository
    |
    v
FastAPI API
    |
    v
Redis / Worker Queue
    |
    v
Security Scanner Workers
    |
    v
Finding Normalization
    |
    +---- Deduplication
    +---- Lifecycle Management
    +---- Reconciliation
    +---- AI-Assisted Triage
    |
    v
PostgreSQL
    |
    v
React + TypeScript Dashboard