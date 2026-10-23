# AI Use Log — Task 2: Curriculum Audit

## 1. Purpose

This log documents the use of AI tools to support learning, curriculum analysis, and the development of practical exercises for the B.Tech Computer Science and Engineering programme.

AI-generated content is treated as a draft. Important facts, code, calculations, and recommendations must be independently verified before they are used in the final curriculum audit.

**Institution:** ICFAI Foundation for Higher Education, Hyderabad  
**Programme:** B.Tech Computer Science and Engineering  
**Admission batch:** 2023–2027

## 2. AI Tool and Recording Method

For each exercise, record:
- The AI tool and exact model displayed in the interface.
- The date the prompt was actually submitted.
- The exact prompt used.
- A short summary of the actual output received.
- The method used to verify the output.
- Any errors, limitations, or corrections identified.

Do not describe an exercise as completed or verified until the relevant steps have actually been performed.
## 3. Exercise 1 — Natural Language Processing (NLP)

**Topic:** Stemming versus lemmatization.

**Prompt:** Explain the difference between stemming and lemmatization in Natural Language Processing. Give five example words, show the expected output of both methods where applicable, and provide a short Python example using NLTK. Identify cases where the output depends on the chosen algorithm or dictionary.

**AI tool/model:** ChatGPT — GPT-6

**Date performed:** 23 October 2026

**Output summary:** The AI explained that stemming removes word endings using algorithmic rules, while lemmatization uses lexical information and part-of-speech information to find a base form. It compared the words playing, studies, cars, better, and running and provided an example using NLTK's PorterStemmer and WordNetLemmatizer. It also explained that different stemming algorithms and part-of-speech choices can produce different results.

**Verification method:** The explanation was compared with the official NLTK documentation. The documentation confirms that WordNetLemmatizer defaults to noun mode and accepts part-of-speech values for nouns, verbs, adjectives, and adverbs. The Python example still needs to be run to verify all displayed outputs.

**Result and corrections:** The response correctly highlighted the importance of the lemmatizer's part-of-speech setting. However, the supplied code appeared with missing line breaks between statements, so it must be formatted correctly before execution. Code execution and full output verification remain pending.

**Reference links:**
- WordNetLemmatizer: https://www.nltk.org/api/nltk.stem.wordnet.html
- PorterStemmer: https://www.nltk.org/api/nltk.stem.PorterStemmer.html


## 4. Exercise 2 — HCL/HCI (Official Subject Title to Be Confirmed)

**Topic:** Usability evaluation of a college student portal.

**Prompt:** Design a simple usability evaluation for a college student portal. Identify five representative user tasks, propose measurable usability criteria, and create a short test plan covering task completion, errors, time taken, accessibility, and user feedback. Do not invent test results.

**AI tool/model:** ChatGPT — GPT-6

**Date performed:** Record the actual date the prompt was submitted.

**Output summary:** The AI proposed five representative tasks: logging in, finding the timetable, checking examination results, finding fee details, and updating the student profile. It suggested measuring task completion, time taken, user errors, accessibility barriers, and satisfaction. Proposed targets included at least 80% task completion, a median completion time of two minutes, no more than one error per task, and an average satisfaction rating of at least 4 out of 5.

**Verification method:** Review the tasks and measurements against HCI principles. Check that the targets are measurable and that accessibility testing includes keyboard navigation, visible focus, sufficient contrast, and screen-reader usability where applicable.

**Result and corrections:** These are proposed evaluation criteria, not measured results. No actual participant testing or usability results are claimed. The plan should be tested with volunteers before drawing conclusions about the portal's usability.

**Limitations:** The proposed targets have not been validated through testing. The sample size and task difficulty may affect the results. Confirm the official course title before final submission.
## 5. Exercise 3 — Introduction to Entrepreneurship

**Topic:** Evaluating the SkillSwap Campus business idea.

**Prompt:** Evaluate SkillSwap Campus, a proposed student-to-student skill exchange platform where students teach skills to one another using credits instead of direct payments. Identify the target users, value proposition, key assumptions, possible revenue or sustainability models, competitors or substitutes, and three low-cost experiments to test demand. Clearly distinguish assumptions from verified facts.

**AI tool/model:** ChatGPT — GPT-6

**Date performed:** Record the actual date the prompt was submitted.

**Output summary:** The AI-assisted evaluation framework considers students who want to learn or teach practical skills as the target users. The proposed value proposition is to exchange skills using platform credits rather than requiring direct payment for every session. Key assumptions include student willingness to participate, trust between users, sufficient demand for different skills, and the feasibility of a credit-based exchange system.

