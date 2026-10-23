# Task 1: College Workflow Improvement

## 1. Project Overview

**Project name:** CampusFlow — College Request Management Prototype

CampusFlow is a prototype that demonstrates how college requests, such as placement-related queries, could be submitted, tracked, and updated through a structured workflow.

The prototype was developed using Python, Streamlit, and MySQL. It uses synthetic demonstration data and is not connected to any college system.

## 2. Problem Statement

College administrative queries may involve students submitting questions, staff reviewing them, requesting missing information, and communicating progress. The actual process, delays, and workload at the selected institution must be verified through permitted observation or voluntary interviews before making claims about current performance.

CampusFlow explores whether a centralized request dashboard could improve visibility, reduce duplicate submissions, and make request status easier to track.

## 3. Proposed Workflow

1. A student submits a request with a student identifier, category, and description.
2. The system validates required fields.
3. The system checks for a matching open request.
4. A valid request receives a unique request ID and is stored in MySQL.
5. Authorized staff review the request and update its status.
6. The request is closed when the issue is resolved.
7. If a database or application error occurs, the system should report the problem clearly and allow safe recovery without creating duplicate records. This recovery behavior requires further testing.
### CampusFlow Prototype Demonstration

I developed CampusFlow as a prototype for organizing college-related student requests. Students can submit requests under categories such as Placement Query, Document Query, Academic Query, and Other. Requests are stored in a MySQL database with a unique request ID. The staff demonstration interface allows a request's status to be updated from Open to In Progress or Closed.

During testing with synthetic data, I successfully submitted a request, verified its storage, viewed it in the staff interface, and changed its status to In Progress. Additional tests covered missing-field validation and duplicate-request prevention.

The prototype demonstrates a possible digital workflow improvement. However, the actual college workflow has not been independently verified, and time savings are illustrative rather than measured. The role selector is not secure authentication, and the prototype is not production-ready.

## 4. Prototype Features

- Request submission with required-field validation.
- Duplicate detection based on student identifier and description.
- Unique request identifiers.
- MySQL storage for request records.
- Request dashboard and status filtering.
- Demonstration of Student and Staff interfaces.
- Status updates stored in the database.

## 5. Testing and Results

The prototype was tested using synthetic data.

- **Normal submission:** A request was submitted and verified in MySQL.
- **Persistence:** A request and its updated status were visible in MySQL.
- **Missing information:** An empty description triggered the required-fields warning. The request count remained unchanged.
- **Duplicate request:** The database count for the matching student identifier and description remained one after the duplicate test.
- **Student interface restriction:** Status-update controls were hidden when Student was selected.
- **Normal database availability:** The app loaded normally after refreshing while MySQL was running.

Detailed scenarios, expected results, observed results, and limitations are documented in `test-cases.md`.

The unauthorized-access test is limited to checking which controls are visible. The role selector is not secure authentication, so server-side authorization has not been demonstrated. An actual database outage and recovery have also not been tested; these remain future tests.

## 6. Security and Reliability Limitations

The Student/Staff selector is a demonstration control, not authentication. A user may be able to select Staff, so the prototype cannot enforce real authorization.

MySQL provides structured database storage, but the current local setup is not a production deployment. Authentication, server-side role checks, database least-privilege access, input handling, backups, error handling, and recovery procedures require further work.

The application has been tested under normal database availability. Database outage behavior and recovery from a failed operation still need controlled testing.

## 7. Evidence Collection Plan

The next stage is to investigate one real college workflow with permission. Evidence may include dated observations, voluntary staff or graduate feedback, documented handoffs, approval requirements, exception cases, and estimates clearly distinguished from observed facts.

No private student records or confidential institutional information should be collected or committed to the repository.

At present, the proposed workflow is a prototype design. The actual college process has not yet been verified.

## 8. Evaluation and Time-Saving Method

The proposed workflow will be evaluated using five required scenarios:

1. Normal submission.
2. Missing information.
3. Duplicate request.
4. Unauthorized action.
5. Failed-step recovery.

For each scenario, the evaluation will record the expected outcome, observed outcome, evidence, and limitations.

Potential time savings will be estimated only after obtaining reasonable baseline estimates. Net time saved per request will be calculated as:

**Net time saved = current handling time − proposed handling time − additional review and support time.**

Any figures used before real observations are available will be labelled illustrative assumptions, not measured college results.

