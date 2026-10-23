
import uuid
from datetime import datetime

import mysql.connector
import pandas as pd
import streamlit as st
from mysql.connector import Error

st.set_page_config(
    page_title="CampusFlow",
    page_icon="🏫",
    layout="wide",
)

COLUMNS = [
    "Request ID", "Student", "Category",
    "Description", "Status", "Created"
]

CATEGORIES = [
    "Placement Query",
    "Document Query",
    "Academic Query",
    "Other",
]

STATUSES = ["Open", "In Progress", "Closed"]


def get_connection():
    return mysql.connector.connect(
        host=st.secrets["mysql"]["host"],
        port=int(st.secrets["mysql"]["port"]),
        user=st.secrets["mysql"]["user"],
        password=st.secrets["mysql"]["password"],
        database=st.secrets["mysql"]["database"],
        connection_timeout=5,
    )


def fetch_requests():
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT request_id, student_id, category,
                   description, status, created_at
            FROM requests
            ORDER BY created_at DESC
        """)
        rows = cursor.fetchall()

        return pd.DataFrame([
            {
                "Request ID": row["request_id"],
                "Student": row["student_id"],
                "Category": row["category"],
                "Description": row["description"],
                "Status": row["status"],
                "Created": str(row["created_at"]),
            }
            for row in rows
        ], columns=COLUMNS)
    finally:
        conn.close()


def create_request(student, category, description):
    conn = get_connection()
    try:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT request_id
            FROM requests
            WHERE LOWER(student_id) = LOWER(%s)
              AND LOWER(description) = LOWER(%s)
              AND status <> 'Closed'
            LIMIT 1
        """, (student.strip(), description.strip()))

        duplicate = cursor.fetchone()
        if duplicate:
            return False, duplicate[0]

        request_id = f"CF-{uuid.uuid4().hex[:8].upper()}"

        cursor.execute("""
            INSERT INTO requests
                (request_id, student_id, category,
                 description, status)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            request_id,
            student.strip(),
            category,
            description.strip(),
            "Open",
        ))

        conn.commit()
        return True, request_id
    except Error:
        conn.rollback()
        raise
    finally:
        conn.close()


def change_status(request_id, status):
    if status not in STATUSES:
        raise ValueError("Invalid status selected.")

    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE requests
            SET status = %s
            WHERE request_id = %s
        """, (status, request_id))

        if cursor.rowcount == 0:
            raise ValueError("Request not found.")

        conn.commit()
    except (Error, ValueError):
        conn.rollback()
        raise
    finally:
        conn.close()


st.title("🏫 CampusFlow")
st.subheader("College Request Management System")
st.caption(
    "Assignment prototype using synthetic data. "
    "Not connected to college systems."
)

st.sidebar.header("Demo access")
role = st.sidebar.selectbox("Choose a demo role", ["Student", "Staff"])
st.sidebar.info(
    "Demonstration only: this role selector is not authentication."
)

st.markdown("## Submit a request")

if role == "Student":
    with st.form("request_form", clear_on_submit=True):
        student = st.text_input("Demo student identifier")
        category = st.selectbox("Category", CATEGORIES)
        description = st.text_area("Describe your request")
        submitted = st.form_submit_button("Submit Request")

    if submitted:
        if not student.strip() or not description.strip():
            st.error("Please fill in both required fields.")
        else:
            try:
                success, result = create_request(
                    student, category, description
                )
                if success:
                    st.success(f"Request created: {result}")
                    st.rerun()
                else:
                    st.warning(
                        f"A matching open request already exists: {result}"
                    )
            except Error:
                st.error(
                    "The request could not be saved to MySQL. "
                    "Check the database connection and try again."
                )
else:
    st.info(
        "Staff demo mode: update request statuses below. "
        "Real deployments require verified staff authentication "
        "and server-side authorization."
    )

st.markdown("## Request dashboard")

status_filter = st.selectbox(
    "Filter requests",
    ["All"] + STATUSES,
)

try:
    df = fetch_requests()

    visible_df = df
    if status_filter != "All":
        visible_df = df[df["Status"] == status_filter]

    st.dataframe(
        visible_df,
        use_container_width=True,
        hide_index=True,
    )

    st.caption(f"Showing {len(visible_df)} request(s).")

    if role == "Staff":
        st.markdown("## Update request status")

        if df.empty:
            st.info("No requests are available to update.")
        else:
            selected_id = st.selectbox(
                "Select request",
                df["Request ID"].tolist(),
            )

            current_status = df.loc[
                df["Request ID"] == selected_id, "Status"
            ].iloc[0]

            new_status = st.selectbox(
                "Set status",
                STATUSES,
                index=STATUSES.index(current_status)
                if current_status in STATUSES else 0,
            )

            if st.button("Save status"):
                try:
                    change_status(selected_id, new_status)
                    st.success(
                        f"{selected_id} updated to {new_status}."
                    )
                    st.rerun()
                except (Error, ValueError):
                    st.error(
                        "Status update failed. "
                        "Check the request and database, then retry."
                    )
    else:
        st.warning("Only the Staff demo role can update statuses.")

except Error:
    st.error(
        "Could not connect to MySQL or load requests. "
        "Check your database service and secrets.toml configuration."
    )