Three proposed low-cost experiments are:
1. Conduct a voluntary student survey to measure interest in learning and teaching skills.
2. Create a simple sign-up form to measure how many students offer skills and how many request them.
3. Run a small, manually coordinated pilot and record completed exchanges, cancellations, and participant feedback.

Possible sustainability models include institutional sponsorship, optional premium features, or partnerships. These are ideas to investigate, not validated revenue sources. Existing skill-sharing services and informal student groups should be researched as competitors or substitutes.

**Verification method:** Research existing skill-sharing platforms and compare their actual features with the proposed idea. Check any competitor or market claims against reliable sources. Evaluate whether each experiment has a measurable outcome and can be conducted with minimal cost.

**Result and corrections:** The concept is a proposal, not a proven unique business. No claim of market demand, uniqueness, revenue, or successful testing is made without supporting evidence.

**Limitations:** Student interest, operational costs, fairness of the credit system, and long-term participation remain unverified. Any survey or pilot must be voluntary.

## 6. Exercise 4 — Ethical Hacking

**Topic:** Defensive security review of the CampusFlow demo application.

**Prompt:** Create a defensive security review checklist for a student-request web application that stores request IDs, student IDs, categories, descriptions, and status values in MySQL. Cover authentication, role-based authorization, SQL injection, input validation, duplicate requests, sensitive data exposure, logging, and database recovery. For each risk, give a safe test and a mitigation. Assume testing is limited to my own local demo application.

**AI tool/model:** ChatGPT — GPT-6

**Date performed:** Record the actual date the prompt was submitted.

**Output summary:** The AI proposed a defensive checklist covering authentication, authorization, SQL injection, input validation, duplicate handling, data exposure, logging, and database recovery. Suggested mitigations include using parameterized SQL queries, validating required fields, limiting access to sensitive information, implementing server-side authorization, and maintaining appropriate backups and recovery procedures.

**Verification method:** Compare the checklist with the OWASP Top 10 guidance at https://owasp.org/www-project-top-ten/. Review the CampusFlow source code to check which protections are implemented. Record actual test results separately from proposed tests.

**Result and corrections:** The application has been tested for required-field validation, duplicate-request handling, MySQL persistence, and status updates. The Student/Staff selector only changes the displayed interface; it is not secure authentication or server-side authorization. Actual unauthorized access testing and database failure/recovery testing have not been completed.

**Limitations:** These checks do not establish that the application is secure or production-ready. Additional testing is required for authentication, authorization, SQL injection resistance, sensitive-data exposure, logging, and database recovery.

## 7. Exercise 5 — Deep Learning

**Topic:** Understanding overfitting and underfitting.

**Prompt:** Explain overfitting and underfitting in a deep learning classification model. Propose a small experiment using a training set, validation set, and test set. Explain how to use learning curves, early stopping, and regularization, and identify common data leakage mistakes. Provide Python pseudocode and state which observations would support each conclusion.

**AI tool/model:** ChatGPT — GPT-6

**Date performed:** Record the actual date the prompt was submitted.

**Output summary:** The AI-assisted exercise explains that underfitting occurs when a model fails to learn patterns adequately, while overfitting occurs when it performs well on training data but generalizes poorly to unseen data. The proposed experiment separates data into training, validation, and test sets. Learning curves help compare training and validation performance; early stopping can stop training when validation performance stops improving; regularization can reduce overfitting.

**Verification method:** Compare the explanation with course materials or a recognized machine-learning reference. Check that the validation set is used for model selection and the test set is reserved for final evaluation. Review the experiment design for data leakage, including preprocessing fitted on the full dataset before splitting.

**Result and corrections:** This entry records a proposed experiment, not a completed model-training experiment. No accuracy scores, learning curves, or experimental outcomes are claimed. Actual execution and evaluation remain pending.

**Limitations:** The best model, stopping point, and regularization method depend on the dataset, architecture, and training configuration. These choices should be supported by experimental evidence rather than assumptions.

## 8. Overall Reflection

Complete this section after all five exercises have been performed.

- Which AI suggestions were useful?
- Which claims or outputs needed correction?
- Which verification methods were used?
- What limitations did the AI tool have?
- How can AI support learning without replacing independent reasoning and practical work?

## 9. Limitations and Responsible Use

This log is a record of AI-assisted work, not proof that every suggested approach is correct. Proposed prompts, summaries, and verification plans must be distinguished from completed experiments.

No participant feedback, code execution, security testing, competitor research, or experimental results should be claimed unless they have actually been carried out and documented.
