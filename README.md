# HKAIverse.ai Round 2 | Workflow Automation & CSE Curriculum Audit

**A practical, evidence-oriented approach to improving college workflows and aligning computer science education with industry needs.**

This repository contains two connected projects developed for the HKAIverse.ai Round 2 assignment: a college-request management prototype and a curriculum comparison tool. The work combines workflow design, application development, prototype testing, curriculum review, and documented limitations.

## Project Overview

| Component | Purpose | Main Deliverable |
|---|---|---|
| Task 1 — CampusFlow | Demonstrate a structured approach to college requests and request-status tracking | Streamlit application with MySQL integration |
| Task 2 — Curriculum Audit | Compare available CSE curriculum information with selected industry skill requirements | Curriculum dataset, audit report, and interactive comparison tool |

## Task 1 — CampusFlow: College Workflow Improvement

### Problem

College requests may be difficult to organize and track when handled through informal channels. The actual workflow, including staff handling, approvals, exceptions, and follow-up practices, has not yet been independently investigated. CampusFlow is therefore a prototype for a proposed improvement, not a verified replacement for an observed institutional process.

### Proposed Solution

CampusFlow provides a structured interface for submitting college requests and tracking their progress.

**Key features**

- Submit requests using a structured form.
- Store request records in MySQL.
- Generate a request identifier for tracking.
- Display submitted requests in the staff demonstration interface.
- Update request status: Open, In Progress, or Closed.
- Validate required fields and check for matching open requests.

### Implementation

- Python
- Streamlit
- MySQL
- SQL-based record verification

### Testing and Evidence

Documented prototype checks cover request submission, MySQL persistence, status updates, missing-field validation, duplicate-request handling, and student-interface controls.

Security testing and database-failure recovery have not been completed. The Student/Staff selector is a demonstration control, not secure authentication or server-side authorization. CampusFlow is not production-ready.

**Time-saving analysis:** Estimated time savings are illustrative assumptions, not measured outcomes. See `task-1-college-workflow/calculations.md`.

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

1. Organize available semester-wise course information.
2. Record source URLs, access dates, and verification limitations.
3. Compare curriculum coverage with skills listed in selected job descriptions.
4. Classify proposed changes as KEEP, UPDATE, ADD, REDUCE, or VERIFY.
5. Document AI-assisted exercises across five subjects.
6. Calculate the potential impact of proposed changes while distinguishing portal-displayed units from verified academic credits.

### Interactive Curriculum Comparison Tool

The Streamlit tool allows reviewers to explore the curriculum dataset using the available semester, subject-area, and recommendation filters. It also provides a proposed credit-impact calculator and a verification checklist.

**Explore the curriculum audit**

- [Curriculum comparison application](campusflow-app/curriculum_tool.py)
- [Curriculum dataset](task-2-curriculum-audit/curriculum.csv)
- [Curriculum audit report](task-2-curriculum-audit/report.md)
- [Job-description analysis](task-2-curriculum-audit/job-descriptions.md)
- [Source register](task-2-curriculum-audit/sources.md)
- [Credit calculations](task-2-curriculum-audit/credit-calculations.md)
- [AI exercise log](task-2-curriculum-audit/ai-use-log.md)

### Important Limitations

The available portal information has not yet been confirmed as the official curriculum applicable to the 2023 admission batch. Portal-displayed units must not be treated as verified official credits. Semester VIII internship details remain pending verification, and job-description requirements must be checked against the original listings.

The 20–25% programme-credit impact target remains unverified until the official programme-credit total and the final list of affected courses are established.

All curriculum changes are proposals, not approved institutional changes.

## Run the Applications Locally

### Prerequisites

- Python
- pip
- Streamlit
- MySQL, for the database-backed CampusFlow application

### 1. Install dependencies

From the repository root:

```bash
pip install -r requirements.txt
```

### 2. Configure and run CampusFlow

Configure database credentials locally in `.streamlit/secrets.toml`. Never commit passwords, access tokens, or real student information.

Run:

```bash
streamlit run campusflow-app/app.py
```

### 3. Run the curriculum comparison tool

In a separate terminal:

```bash
streamlit run campusflow-app/curriculum_tool.py
```

The applications can run independently. CampusFlow demonstrates request management, while the curriculum tool supports the curriculum audit.

## Repository Structure

```text
hkaiverse-round2/
├── campusflow-app/
│   ├── app.py
│   ├── curriculum_tool.py
│   └── data/
│       └── requests.csv
├── task-1-college-workflow/
│   ├── calculations.md
│   ├── evidence-log.csv
│   ├── report.md
│   └── test-cases.md
├── task-2-curriculum-audit/
│   ├── ai-use-log.md
│   ├── credit-calculations.md
│   ├── curriculum.csv
│   ├── job-descriptions.md
│   ├── report.md
│   └── sources.md
├── .gitignore
├── README.md
└── requirements.txt
```

## Responsible Use of Evidence and AI

- Distinguish observed facts from assumptions and proposed improvements.
- Report only tests that were actually performed.
- Clearly label unverified curriculum details and credit values.
- Document AI-assisted exercises and independently review their outputs.
- Do not claim measured impact, verified security, or institutional approval without supporting evidence.
- Use synthetic demonstration data and protect credentials and personal information.

## Submission References

- **Repository:** [HKAIverse Round 2 on GitHub](https://github.com/akshay00527-cyber/hkaiverse-round2)
- **Latest commit:** [e94b2a4e9945acca8f224403bc065d3836409b02](https://github.com/akshay00527-cyber/hkaiverse-round2/commit/e94b2a4e9945acca8f224403bc065d3836409b02)
- **Release:** [v1.0.0](https://github.com/akshay00527-cyber/hkaiverse-round2/releases/tag/v1.0.0) — publish and verify this release before relying on the link.

## Project Goal

Demonstrate practical problem-solving by designing a proposed workflow improvement, building and testing a working prototype, examining curriculum-to-industry alignment, and presenting recommendations with transparent evidence and limitations.