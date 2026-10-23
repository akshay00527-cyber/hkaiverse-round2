# HKAIverse.ai Round 2 | Workflow Automation & CSE Curriculum Audit

**A practical, evidence-oriented approach to improving college workflows and aligning computer science education with industry needs.**

This repository contains two connected projects developed for the HKAIverse.ai Round 2 assignment: a college-request management prototype and a curriculum comparison tool. The work combines workflow analysis, application development, testing, curriculum review, and documented limitations.

## Project Overview

| Component | Purpose | Main Deliverable |
|---|---|---|
| Task 1 — CampusFlow | Structure college requests and enable request-status tracking | Streamlit application with MySQL integration |
| Task 2 — Curriculum Audit | Compare displayed CSE curriculum information with industry skill requirements | Curriculum dataset, audit report, and interactive comparison tool |

## Task 1 — CampusFlow: College Workflow Improvement

### Problem

College requests handled through email can be difficult to organize and track. The exact existing workflow, including staff handling and follow-up practices, requires further investigation.

### Proposed Solution

CampusFlow is a prototype that provides a structured interface for submitting college requests and tracking their progress.

**Key features**
- Submit requests using a structured form.
- Store request records in MySQL.
- Generate a request identifier for tracking.
- Display submitted requests in the staff interface.
- Update request status, including Open, In Progress, and Closed.
- Validate required fields and check for matching open requests.

### Implementation

- Python
- Streamlit
- MySQL
- SQL-based record verification

### Testing and Evidence

The documented prototype checks cover request submission, persistent storage, status updates, missing-field validation, duplicate-request handling, and student-interface controls.

Security testing and database-failure recovery have not been completed. The role selector is a demonstration feature, not secure authentication.

**Time-saving analysis:** Any estimated time savings are illustrative until measured against the actual college workflow. See `task-1-college-workflow/calculations.md`.

**Explore the evidence**
- [Workflow report](task-1-college-workflow/report.md)
- [Test cases](task-1-college-workflow/test-cases.md)
- [Evidence log](task-1-college-workflow/evidence-log.csv)
- [Time calculations](task-1-college-workflow/calculations.md)
- [Application source](campusflow-app/app.py)

## Task 2 — CSE Curriculum Audit

### Objective

Examine the available CSE curriculum information, compare it with selected industry job descriptions, and propose evidence-informed changes to strengthen industry readiness.

### Approach

1. Organize the available semester-wise course information.
2. Record sources, access dates, and verification limitations.
3. Compare course coverage with skills requested in selected job descriptions.
4. Classify proposed curriculum changes as Keep, Update, Add, Reduce, or Verify.
5. Document proposed AI-related exercises across five subjects.
6. Calculate the potential impact of proposed changes while distinguishing displayed units from verified academic credits.

### Interactive Curriculum Comparison Tool

The Streamlit tool allows reviewers to explore the curriculum dataset using available semester, subject-area, and recommendation filters. It also provides a proposed credit-impact calculator and verification checklist.

**Open the source files**
- [Curriculum comparison application](campusflow-app/curriculum_tool.py)
- [Curriculum dataset](task-2-curriculum-audit/curriculum.csv)
- [Curriculum audit report](task-2-curriculum-audit/report.md)
- [Job-description analysis](task-2-curriculum-audit/job-descriptions.md)
- [Source register](task-2-curriculum-audit/sources.md)
- [Credit calculations](task-2-curriculum-audit/credit-calculations.md)
- [AI exercise log](task-2-curriculum-audit/ai-use-log.md)

### Important Limitations

The available portal information is not yet confirmed as the official curriculum for the relevant admission batch. Displayed course units must not be treated as verified official credits. Semester VIII internship details remain pending verification, and job-description requirements should be checked against the original listings.

Proposed curriculum changes are recommendations, not approved institutional changes.

## Run the Applications Locally

### Prerequisites

- Python
- pip
- Streamlit
- MySQL, if using the database-backed CampusFlow workflow

### 1. Install dependencies

From the repository root:

```bash
pip install -r requirements.txt
```

### 2. Run CampusFlow

```bash
streamlit run campusflow-app/app.py
```

Configure database credentials locally in `.streamlit/secrets.toml` before using the MySQL-backed features. Never commit passwords, access tokens, or real student information.

### 3. Run the curriculum comparison tool

In another terminal:

```bash
streamlit run campusflow-app/curriculum_tool.py
```

The applications can run independently. CampusFlow uses the request-management workflow; the curriculum tool supports the curriculum audit.

## Repository Structure

```text
hkaiverse-round2/
├── campusflow-app/
│   ├── app.py
│   ├── curriculum_tool.py
│   └── data/
├── task-1-college-workflow/
│   ├── report.md
│   ├── evidence-log.csv
│   ├── test-cases.md
│   └── calculations.md
├── task-2-curriculum-audit/
│   ├── report.md
│   ├── curriculum.csv
│   ├── job-descriptions.md
│   ├── sources.md
│   ├── credit-calculations.md
│   └── ai-use-log.md
├── requirements.txt
├── .gitignore
└── README.md
```

## Responsible Use of Evidence and AI

- Distinguish observed facts from assumptions and proposed improvements.
- Report only tests that were actually performed.
- Keep unverified curriculum details and credit values clearly labelled.
- Document AI-assisted exercises and independently review their outputs.
- Avoid claiming measured impact, verified security, or institutional approval without supporting evidence.

## Project Goal

The goal is to demonstrate practical problem-solving: identify a real workflow worth improving, build and test a working prototype, examine curriculum-to-industry alignment, and present recommendations with transparent evidence and limitations.

**Repository:** [HKAIverse Round 2 on GitHub](https://github.com/akshay00527-cyber/hkaiverse-round2)
