# CampusFlow Test Report

**Project:** CampusFlow - College Request Management Prototype
**Report prepared:** 23 October 2026
**Test dates:** Individual observations are recorded in `evidence-log.csv`; some tests were performed on an earlier prototype version.
**Environment:** Windows, Python, Streamlit, MySQL
**Data:** Synthetic demonstration data only


## 1. Purpose and scope

This test report evaluates whether CampusFlow can accept a college-service request, validate required information, prevent a duplicate request in the tested scenario, store records in MySQL, and support a basic status update.

The tests evaluate the prototype, not the security or performance of a live college system. Results are reported as observed; expected behavior is not treated as a successful test.

## 2. Test summary

| ID | Scenario | Expected result | Observed result | Status |
|---|---|---|---|---|
| TC-01 | Normal request | Request receives a unique ID and is saved | A synthetic request was created and verified in MySQL | PASS |
| TC-02 | Persistent storage | Saved record remains available after refresh | The record and status were verified using a MySQL query | PASS |
| TC-03 | Staff status update | Status change is saved | Status changed to In Progress and was verified in MySQL | PASS |
| TC-04 | Missing information | Validation warning; no incomplete request is inserted | Warning appeared; the tested record count remained unchanged | PASS |
| TC-05 | Duplicate request | Matching open request is rejected without another record | Matching record count remained one in the tested case | PASS |
| TC-06 | Student interface | Staff controls are hidden in Student mode | Status-update controls were hidden | PASS - interface only |
| TC-07 | Normal database availability | App loads while MySQL is running | App loaded normally while the database was available | PASS |
| TC-08 | Unauthorized staff action | A user without staff authorization cannot change status | No authentication or server-side staff authorization is implemented; a security rejection was not verified | NOT IMPLEMENTED / NOT TESTED |
| TC-09 | Database failure and recovery | Safe error message; successful recovery after service restoration | Attempt to stop MySQL was blocked by insufficient permissions | BLOCKED - NOT VERIFIED |

## 3. Detailed observations

### TC-01 - Normal request

**Method:** Submit a request with the required information using synthetic data.

**Observed result:** A request was created successfully and its record was found in the `campusflow.requests` table.

**Conclusion:** Basic request creation and database storage worked in the tested case.

### TC-02 - Persistent storage

**Method:** Inspect the saved record and status in MySQL after the application interaction.

**Observed result:** The record and status were present in MySQL.

**Limitation:** This is not a backup, disaster-recovery, or data-integrity audit.

### TC-03 - Status update

**Method:** Change a request to In Progress using the Staff demonstration interface.

**Observed result:** The updated status was verified in MySQL.

**Limitation:** The Staff selector is a demonstration control, not verified staff authentication.

### TC-04 - Missing information

**Method:** Submit a request with an empty description.

**Expected result:** The application warns the user and does not insert an incomplete request.

**Observed result:** The application displayed a required-fields warning, and the tested record count remained unchanged.

**Conclusion:** Required-field validation worked in this scenario.

### TC-05 - Duplicate request

**Method:** Submit the same open request again using the same synthetic tester and description.

**Expected result:** The application rejects the duplicate and retains one matching record.

**Observed result:** The matching MySQL record count remained one.

**Limitation:** This does not prove protection against concurrent submissions or every variation of duplicate text.

### TC-06 - Student interface restriction

**Method:** Select Student mode and inspect the available controls.

**Observed result:** Staff status-update controls were hidden.

**Conclusion:** The interface behaved as expected.

**Security limitation:** Hiding controls is not authorization. The current role selector permits a user to select Staff. Real deployment requires authenticated identities and server-side role checks.

### TC-07 - Normal database availability

**Method:** Refresh the application while MySQL is running.

**Observed result:** The application loaded normally.

**Limitation:** Normal operation does not demonstrate outage handling or recovery.

### TC-08 - Unauthorized request

**Objective:** Assess whether staff-only actions are protected from users without verified staff permissions.

**Inspection:** The app uses a Student/Staff role selector. It does not implement verified user authentication or server-side staff authorization.

**Result:** Unauthorized-access prevention has not been established. The absence of authorization was identified through code inspection; an actual authenticated access-control test was not completed.

**Status:** NOT IMPLEMENTED / NOT TESTED.

**Required improvement:** Add authenticated accounts, enforce staff permissions on the server for every status-changing operation, and test requests made without valid staff authorization before considering deployment.

### TC-09 - Database failure and recovery

**Objective:** Assess behavior during a temporary MySQL outage.

**Initial state:** MySQL80 was confirmed running.

**Test attempt:** An attempt to stop the service failed because of insufficient permissions.

**Result:** The outage could not be induced, so error handling and recovery were not verified.

**Status:** BLOCKED - test not completed.

**Recovery plan:** In an authorized test environment, stop the database, attempt a request, and check that the app reports failure without claiming the request was saved. Restore MySQL, reload the app, and verify that existing records remain available and retrying does not create unintended duplicates.

## 4. Five required synthetic workflow cases

These five cases map directly to the assignment. The results below distinguish completed tests from scenarios whose behavior remains unverified.

| Required case | Synthetic input or action | Expected behavior | Evidence and current status |
|---|---|---|---|
| Normal | Placement Query with all required fields | Create a unique request ID, save the record, set status to Open | Basic request creation was tested - PASS |
| Missing information | Leave the description empty | Show validation warning and do not create a request | Previously tested - PASS |
| Duplicate | Submit the same open request twice for the same synthetic tester | Reject the duplicate and retain one matching record | Previously tested - PASS for the tested case |
| Unauthorized request | Attempt a staff status change without verified staff authorization | Reject the operation and preserve the existing status | Not implemented or verified - NOT TESTED |
| Failed step | Attempt a request while MySQL is unavailable | Show a clear failure; do not falsely confirm saving; recover safely after database restoration | Outage test blocked by permissions - BLOCKED |

The normal, missing-information, and duplicate cases have recorded evidence. The unauthorized and failed-step cases are requirements for the proposed system, not passed tests.

## 5. Limitations and next steps

1. The app is a prototype, not a production-ready college service.
2. The Student/Staff selector is not secure authentication.
3. Database outage and recovery behavior remains unverified.
4. Tests do not establish behavior under heavy load, concurrent submissions, or all possible input variations.
5. The app tests use synthetic data and do not establish how the actual college currently handles requests.
6. The workflow's real steps, handoffs, approval rules, and exceptions must be supported by the separate dated evidence log. Unobserved details must be labelled as assumptions or items requiring confirmation.

Before any live deployment, implement authentication and authorization, test database failure and recovery, add appropriate logging and backups, and obtain approval from the responsible college authority.

## 6. Overall result

The tested prototype scenarios passed for normal request creation, persistent storage, a basic status update, missing-field validation, duplicate checking in the tested case, student-interface restrictions, and normal database availability.

Unauthorized-access prevention and database failure recovery remain unverified. No claim is made that the prototype is secure, production-ready, or proven to improve the actual college workflow.
