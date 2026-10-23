# CampusFlow Test Cases

**Project:** CampusFlow — College Request Management Prototype  
**Test date:** 22 October 2026  
**Test environment:** Windows, Python, Streamlit, MySQL  
**Test data:** Synthetic demonstration data only

## 1. Test Results

| Test ID | Action | Expected result | Observed result | Status |
|---|---|---|---|---|
| TC-01: Normal request | Submit a request with the required information | Request is created with a unique ID and saved in MySQL | Request CF-741D25E9 was created and verified in MySQL | PASS |
| TC-02: Persistent storage | Check the saved request and status in MySQL after app refresh | The request remains stored | Request record and status were verified using a MySQL query | PASS |
| TC-03: Status update | Change a request to In Progress using the Staff demo interface | Status is updated and saved | Status In Progress was verified in MySQL | PASS |
| TC-04: Missing information | Submit a request with an empty description | Validation warning appears and no request is created | The app displayed “Please fill in both required fields.” The request count remained 1 for STU002 | PASS |
| TC-05: Duplicate request | Submit the same open request using the same student identifier and description | A duplicate warning appears and no duplicate record is created | The matching MySQL record count remained 1 | PASS |
| TC-06: Student interface restriction | Select Student and inspect status-update controls | Status-update controls are hidden from the Student interface | The status-update controls were hidden | PASS — UI only |
| TC-07: Normal database availability | Refresh the app while MySQL is running | The app loads without an error | The app loaded normally after refreshing | PASS |
| TC-08: Unauthorized access | Attempt a staff status update without valid staff authentication | The system rejects unauthorized actions | Not tested. The current role selector is not secure authentication | NOT TESTED |
| TC-09: Database failure recovery | Simulate a database outage, restore service, and verify the records | The app reports the failure safely and recovers without data loss or duplicate records | An actual outage and recovery have not been tested | NOT TESTED |

## 2. Detailed Test Notes

### TC-01: Normal request

- **Purpose:** Verify that a request can be submitted and stored.
- **Observed result:** A synthetic request was submitted successfully.
- **Database verification:** Request ID CF-741D25E9 was present in the `campusflow.requests` table.
- **Conclusion:** Basic request creation and MySQL storage worked in the tested scenario.

### TC-02: Persistent storage

- **Purpose:** Verify that request data is stored in MySQL rather than only in temporary application state.
- **Observed result:** The request record and its status were verified through a MySQL query.
- **Limitation:** This confirms the tested record was stored; it does not constitute a full backup or disaster-recovery test.

### TC-03: Status update

- **Purpose:** Check whether a request status can be changed and saved.
- **Observed result:** The request status was updated to In Progress and verified in MySQL.
- **Limitation:** The Staff role is a demonstration selector, not authenticated staff access.

### TC-04: Missing information

- **Purpose:** Check validation of required fields.
- **Observed result:** When the description was left empty, the application displayed “Please fill in both required fields.”
- **Database verification:** The number of records for student identifier STU002 remained 1.
- **Conclusion:** The incomplete request was not inserted in the tested scenario.

### TC-05: Duplicate request

- **Purpose:** Check whether an identical open request is prevented from being created again.
- **Observed result:** The matching record count remained 1 after the duplicate test.
- **Conclusion:** Duplicate prevention worked for the tested student identifier and description.
- **Limitation:** This does not establish duplicate prevention under concurrent submissions or every possible input variation.

### TC-06: Student interface restriction

- **Purpose:** Check whether status-update controls are hidden when Student is selected.
- **Observed result:** The status-update controls were hidden.
- **Conclusion:** The interface restriction worked in the tested scenario.
- **Security limitation:** Hiding controls is not secure authorization. A user may be able to select Staff. Production use would require authenticated accounts and server-side authorization checks.

### TC-07: Normal database availability

- **Purpose:** Check normal application behavior while MySQL is running.
- **Observed result:** The app loaded normally after refreshing.
- **Conclusion:** Normal database availability was confirmed in this test.
- **Limitation:** This was not an outage simulation and does not prove failure recovery.

## 3. Untested Scenarios and Recovery Plan

### TC-08: Unauthorized access

**Current status:** Not tested.

The current role selector is not secure authentication. A future test should attempt a status update without valid staff credentials and verify that the server rejects the operation. The application should use authenticated accounts and server-side role checks before this test can establish access-control behavior.

### TC-09: Database failure recovery

**Current status:** Not tested.

A future controlled test should simulate a database outage in a safe test environment. The application should show a clear error, avoid falsely reporting a successful submission, and reconnect safely after the database is restored. The test should verify that retries do not create duplicate records or lose successfully saved requests.

## 4. Overall Result

The prototype passed the tested scenarios for normal request creation, database storage, status updates, missing-field validation, duplicate checking, student-interface restrictions, and normal database availability.

The unauthorized-access and database-failure recovery scenarios remain untested. The current prototype is for demonstration only and is not production-ready.

All test data is synthetic. These results do not establish how the actual college currently handles administrative requests.
## 5. Five Synthetic Workflow Scenarios

These scenarios evaluate how CampusFlow handles different request types. They use synthetic data and do not represent actual student cases.

| Scenario | Synthetic request | Expected result | Evaluation |
|---|---|---|---|
| SC-01 | Placement Query: “Need information about placement registration.” | Request is saved with a unique ID and Open status. | Normal submission was tested; use the recorded test evidence. |
| SC-02 | Document Query: “Need information about obtaining a transcript.” | Request is saved under the Document Query category. | Test this scenario if it has not already been performed. |
| SC-03 | Academic Query: “Need clarification about an examination timetable.” | Request is saved under the Academic Query category. | Test this scenario if it has not already been performed. |
| SC-04 | Request with an empty description. | Validation warning appears and no request is created. | Previously tested; the record count remained unchanged. |
| SC-05 | Submit the same open request twice using the same student identifier and description. | The duplicate is rejected and no extra record is created. | Previously tested; the matching record count remained one. |

### Evaluation limitations

The normal submission, missing-description, and duplicate-request scenarios have recorded test evidence. The Document Query and Academic Query scenarios must be tested and their actual results recorded before they can be marked as passed. Expected results alone do not constitute test evidence.