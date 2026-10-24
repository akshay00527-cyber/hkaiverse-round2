# Task 1: College Workflow Improvement

## 1. Project Overview

**Project name:** CampusFlow — College Request Management Prototype

CampusFlow is a prototype that demonstrates how college requests, such as placement-related queries, can be submitted, tracked, and updated through a structured workflow.

The prototype was developed using Python, Streamlit, and MySQL. It uses synthetic demonstration data and is not connected to any college system.

## 2. Problem Statement

College administrative requests may involve students submitting queries, staff reviewing them, requesting missing information, assigning responsibility, obtaining approvals, and communicating outcomes. The actual process, delays, and workload at the selected institution have not been independently verified.

CampusFlow explores whether a centralized request dashboard could improve request visibility, reduce duplicate submissions, and make request status easier to track.

## 3. Current Workflow: Hypothetical Baseline

**Evidence status:** The actual college workflow has not been independently verified. The following workflow is hypothetical and is provided for analysis only.

1. A student submits a request through an existing communication channel.
2. A staff member receives and reviews the request.
3. If information is missing, the staff member asks the student for clarification.
4. The request is directed to the appropriate office or responsible person.
5. An authorized person reviews and approves the request if required.
6. The responsible staff member communicates the outcome to the student.

Possible issues include missing information, duplicate requests, unclear ownership, delayed approvals, and limited visibility into request status. These are potential risks, not confirmed problems at the selected institution.

The existing communication channel, responsibilities, approval rules, handoffs, and processing times must be verified through permitted observation or voluntary interviews. Email is a possible channel, but its use has not been confirmed.

## 4. Proposed Workflow: CampusFlow

1. **Submit:** The student enters the request category and description.
2. **Validate:** The system checks required fields and identifies likely duplicate requests.
3. **Register:** A valid request is assigned a unique request ID and stored in MySQL.
4. **Review and assign:** The responsible staff member reviews the request and determines the appropriate next step.
5. **Approve or escalate:** Requests requiring institutional authority or an exception are referred to the appropriate authorized person.
6. **Update:** The responsible staff member records progress and communicates the outcome through an approved channel.
7. **Close:** The request is closed after the issue is resolved.
8. **Recover:** If an application or database operation fails, the system should display a clear error and provide a safe retry or escalation process. This recovery behavior requires further testing.

These steps describe a proposed workflow, not verified institutional procedures.

### Ownership and Approval Boundaries

The student is responsible for providing accurate information. The system handles required-field validation, duplicate checks, request IDs, and database storage. A designated staff member would review, route, and update requests under an approved process. Decisions requiring institutional authority must remain with the relevant authorized person.

The Student/Staff selector in the prototype is only a demonstration feature. It is not secure authentication and does not establish server-side authorization.

## 5. Prototype Features

- Request submission through a Streamlit interface.
- Required-field validation.
- Duplicate detection based on student identifier and description.
- Unique request identifiers.
- MySQL storage for request records.
- Request dashboard and status filtering.
- Student and Staff demonstration interfaces.
- Database-backed request status updates.

The prototype uses synthetic data and is not integrated with institutional systems.

## 6. Testing and Results

The prototype was tested using synthetic data in a local demonstration environment.

1. **Normal submission — PASS:** A request was submitted and verified in MySQL.
2. **Database persistence — PASS:** A request and its updated status remained visible in MySQL.
3. **Missing information — PASS:** An empty description triggered a required-fields warning, and the request count remained unchanged.
4. **Duplicate request — PASS:** The matching student identifier and description remained at one database record after the documented duplicate test.
5. **Student interface restriction — PASS for interface visibility only:** Status-update controls were hidden when Student was selected.
6. **Normal database availability — PASS:** The application loaded after refreshing while MySQL was running.
7. **Unauthorized access — NOT VERIFIED:** Secure authentication and server-side authorization were not demonstrated.
8. **Database failure and recovery — NOT TESTED:** A controlled database outage and recovery test was not completed.

