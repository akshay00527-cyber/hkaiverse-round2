
from pathlib import Path

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="CSE Curriculum Audit",
    page_icon="📚",
    layout="wide",
)

st.title("CSE Curriculum Comparison Tool")
st.write(
    "Preliminary curriculum audit for B.Tech Computer Science "
    "and Engineering, admission batch 2023–2027."
)

st.warning(
    "Course information is transcribed from student portal screenshots. "
    "Displayed units have not yet been confirmed as official academic "
    "credits, and the applicable curriculum version still needs verification."
)

# Resolve the CSV relative to this script, not the terminal's working directory.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
CURRICULUM_PATH = (
    PROJECT_ROOT / "task-2-curriculum-audit" / "curriculum.csv"
)

if not CURRICULUM_PATH.exists():
    st.error(f"Curriculum file not found: {CURRICULUM_PATH}")
    st.stop()

try:
    courses = pd.read_csv(CURRICULUM_PATH, dtype=str).fillna("")
except Exception as exc:
    st.error(f"Could not read curriculum.csv: {exc}")
    st.stop()

required_columns = {
    "semester",
    "course_code",
    "course_name",
    "credits",
    "course_type",
    "verification_status",
    "notes",
}

missing_columns = required_columns - set(courses.columns)
if missing_columns:
    st.error(
        "The CSV is missing these columns: "
        + ", ".join(sorted(missing_columns))
        + ". Check the header row in curriculum.csv."
    )
    st.stop()

courses["credits"] = pd.to_numeric(
    courses["credits"].replace({"Unknown": "", "unknown": ""}),
    errors="coerce",
)

# Recommendations are proposals for review, not official decisions.
recommendations = {
    "CS101": ("KEEP", "Programming"),
    "CS102": ("KEEP", "Programming"),
    "CS201": ("KEEP", "Software Engineering"),
    "CS203": ("KEEP", "Algorithms"),
    "DS101": ("UPDATE", "AI/ML"),
    "CS305": ("UPDATE", "AI/ML"),
    "CS307": ("UPDATE", "Cloud"),
    "DS201": ("UPDATE", "AI/ML"),
    "DS307": ("UPDATE", "Data"),
    "DS311": ("UPDATE", "AI/ML"),
    "DS306": ("UPDATE", "AI/ML"),
    "DS401": ("UPDATE", "HCI"),
    "CS415": ("UPDATE", "Security"),
    "MG401": ("KEEP", "Business"),
}

courses["Recommendation"] = courses["course_code"].map(
    lambda code: recommendations.get(code, ("VERIFY", "Other"))[0]
)
courses["Area"] = courses["course_code"].map(
    lambda code: recommendations.get(code, ("VERIFY", "Other"))[1]
)

# Proposed addition: not an official course or approved change.
proposed_rows = pd.DataFrame([
    {
        "semester": "Proposed",
        "course_code": "",
        "course_name": "Data Engineering and Data Quality",
        "credits": float("nan"),
        "course_type": "Proposed course",
        "verification_status": "Proposal only",
        "notes": "Suggested topic; validate employer evidence, prerequisites, and credit balance.",
        "Recommendation": "ADD",
        "Area": "Data",
    },
    {
        "semester": "Review needed",
        "course_code": "",
        "course_name": "Potential overlap across introductory content",
        "credits": float("nan"),
        "course_type": "Review item",
        "verification_status": "Not yet established",
        "notes": "Review learning outcomes before recommending any reduction; no course removal is confirmed.",
        "Recommendation": "REDUCE",
        "Area": "Foundation",
    },
])

courses = pd.concat([courses, proposed_rows], ignore_index=True)
courses["semester"] = courses["semester"].astype(str)

# Filters
st.sidebar.header("Filter Courses")

semester_options = ["All"] + sorted(
    courses["semester"].unique().tolist()
)
selected_semester = st.sidebar.selectbox(
    "Semester", semester_options
)

area_options = ["All"] + sorted(courses["Area"].unique().tolist())
selected_area = st.sidebar.selectbox("Subject area", area_options)

