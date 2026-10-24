# Task 2 — CSE Curriculum Audit and Redesign Proposal

## 1. Executive Summary

This report presents a preliminary audit and redesign proposal for the B.Tech Computer Science and Engineering programme at ICFAI Foundation for Higher Education (IFHE), Hyderabad, for the 2023–2027 admission batch.

The audit examines the balance between computing fundamentals, practical software development, artificial intelligence and machine learning, cybersecurity, data management, human-computer interaction, and project work. It uses student academic portal screenshots, an official programme reference, selected employer job descriptions, and AI-assisted subject exercises.

The current `curriculum.csv` contains **152 portal-displayed units across Semesters I–VII**. These are arithmetic totals of the entries recorded in the file, not independently verified official academic credits. The applicable official curriculum version for the 2023 admission batch, the equivalence of displayed units to official credits, and Semester VIII internship requirements remain unverified.

The redesign recommendations are proposals for review, not approved institutional curriculum changes. The percentage of official programme credits affected by the proposed changes has not yet been calculated because the official credit denominator and final list of affected courses have not been verified.

## 2. Programme and Scope

- **Institution:** ICFAI Foundation for Higher Education, Hyderabad
- **Programme:** B.Tech Computer Science and Engineering
- **Admission batch:** 2023–2027
- **Audit focus:** Programming, algorithms, databases, software engineering, AI/ML, data engineering, cybersecurity, HCI, and practical project work.

The intended audit scope covers all eight semesters, including course prerequisites, compulsory requirements, electives, internships, projects, and graduation rules.

## 3. Evidence and Method

The preliminary course inventory in `curriculum.csv` was transcribed from student academic portal screenshots. Course codes, titles, displayed units, and official credit equivalence require verification against the curriculum applicable to the 2023 admission batch. Semester VIII internship credits and requirements have not yet been established.

The official programme reference recorded in `sources.md` is:

https://www.ifheindia.org/icfai-tech-school-hyderabad/icfaitech-btech-program-structure

The applicable curriculum and regulations for the 2023 admission batch have not yet been independently confirmed. Portal-displayed units must not be treated as official academic credits until their equivalence is verified.

The audit method is:

1. Verify course codes, titles, credits, learning outcomes, and prerequisites against the applicable official curriculum.
2. Map each course to the skills and learning outcomes it develops.
3. Compare those outcomes with specific, dated employer job descriptions.
4. Propose KEEP, UPDATE, REDUCE, and ADD decisions with evidence-based reasons.
5. Calculate the effect of the proposed changes on programme credits without double-counting.
6. Check prerequisites, compulsory requirements, semester workload, and regulatory constraints.
7. Seek voluntary feedback from a faculty member or graduate if access is available.
8. Document evidence, assumptions, AI assistance, limitations, and revisions in the repository.

## 4. Preliminary Curriculum Observations

The preliminary inventory identifies computing subjects and areas including programming, data structures, object-oriented programming, algorithms, theory of computation, database management, software engineering, computer networks, cloud computing, artificial intelligence, machine learning, computer vision, big-data systems, and project work. Each course must be checked against the applicable official curriculum.

The following Semester VII subjects and course codes were recorded in the preliminary inventory:

- CS415 — Ethical Hacking
- DS306 — Deep Learning
- DS311 — Natural Language Processing
- DS401 — Human Computer Interaction
- MG401 — Introduction to Entrepreneurship

These entries are based on the collected portal information and still require confirmation against the official curriculum version applicable to the 2023 admission batch. Their official credit values must also be verified.

### Credit inventory status

The current `curriculum.csv` contains the following provisional portal-displayed unit totals:

| Semester | Displayed units |
|---|---:|
| I | 20 |
| II | 24 |
| III | 23 |
| IV | 24 |
| V | 24 |
| VI | 21 |
| VII | 16 |
| **Semesters I–VII total** | **152** |

These figures are arithmetic totals of the entries currently recorded in `curriculum.csv`. They are not independently verified official programme credits. Course codes, titles, displayed units, and their equivalence to official credits must be checked against the applicable curriculum for the 2023 admission batch.

A subset consisting of Semesters I, II, III, VI, and VII totals 104 displayed units. This is a partial-semester subtotal, not the complete Semesters I–VII total.

Semester VIII is excluded because the official internship credit allocation and requirements have not been established. The official programme-credit denominator therefore remains unverified, and the percentage of programme credits affected by the proposed changes cannot yet be calculated.

## 5. Employer Job-Description Comparison

The selected employer roles and source URLs are documented in `job-descriptions.md` and `sources.md`.

