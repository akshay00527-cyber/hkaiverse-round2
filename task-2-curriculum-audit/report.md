# Task 2 — CSE Curriculum Audit and Redesign Proposal

## 1. Executive Summary

This report proposes a structured audit and redesign of the B.Tech Computer Science and Engineering curriculum at ICFAI Foundation for Higher Education, Hyderabad, for the 2023–2027 admission batch.

The audit considers the curriculum's alignment with software engineering, artificial intelligence, machine learning, and related entry-level career pathways. It uses student academic portal evidence, an official programme reference, selected job descriptions, and AI-assisted subject exercises.

This is a preliminary proposal. The complete official curriculum applicable to the admission batch, all course credits, and programme regulations must be verified before the redesign can be finalized.

## 2. Programme and Scope

- **Institution:** ICFAI Foundation for Higher Education, Hyderabad
- **Programme:** B.Tech Computer Science and Engineering
- **Admission batch:** 2023–2027
- **Audit focus:** Programming, algorithms, databases, software engineering, AI/ML, cybersecurity, human-computer interaction, and practical project work.

The audit should cover all eight semesters, including prerequisite relationships, compulsory courses, electives, internships, and graduation requirements.

## 3. Evidence and Method

The preliminary course inventory was transcribed from student academic portal screenshots for Semesters I, II, III, and VI. The inventory records Semesters IV and V as missing, while several Semester VII and VIII values remain unverified.

The official programme reference recorded in `sources.md` is:

https://www.ifheindia.org/icfai-tech-school-hyderabad/icfaitech-btech-program-structure

The applicable curriculum version for the 2023 admission batch must be confirmed. Displayed portal units should not be assumed to equal official academic credits without verification.

The audit process is:

1. Verify course names, codes, credits, and prerequisites against the applicable official curriculum.
2. Map each course to the skills and learning outcomes it develops.
3. Compare these outcomes with dated employer job descriptions.
4. Identify content to keep, update, reduce, or add.
5. Calculate the effect on programme credits and check regulatory requirements.
6. Obtain voluntary feedback from faculty members or graduates where possible.
7. Record evidence, assumptions, limitations, and changes in the repository.

## 4. Preliminary Curriculum Observations

The currently transcribed inventory includes programming, data structures, algorithms, object-oriented programming, theory of computation, databases-related learning through earlier coursework, computer networks, cloud computing, computer vision, artificial intelligence, big data systems, and a special project.

The subjects identified for Semester VII include Natural Language Processing, an HCL/HCI subject whose official title must be confirmed, Introduction to Entrepreneurship, Ethical Hacking, and Deep Learning. Their exact official names, credits, and learning outcomes remain to be verified.

These observations are based on incomplete evidence and are not a claim that the entire programme has been audited.

## 5. Job-Market Comparison

The preliminary employer comparison is documented in `job-descriptions.md`, with links recorded in `sources.md`.

The selected roles represent different career directions:

- HCLTech: an analyst/support or generative-AI-related role.
- Accenture: an AI/ML computational-science-related role.
- Google: an AI/ML software engineering role.

The comparison should distinguish entry-level requirements from roles requiring previous experience. Job advertisements are examples of employer demand, not proof that every skill must become a compulsory university course.

Before final submission, recheck that each listing is accessible, record its actual title and access date, and extract specific skills from the listing rather than relying on the title alone.

## 6. Preliminary KEEP / UPDATE / REDUCE / ADD Recommendations

These recommendations are provisional until the official curriculum and course outcomes are verified.

| Action | Proposed direction | Reason |
|---|---|---|
| KEEP | Programming fundamentals | Foundation for further software development |
| KEEP | Data structures and algorithms | Supports problem-solving and technical interviews |
| KEEP | Object-oriented programming | Supports maintainable software design |
| KEEP | Computer networks | Provides networking fundamentals |
| KEEP | Database and data-management learning | Supports application development and analytics |
| UPDATE | Software project work | Include version control, testing, documentation, and code review |
| UPDATE | AI and machine-learning courses | Add reproducible experiments and careful evaluation |
| UPDATE | Cloud computing | Include deployment, monitoring, and cost awareness |
| UPDATE | Cybersecurity learning | Emphasize defensive practice, authorization, and secure coding |
| UPDATE | HCI/usability learning | Include accessibility and evidence-based usability evaluation |
| ADD | Data engineering and data quality practice | Supports reliable data pipelines and analytics |
| ADD | Responsible AI and evaluation | Addresses privacy, bias, reproducibility, and limitations |
| ADD | Portfolio-based capstone work | Demonstrates integrated, practical competence |
| REDUCE | Repeated introductory material, if confirmed | Free space only where a documented overlap exists |