recommendation_options = [
    "All", "KEEP", "UPDATE", "REDUCE", "ADD", "VERIFY"
]
selected_recommendation = st.sidebar.selectbox(
    "Recommendation", recommendation_options
)

filtered = courses.copy()

if selected_semester != "All":
    filtered = filtered[filtered["semester"] == selected_semester]

if selected_area != "All":
    filtered = filtered[filtered["Area"] == selected_area]

if selected_recommendation != "All":
    filtered = filtered[
        filtered["Recommendation"] == selected_recommendation
    ]

st.subheader("Course comparison")
display_columns = [
    "semester",
    "course_code",
    "course_name",
    "credits",
    "course_type",
    "verification_status",
    "Recommendation",
    "Area",
    "notes",
]
st.dataframe(
    filtered[display_columns],
    use_container_width=True,
    hide_index=True,
)
st.caption(f"Showing {len(filtered)} of {len(courses)} entries.")

st.subheader("Recommendation summary")
summary = (
    courses["Recommendation"]
    .value_counts()
    .reindex(
        ["KEEP", "UPDATE", "REDUCE", "ADD", "VERIFY"],
        fill_value=0,
    )
)

cols = st.columns(5)
for col, label in zip(
    cols, ["KEEP", "UPDATE", "REDUCE", "ADD", "VERIFY"]
):
    col.metric(label, int(summary[label]))

st.info(
    "Recommendations are preliminary review suggestions, not official "
    "curriculum decisions. REDUCE does not mean a course has been removed."
)

st.subheader("Data completeness")
numeric_credits = courses.loc[
    courses["course_type"] != "Proposed course", "credits"
]
known_units = numeric_credits.sum(min_count=1)
unknown_count = int(numeric_credits.isna().sum())

col1, col2 = st.columns(2)
col1.metric(
    "Known displayed units in listed courses",
    "Not available" if pd.isna(known_units) else f"{known_units:g}",
)
col2.metric("Entries with unknown units", unknown_count)

st.caption(
    "This sum covers listed portal courses only. It is not the official "
    "programme-credit total; internship and official credit equivalence "
    "remain unverified."
)

st.subheader("Credit-change calculator")
st.write(
    "Use only verified official credit figures. Do not enter estimated "
    "values as if they were official."
)

original_credits = st.number_input(
    "Original programme credits (verified)",
    min_value=0.0,
    value=0.0,
    step=1.0,
)
affected_credits = st.number_input(
    "Distinct credits affected by redesign",
    min_value=0.0,
    value=0.0,
    step=1.0,
)
proposed_total = st.number_input(
    "Proposed programme credits (verified)",
    min_value=0.0,
    value=0.0,
    step=1.0,
)

if original_credits > 0:
    percentage = affected_credits / original_credits * 100
    st.metric("Percentage affected", f"{percentage:.2f}%")

    if affected_credits > original_credits:
        st.error(
            "Affected credits cannot exceed original credits. "
            "Check for duplicate counting."
        )
    elif 20 <= percentage <= 25:
        st.success("The affected-credit percentage is within 20–25%.")
    else:
        st.info("The affected-credit percentage is outside 20–25%.")

    if proposed_total > 0:
        difference = proposed_total - original_credits
        st.metric("Change in programme credits", f"{difference:+.1f}")
        if difference != 0:
            st.warning(
                "Confirm regulations and graduation requirements before "
                "accepting a change in total programme credits."
            )
else:
    st.info(
        "Enter the verified original programme total to calculate "
        "the affected-credit percentage."
    )

st.subheader("Verification checklist")
st.caption(
    "Check these only after you have genuinely completed each verification."
)

st.checkbox(
    "I verified the applicable official curriculum version.",
    key="verify_curriculum",
)
st.checkbox(
    "I verified all course credits and prerequisites.",
    key="verify_credits",
)
st.checkbox(
    "I checked that affected credits are not double-counted.",
    key="verify_counting",
)

if all(
    st.session_state.get(key, False)
    for key in [
        "verify_curriculum",
        "verify_credits",
        "verify_counting",
    ]
):
    st.success("All verification checks are marked complete.")