The interface restriction does not prove that unauthorized users are prevented from performing restricted actions. The database failure-recovery behavior also remains unverified. Detailed test cases and limitations are documented separately in test-cases.md.

## 7. Security and Reliability Limitations

The Student/Staff selector is not authentication. The local prototype is not production-ready and should not be used for confidential student requests.

Further work is required to implement and review authentication, server-side role-based authorization, least-privilege database access, safe input handling, sensitive-data protection, appropriate logging, backups, and recovery procedures.

The current results establish that several basic functions work in the local synthetic-data environment. They do not establish that the application is fully secure or ready for institutional use.

## 8. Evidence Collection Plan

The next stage is to investigate one real college workflow with permission or document that access was unavailable.

If permitted, evidence collection may include dated observations, voluntary staff or graduate feedback, documented handoffs, confirmed approval requirements, exception cases, and baseline handling-time estimates.

Observed facts, estimates, assumptions, and unverified details must be clearly distinguished. No private student records, credentials, or confidential institutional information should be collected or committed to the repository.

The actual college workflow investigation remains pending.

## 9. Five Required Evaluation Scenarios

**Scenario 1: Normal submission**

Expected result: A valid request receives a unique request ID and is saved in the database.

Evidence status: Basic submission and persistence were tested successfully.

**Scenario 2: Missing information**

Expected result: An incomplete request is rejected with a clear validation message and is not saved.

Evidence status: Required-field validation was tested successfully for an empty description.

**Scenario 3: Duplicate request**

Expected result: A matching open request triggers a warning and is not unintentionally duplicated.

Evidence status: Duplicate detection was tested for the documented student identifier and description.

**Scenario 4: Unauthorized action**

Expected result: A user without the required permission cannot perform restricted staff actions.

Evidence status: Secure authorization has not been implemented or verified. Hiding interface controls is insufficient to demonstrate security.

**Scenario 5: Failed-step recovery**

Expected result: The application reports failure clearly, avoids falsely confirming success, and provides a safe retry or escalation route without unintended duplicate records.

Evidence status: A controlled database outage and recovery test has not been completed.

Expected outcomes are requirements, not claimed test results. Future tests should record the date, conditions, expected outcome, observed outcome, supporting evidence, and limitations.

## 10. Evaluation and Time-Saving Calculation

Net time saved per request will be calculated using the following formula:

**Net time saved = baseline handling time − proposed handling time − additional review and support time.**

For illustration only, assume the following values:

- Baseline handling time: 12 minutes per request.
- Proposed handling time: 7 minutes per request.
- Additional review and support time: 2 minutes per request.

Illustrative net time saved:

12 − 7 − 2 = 3 minutes per request.

If the assumed monthly volume is 100 requests:

3 × 100 = 300 minutes, or 5 hours per month.

These figures are illustrative assumptions, not measured college results. The request volume and handling times must be replaced with reasonable, documented estimates when evidence becomes available. A fair calculation should include correction work, duplicate review, user support, and failure recovery.

## 11. Next Steps

- Obtain permission to observe a real college workflow or document that access was unavailable.
- Confirm actual communication channels, responsibilities, approval rules, and handoffs where possible.
- Complete and document the five evaluation scenarios without presenting untested scenarios as passed.
- Conduct controlled authorization and failure-recovery tests when feasible.
- Replace illustrative time assumptions with evidence-based estimates when available.
- Seek feedback from a willing staff member or recent graduate if available.
- Preserve dated evidence and update the project repository.

## 12. Conclusion

CampusFlow demonstrates a possible approach to structured college request management using Streamlit and MySQL. Basic tests with synthetic data passed for request submission, persistence, required-field validation, duplicate checking, interface visibility, and normal database availability.

The actual college workflow has not been independently verified. Secure authorization, database failure recovery, and measured institutional benefits remain incomplete or unverified. CampusFlow should therefore be treated as a demonstration prototype, not a verified replacement for an existing college process or a production-ready application.
