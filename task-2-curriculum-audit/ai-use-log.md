# AI Use Log

## Purpose

This log records how AI tools were used to support the curriculum audit and redesign. AI-generated suggestions are treated as drafts and are not considered official curriculum facts unless independently verified.

## Tool Information

- **AI tool:** ChatGPT
- **Model:** GPT-6
- **Use:** Brainstorming, explanations, drafting, and organizing curriculum-audit material.
- **Verification principle:** Official programme documents and student portal records take priority over AI-generated information.

## Exercise 1 — Natural Language Processing

**Topic:** Stemming and lemmatization.

**Prompt summary:** Explain the difference between stemming and lemmatization, provide five example words, demonstrate Python code using NLTK, and identify outputs that depend on the chosen algorithm.

**Output summary:** The AI explained the difference between rule-based word reduction and vocabulary- or context-aware lemmatization and provided illustrative examples and Python code.

**Verification method:** Run the code in the intended Python environment, inspect the output, and compare it with the selected NLTK stemmer and lemmatizer documentation.

**Verification status:** Code execution and exact outputs must be confirmed before reporting them as tested results.

## Exercise 2 — HCL / HCI

**Topic:** Usability evaluation of a college student portal.

**Prompt summary:** Design a usability evaluation with five representative user tasks and measurable criteria for task completion, errors, time taken, accessibility, and user feedback. Do not invent test results.

**Output summary:** The AI proposed a usability test plan, representative tasks, measurement criteria, and a process for recording observations.

**Verification method:** Review the proposed tasks against the actual portal and accessibility requirements. Conduct sessions with participants before reporting any findings.

**Verification status:** Proposed test plan only. No usability results are claimed here. The official course title must be verified from the student portal.

**Date performed:** Confirm the actual prompt date from the original conversation history before final submission.

## Exercise 3 — Introduction to Entrepreneurship

**Topic:** SkillSwap Campus.

**Prompt summary:** Develop a distinctive campus business idea and present its business model, target users, value proposition, and operating approach.

**Output summary:** The AI helped develop SkillSwap Campus, a concept for students to exchange skills and learn from one another. The idea requires validation with potential users and comparison with existing services before claiming that it is unique.

**Verification method:** Interview potential student users, identify likely alternatives, test demand, and estimate operating costs and possible revenue sources.

**Verification status:** Initial business concept. Market demand, feasibility, and uniqueness have not been established through formal research.

## Exercise 4 — Ethical Hacking

**Topic:** Defensive security review of the CampusFlow demo application.

**Prompt summary:** Create a defensive security checklist for a student-request application storing request IDs, student IDs, categories, descriptions, and status values in MySQL. Cover authentication, role-based authorization, SQL injection, input validation, duplicate requests, sensitive-data exposure, logging, and database recovery. Restrict testing to the user's own local demo application.

**Output summary:** The AI proposed security checks and mitigations, including parameterized SQL queries, input validation, server-side authorization, limiting sensitive-data exposure, and appropriate backup and recovery procedures.

**Verification method:** Compare the checklist with the OWASP Top 10 guidance at https://owasp.org/www-project-top-ten/ and inspect the application's source code. Record actual test outcomes separately from suggested tests.

**Observed results and corrections:** Required-field validation, duplicate-request handling, MySQL persistence, and status updates were tested as documented in the project test cases. The Student/Staff selector changes the displayed interface; it does not establish secure authentication or server-side authorization. Unauthorized-access testing and database failure/recovery testing remain incomplete.

**Limitations:** These checks do not prove that the application is secure or production-ready.

## Exercise 5 — Deep Learning

**Topic:** Overfitting and underfitting in machine learning.

**Prompt summary:** Explain overfitting and underfitting and discuss ways to identify and reduce them during model training.

**Output summary:** The AI explained how training and validation performance can help identify overfitting and underfitting and outlined possible responses, such as regularization, suitable model complexity, and collecting or improving training data.

**Verification method:** Compare the explanation with course materials and validate any practical claims using training and validation metrics from an actual experiment.

**Verification status:** Conceptual explanation. No experimental results are claimed unless supported by recorded model runs.

## Limitations and Responsible Use

- AI-generated suggestions may be incomplete or inaccurate.
- Official course titles, course codes, credits, and programme requirements must be checked against official records.
- Proposed usability and security tests must not be described as completed tests.
- Business ideas must not be described as unique or commercially validated without supporting research.
- Dates, results, and source details must reflect what actually happened.
- Personal, confidential, or sensitive information should not be included in public project files.

## Final Review Checklist

- [ ] Confirm the actual date for each exercise where a date is required.
- [ ] Verify official course titles and credit values against available records.
- [ ] Run code examples before claiming that their output was tested.
- [ ] Separate AI suggestions from observed facts and verified results.
- [ ] Add supporting sources where external information is used.
