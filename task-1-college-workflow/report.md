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

### Existing workflow observed

During my observation of the college's request-handling process, I found that requests are handled through email. Email provides a familiar communication channel, but request tracking may require staff to review messages and follow up manually, depending on the existing process.

The observation establishes email as the channel used. Further investigation is required to confirm how requests are assigned, prioritized, tracked, resolved, and communicated back to students.

### Proposed workflow: CampusFlow

CampusFlow is a prototype designed to centralize college-related requests. Students submit a request through a web form, select a category, and provide a description. The application stores the request in MySQL with a unique request ID and status. The staff demonstration interface allows the status to be updated as work progresses.

### Comparison

The observed workflow uses email for handling requests. The proposed workflow uses a structured web form and a database-backed request record. CampusFlow demonstrates request submission, persistent storage, and status updates using synthetic test data.

The prototype has not yet been deployed in the college or evaluated by college staff. Therefore, improvements in response time, workload, or request completion cannot yet be claimed as measured outcomes.

### Evidence and limitations

The email-based workflow was observed. The CampusFlow prototype was tested separately using synthetic data. No actual student emails or personal information were used as test data. Additional evidence is needed to establish the number of requests handled, the time spent on each request, and the current follow-up process.