The comparison covers three career directions:

- **HCLTech:** Analyst (Support & Operations), with a Generative AI-related job summary.
- **Accenture:** AI/ML Computational Science Associate.
- **Google:** Software Engineer II, AI/ML.

These roles can help identify practical skills worth considering, such as programming, debugging, data handling, testing, machine learning, deployment, and communication. However, job advertisements differ in seniority and requirements. They do not establish that every listed skill should become a compulsory university course.

Before final submission, verify each listing's exact title, role level, required skills, availability, and access date. Include only requirements supported by the actual advertisement. The Google Software Engineer II role should be treated as an experienced-role benchmark rather than automatically described as an entry-level opportunity.

## 6. Proposed KEEP, UPDATE, REDUCE, and ADD Recommendations

The following recommendations are provisional proposals based on the preliminary inventory and selected employer-role comparisons. They must be checked against the official syllabus, course learning outcomes, employer evidence, and institutional regulations before being finalised.

| No. | Action | Curriculum area | Proposed decision and reason |
|---:|---|---|---|
| 1 | KEEP | Programming fundamentals | Preserve the programming foundation needed for later software development and practical assignments. |
| 2 | KEEP | Data structures, algorithms, and object-oriented programming | Retain core problem-solving, algorithm analysis, abstraction, and maintainable program design. |
| 3 | KEEP | Database management and computer networks | Preserve SQL, data integrity, client-server communication, and network fundamentals for application and cloud work. |
| 4 | UPDATE | Software engineering | Strengthen practical work in version control, code review, automated testing, issue tracking, and technical documentation. |
| 5 | UPDATE | AI and machine-learning subjects | Include reproducible experiments, suitable baselines, correct data splitting, evaluation metrics, and error analysis. |
| 6 | UPDATE | Cloud computing | Add practical deployment, configuration, monitoring, access-control, and cost-awareness exercises. |
| 7 | UPDATE | Ethical hacking and cybersecurity | Emphasise authorised lab testing, secure coding, threat modelling, and defensive reporting. |
| 8 | UPDATE | Human Computer Interaction | Include accessibility checks and a usability evaluation with defined tasks, measures, and honest reporting of results. |
| 9 | ADD | Data engineering and data quality | Introduce data validation, transformation, pipeline reliability, and data-quality checks, subject to available curriculum space and approval. |
| 10 | ADD | Responsible AI and model evaluation | Include privacy, bias evaluation, reproducibility, limitations, and documentation of AI-assisted work. |
| 11 | ADD | Interdisciplinary CampusFlow lab or capstone | Integrate requirements analysis, implementation, testing, documentation, security, and evaluation in a practical project. |
| 12 | REDUCE | Confirmed overlap in introductory content | Reduce only material demonstrated by syllabus and learning-outcome comparisons to duplicate existing content. Preserve compulsory outcomes and prerequisites. |

These recommendations are proposals, not approved institutional changes. Before finalising them, identify the exact existing courses affected, support each decision with syllabus or job-description evidence, and check prerequisites, compulsory requirements, semester workload, and applicable regulations.

The REDUCE recommendation is conditional. No course or credit allocation should be reduced solely on the assumption that content overlaps.

## 7. Proposed Credit-Change Plan

The assignment asks for proposed changes affecting approximately 20–25% of programme credits. This target has **not yet been calculated or verified**.

The available evidence does not establish the official programme-credit denominator. The applicable curriculum version for the 2023 admission batch, the official credit equivalence of portal-displayed units, and Semester VIII internship credits must be confirmed first.

The final calculation must:

1. Confirm the official total programme credits for the 2023 admission batch.
2. Identify the exact existing courses affected by each recommendation.
3. Record the official credits for each affected course.
4. Count each existing course only once, even if several recommendations apply to it.
5. Distinguish updated or reduced existing courses from newly proposed courses.
6. Calculate the percentage of original programme credits affected.
7. Verify that compulsory courses, prerequisites, required learning outcomes, internship requirements, and graduation rules are preserved.

**Formula**

Percentage of original programme credits affected = (Distinct official credits affected ÷ Verified total programme credits) × 100

| Metric | Current status |
|---|---|
| Semesters I–VII total | 152 provisional displayed units from current CSV |
| Itemized Semesters I, II, III, VI, and VII subtotal | 104 displayed units; partial-semester subset |
| Verified official programme-credit total | Pending verification |
| Official Semester VIII internship credits | Unknown |
| Distinct official credits affected by the final proposal | Pending final change list |
| Percentage affected | Not yet calculable |
| 20–25% target achieved | Not yet established |

