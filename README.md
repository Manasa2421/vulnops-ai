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