A reduction should not be made simply to create room for new topics. Course syllabi and learning outcomes must first establish genuine duplication, and compulsory programme requirements must be preserved.

## 7. Proposed Credit-Change Plan

The assignment calls for changes affecting approximately 20–25% of programme credits. This target cannot yet be calculated because the full official credit total and several semester records are unavailable.

Once verified, the redesign should:

1. Identify the specific courses and credits that will be updated, reduced, or added.
2. Avoid double-counting credits affected by more than one recommendation.
3. Calculate the percentage of original programme credits affected.
4. Check total credits, prerequisites, compulsory courses, and graduation rules.
5. Document how any new course or revised course fits into the semester sequence.

See `credit-calculations.md` for the current data status and preliminary calculations.

## 8. AI-Assisted Subject Exercises

The `ai-use-log.md` file records AI-assisted exercises for five subjects:

1. **Natural Language Processing:** Stemming versus lemmatization.
2. **HCL/HCI:** Usability evaluation of a college student portal.
3. **Introduction to Entrepreneurship:** Evaluation of the SkillSwap Campus idea.
4. **Ethical Hacking:** Defensive security review of CampusFlow.
5. **Deep Learning:** Overfitting, underfitting, and experiment design.

AI-generated material is treated as a draft, not as verified evidence. Documentation, code execution, source checks, and actual experiments must be recorded accurately. Proposed tests must not be presented as completed tests.

## 9. Proposed Lab or Capstone

**Proposed title:** CampusFlow — Student Request Workflow and Analytics

CampusFlow is a small prototype for submitting and tracking student requests. It uses Streamlit as the interface and MySQL to store request records. The prototype provides a practical basis for studying workflow design, input validation, data persistence, and status tracking.

A proposed academic extension could include:

- A documented workflow with owners, approval boundaries, and exception handling.
- Role-based access control implemented and tested on the server side.
- Audit logging and safe handling of student information.
- Test cases for normal requests, missing information, duplicates, unauthorized access, and database failure.
- Aggregated reporting on request categories and resolution times, using synthetic or appropriately anonymized data.
- A test report that distinguishes implemented features from proposed improvements.

The current role selector is only a demonstration interface and must not be described as secure authentication or authorization. Actual database outage recovery and unauthorized-access tests remain outstanding.

## 10. Feedback and Validation Plan

The proposed next step is to request voluntary feedback from a faculty member or graduate on the relevance of the proposed changes, feasibility of the credit plan, and usefulness of the practical capstone.

If suitable participants cannot be reached, this limitation should be recorded. No feedback should be invented or represented as received without evidence.

The curriculum should also be reviewed against the applicable official regulations before any final recommendation is made.

## 11. Limitations

- The complete official curriculum for the 2023 admission batch has not yet been verified.
- Semester IV and V course data are missing from the current inventory.
- Semester VII and VIII credit values remain unverified.
- The selected job advertisements may change or become unavailable.
- Some recommendations are AI-assisted and require independent verification.
- The CampusFlow prototype is not a production student-management system.
- No actual faculty or graduate feedback should be claimed unless collected.
- The target of affecting 20–25% of programme credits remains uncalculated until the official credit total is established.

## 12. Conclusion

A useful curriculum redesign should preserve strong computing foundations while improving practical experience in software development, AI/ML evaluation, data management, security, usability, and project delivery.

The recommendations in this report are a starting point rather than a finalized curriculum. The next priority is to verify the full official programme structure, complete the missing course records, validate job-description evidence, calculate the credit changes, and document the resulting decisions transparently.