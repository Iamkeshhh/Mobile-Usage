import streamlit as st
import pandas as pd

st.title("🎓 Student Performance Simulator")

with st.form("student_form"):

    st.subheader("Enter Student Details")

    mobile_usage = st.selectbox(
        "Daily Mobile Usage",
        ["<2 hrs","2-5 hrs",">5 hrs"]
    )

    gpa = st.number_input(
        "GPA",
        min_value=0.0,
        max_value=10.0,
        value=7.0
    )

    sleep = st.number_input(
        "Sleep Hours",
        min_value=0.0,
        max_value=12.0,
        value=7.0
    )

    concentration = st.slider(
        "Concentration Score",
        0,
        100,
        70
    )

    submit = st.form_submit_button("Analyze Student")

if submit:

    st.success("Analysis Complete")

    st.write("### Student Summary")

    st.write(f"Mobile Usage: {mobile_usage}")
    st.write(f"GPA: {gpa}")
    st.write(f"Sleep Hours: {sleep}")
    st.write(f"Concentration: {concentration}")

    if gpa >= 8 and sleep >= 7:
        st.success("Excellent Academic Performance")
    elif gpa >= 6:
        st.warning("Average Performance")
    else:
        st.error("Needs Improvement")