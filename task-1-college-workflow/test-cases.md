# CampusFlow — Test Cases and Results

## 1. Testing Overview

CampusFlow was tested locally using synthetic demonstration data. The tests evaluate request submission, required-field validation, duplicate detection, database persistence, interface restrictions, authorization limitations, and failure recovery.

**Environment:** Python, Streamlit, and MySQL on a local development machine.

**Testing boundary:** These results apply only to the documented local prototype tests. They do not establish that the application is production-ready or securely integrated with a college system.

## 2. Test Cases

### TC-01: Normal Request Submission

**Objective:** Verify that a valid request can be submitted.

**Test data:** Synthetic student identifier, request category, and description.

**Steps:**
1. Open the CampusFlow application.
2. Enter the required request details.
3. Submit the request.
4. Check the displayed request ID and corresponding database record.

**Expected result:** The request is accepted, assigned a unique request ID, and stored in MySQL.

**Observed result:** A request was submitted and verified in MySQL.

**Status:** PASS.

### TC-02: Database Persistence

**Objective:** Verify that submitted request information is stored in MySQL and remains available after refreshing the application.

**Steps:**
1. Submit a synthetic request.
2. Verify the record in MySQL.
3. Refresh the application.
4. Check that the request remains available.
5. Verify a recorded status update in the database.

**Expected result:** The request and its saved status remain available.

**Observed result:** A request and its updated status were visible in MySQL.

**Status:** PASS for the documented persistence test.

### TC-03: Staff Status Update

**Objective:** Verify that the demonstration staff interface can update a request's status.

**Steps:**
1. Open the staff demonstration interface.
2. Locate a synthetic request.
3. Change its status from Open to In Progress.
4. Check the displayed status and database record.

**Expected result:** The status change is saved and displayed.

**Observed result:** A request status was changed to In Progress and verified.

**Status:** PASS for the demonstrated status update.

**Limitation:** The Staff selector does not authenticate a user or prove that the action is restricted to authorized staff.

### TC-04: Missing Required Information

**Objective:** Check that a request with missing required information is rejected.

**Steps:**
1. Open the request form.
2. Leave the description empty.
3. Submit the form.
4. Check the validation message and database record count.

**Expected result:** A validation warning appears, and the incomplete request is not saved.

**Observed result:** An empty description triggered the required-fields warning, and the request count remained unchanged.

**Status:** PASS for the tested empty-description case.

### TC-05: Duplicate Request

**Objective:** Check that a matching request is detected.

**Steps:**
1. Submit a synthetic request using a student identifier and description.
2. Submit another request with the same matching values while the first request remains open.
3. Check the duplicate warning and database record count.

**Expected result:** The application warns about the matching open request and avoids unintentionally creating a duplicate.

**Observed result:** The matching student identifier and description remained at one database record after the documented duplicate test.

**Status:** PASS for the documented test case.

**Limitation:** This does not establish that every possible duplicate pattern or simultaneous submission is handled correctly.

### TC-06: Student Interface Restriction

**Objective:** Check which controls are visible when the Student interface is selected.

**Steps:**
1. Select Student in the demonstration interface.
2. Inspect the available controls.
3. Check whether status-update controls are displayed.

**Expected result:** Staff status controls are hidden in the Student interface.

**Observed result:** Status-update controls were hidden when Student was selected.

**Status:** PASS for interface visibility only.

**Security limitation:** This is not a successful unauthorized-access security test. The role selector is not secure authentication, and server-side authorization has not been demonstrated.

### TC-07: Normal Database Availability

**Objective:** Check whether the application loads while MySQL is running normally.

**Steps:**
1. Ensure MySQL is running.
2. Open or refresh CampusFlow.
3. Check whether the application loads and accesses its data.

**Expected result:** The application operates under normal database availability.

**Observed result:** The application loaded normally after refreshing while MySQL was running.

**Status:** PASS for normal database availability.

### TC-08: Unauthorized Staff Action

**Objective:** Determine whether a user without appropriate permission can perform a restricted staff action.

**Expected result:** A user without valid authorization cannot perform restricted actions through either the interface or direct server-side requests.

**Observed result:** Secure authentication and server-side authorization have not been implemented or verified. Hiding controls in the Student interface is insufficient to establish access control.

**Status:** NOT VERIFIED.

**Required improvement:** Implement authentication and server-side role-based authorization, then test access restrictions in the authorized local test environment.

### TC-09: Database Failure and Recovery

**Objective:** Determine whether the application handles a database outage or failed database operation safely.

**Expected result:** The application displays a clear error, does not falsely report a successful submission, avoids unintended duplicate records on retry, and provides an appropriate recovery or escalation path.

**Observed result:** A controlled database outage and recovery test was not completed because the required service-control operation could not be performed with the available permissions.

**Status:** NOT TESTED.

**Required improvement:** Arrange a controlled test in the local development environment with appropriate permissions. Verify error handling, record consistency, retry behavior, and recovery before reporting this scenario as passed.

## 3. Test Summary

| Area | Result |
|---|---|
| Normal request submission | PASS |
| Database persistence | PASS |
| Staff status update | PASS for demonstrated action |
| Missing required information | PASS for tested case |
| Duplicate request | PASS for documented case |
| Student interface restrictions | PASS for visibility only |
| Normal database availability | PASS |
| Secure unauthorized-access prevention | NOT VERIFIED |
| Database failure and recovery | NOT TESTED |

## 4. Limitations

The tests used synthetic data in a local prototype. The results do not establish security, production readiness, complete error handling, or compatibility with institutional systems.

The Student/Staff selector is a demonstration feature rather than secure authentication. Unauthorized-access testing and database failure-recovery testing remain incomplete.

The actual college workflow has not been independently verified. All future tests should record the date, environment, steps, expected result, observed result, supporting evidence, and limitations. Untested scenarios must not be reported as successful.

## 5. Conclusion

The completed basic tests demonstrate that several CampusFlow functions work in the local synthetic-data environment. Further work is required to validate server-side authorization, database failure recovery, broader edge cases, and the proposed workflow with appropriate permission.