## 9. Next Steps

- Obtain permission to observe one real college workflow or record why access was unavailable.
- Document dated evidence and distinguish facts, estimates, and assumptions.
- Complete controlled tests for unauthorized access and database-failure recovery.
- Estimate net time saved, including review and support effort.
- Review the workflow with a volunteer staff member or graduate if available.
- Preserve test results and supporting evidence in the project repository.

## 10. Conclusion

CampusFlow demonstrates a possible approach to structured college request management using Streamlit and MySQL. It has passed several basic synthetic-data tests, including request creation, required-field validation, duplicate checking, and normal database operation. Further permitted investigation, security improvements, failure-recovery testing, and measured workflow data are needed before claiming operational benefits.
## Existing College Workflow and Proposed Improvement

### Current workflow: evidence status

The actual request-handling workflow at the selected college has not yet been independently verified. Email is considered a possible existing channel, but its use, handoffs, assignment process, approval requirements, and follow-up practices must be confirmed through authorized observation or voluntary interviews.

No claim about the college's current process, workload, delays, or performance is made without supporting evidence. The evidence log records this investigation as pending.

### Proposed workflow: CampusFlow

CampusFlow is a prototype designed to centralize college-related requests. Students submit a request through a web form, select a category, and provide a description. The application validates required fields, checks for a matching open request, assigns a unique request ID, and stores the request in MySQL.

The proposed workflow is:

1. **Submit — Student:** Enter the request category and description.
2. **Validate — System:** Check required fields and identify likely duplicates.
3. **Register — System:** Save a valid request and return its request ID.
4. **Review and assign — Responsible staff member:** Review the request and determine the appropriate department or next action. This is a proposed responsibility, not a verified college procedure.
5. **Approve or escalate — Designated authority:** Requests involving restricted records, exceptions, or decisions beyond staff authority should be referred to the appropriate authorized person. Approval rules must be confirmed with the institution before real use.
6. **Update — Responsible staff member:** Record progress and communicate the outcome through an approved channel.
7. **Close — Responsible staff member:** Close the request when the issue is resolved, retaining an appropriate record of its outcome.
8. **Recover — System and responsible staff member:** If submission or a database operation fails, show a clear error, avoid falsely confirming success, and provide a safe retry or escalation process. This behavior still requires controlled testing.

### Ownership and approval boundaries

The student is responsible for providing accurate request details. The system is responsible for basic validation, duplicate warnings, request IDs, and persistence. A designated staff member would review and route requests under a future approved process. Decisions requiring institutional authority must remain with the relevant authorized person; the prototype does not determine or grant approval.

The current Student/Staff selector is only a demonstration feature. It does not authenticate users or enforce secure authorization. CampusFlow must not be used to handle real confidential requests until authentication, server-side authorization, and institutional approval requirements are implemented and reviewed.

### Comparison and expected benefits

The current institutional process is still to be investigated. CampusFlow provides a testable alternative based on a structured form, a database-backed request record, and visible request statuses. Potential benefits include easier tracking, fewer duplicate submissions, and clearer ownership of follow-up work.

These benefits are hypotheses, not measured outcomes. A fair comparison requires documenting the existing process, measuring handling time, recording handoffs and exceptions, and testing the proposed workflow with permission.

### Evidence and limitations

CampusFlow was tested separately using synthetic data. Tests covered request submission, MySQL persistence, status updates, missing-field validation, duplicate detection, student-interface restrictions, and normal database availability. The role selector is not secure authentication, and database outage recovery has not been verified.

No real student emails, identifiers, marks, fee records, credentials, or confidential institutional information were used as test data. The actual college workflow investigation remains pending. Any future observations should be dated, supported by evidence, and labelled as observed facts, estimates, or assumptions.

### Net time-saving calculation

Net time saved per request will be estimated using:

**Net time saved = baseline handling time − proposed handling time − additional review and support time.**

For illustration only, if baseline handling takes 12 minutes, the proposed process takes 7 minutes, and additional review/support takes 2 minutes, the estimated net saving is 3 minutes per request. At an assumed 100 requests per month, that would equal 300 minutes, or 5 hours per month.

These values are illustrative assumptions, not measurements from the college. They must be replaced with evidence-based estimates when an authorized workflow investigation is possible. The calculation should include time spent correcting errors, reviewing duplicates, supporting users, and recovering from failures.