The final proposal should include a credit-change table listing each affected course, official credits, proposed action, reason, prerequisite implications, and supporting evidence. Do not claim that the 20–25% target has been achieved until the official denominator and final list of distinct affected courses have been verified.

## 8. AI-Assisted Subject Exercises

The file `ai-use-log.md` documents five subject exercises:

1. **Natural Language Processing:** Compare stemming and lemmatization using example words and an NLTK demonstration. Verify the behaviour of the chosen algorithms and note cases where part-of-speech settings affect results.
2. **Human Computer Interaction:** Design a usability evaluation for a student portal using representative tasks, completion rates, errors, time, accessibility checks, and participant feedback. Proposed success criteria are targets, not measured results.
3. **Introduction to Entrepreneurship:** Evaluate the SkillSwap Campus peer skill-exchange concept. Treat demand, feasibility, and uniqueness as hypotheses until validated with evidence.
4. **Ethical Hacking:** Develop a defensive security checklist for CampusFlow. The prototype's Student/Staff selector is not secure authentication, and uncompleted security tests must remain labelled as untested.
5. **Deep Learning:** Design an experiment to demonstrate overfitting and underfitting using training and validation performance. Do not report experimental findings unless the experiment has actually been run.

For every exercise, record the actual prompt, AI tool/model, date, relevant output summary, verification method, corrections, and limitations. AI-generated material is a draft and must not be presented as independently verified evidence without checking it.

## 9. Proposed Lab or Capstone

**Proposed title:** CampusFlow — Student Request Workflow and Analytics

CampusFlow is a prototype built with Streamlit and MySQL for submitting, storing, and tracking synthetic student-service requests. It provides a practical starting point for work on workflow design, data persistence, validation, and status tracking.

A proposed academic extension could include:

- A documented workflow with owners, approval boundaries, and exception handling.
- Authentication and server-side role-based authorisation.
- Audit logging and appropriate protection of sensitive information.
- Tests for normal requests, missing information, duplicates, unauthorised actions, and database failure.
- Aggregated reporting on request categories and resolution times using synthetic or appropriately anonymised data.
- A documented evaluation that distinguishes implemented functionality from proposed improvements.

The current Student/Staff selector is a demonstration control, not secure authentication or authorisation. Database outage recovery and prevention of unauthorised access have not been verified. CampusFlow is not a production student-management system.

The project could be proposed as a lab or capstone because it connects requirements analysis, database design, software engineering, security, HCI, testing, and analytics. Its suitability and credit allocation would require institutional approval.

## 10. Feedback and Validation Plan

The next step is to seek voluntary feedback from a faculty member or graduate, if access is available. Suggested questions include:

- Which proposed skills are most relevant to recent graduates?
- Which recommendations duplicate existing course outcomes?
- Which additions are feasible within the current semester structure?
- What prerequisites or accreditation requirements could constrain the changes?
- Would the proposed CampusFlow capstone be appropriate for student assessment?

Record the date, participant role without unnecessary personal details, consent, questions, and a fair summary of feedback. If access is unavailable or no one volunteers, document that limitation instead of inventing responses.

The proposal should also be checked against the official curriculum and applicable regulations before finalisation.

## 11. Limitations

- The official curriculum version applicable to the 2023 admission batch has not yet been confirmed.
- Portal-displayed units have not been independently established as official academic credits.
- The 152-unit total is an arithmetic sum of the current Semesters I–VII CSV entries, not a verified official programme-credit total.
- Semester VIII internship credits and requirements remain unknown.
- The selected job advertisements may change or become unavailable; their actual requirements and access dates must be verified.
- The proposed changes have not been approved by the institution.
- The REDUCE recommendation depends on evidence of duplicated learning outcomes.
- AI-assisted exercises require independent verification; proposed experiments and success criteria are not completed results.
- Faculty or graduate feedback must not be claimed unless it has actually been obtained.
- CampusFlow is a prototype and is not production-ready.
- The 20–25% credit-impact target remains uncalculated until the official credit total and distinct affected courses are established.

## 12. Conclusion

The preliminary audit suggests that the curriculum redesign could preserve strong computing foundations while strengthening practical software development, AI/ML evaluation, data quality, cybersecurity, usability, and integrated project work.

The recommendations are proposals, not approved curriculum changes. The next priorities are to verify the official programme structure and credit values, validate job-description evidence, finalise a non-duplicative list of course changes, calculate the credit impact, and document any available feedback.

The final proposal should demonstrate compliance with the assignment's 20–25% target only after those checks have been completed.
