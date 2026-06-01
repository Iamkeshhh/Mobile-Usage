import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="Student Profile",
    layout="wide"
)

st.title("👤 Student Profile Explorer")

uploaded_file = st.sidebar.file_uploader(
    "Upload Dataset",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    # Student Selection Toggle
    selected_student = st.selectbox(
        "Select Student ID",
        sorted(df["Student_ID"].unique())
    )

    student = df[
        df["Student_ID"] == selected_student
    ].iloc[0]

    st.divider()

    # Student Summary Cards
    col1,col2,col3,col4 = st.columns(4)

    col1.metric(
        "Student ID",
        student["Student_ID"]
    )

    col2.metric(
        "GPA",
        student["GPA"]
    )

    col3.metric(
        "Sleep Hours",
        student["Sleep_Hours"]
    )

    col4.metric(
        "Concentration",
        student["Concentration_Score"]
    )

    st.divider()

    st.subheader("Student Details")

    details = pd.DataFrame({
        "Attribute":[
            "Mobile Usage",
            "GPA",
            "Sleep Hours",
            "Concentration Score"
        ],
        "Value":[
            student["Daily_Mobile_Usage"],
            student["GPA"],
            student["Sleep_Hours"],
            student["Concentration_Score"]
        ]
    })

    st.dataframe(
        details,
        use_container_width=True
    )

    st.divider()

    # Radar Chart

    st.subheader("Performance Radar")

    fig = go.Figure()

    fig.add_trace(
        go.Scatterpolar(
            r=[
                student["GPA"]*10,
                student["Sleep_Hours"]*10,
                student["Concentration_Score"]
            ],
            theta=[
                "GPA",
                "Sleep Hours",
                "Concentration"
            ],
            fill='toself',
            name=f"Student {selected_student}"
        )
    )

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0,100]
            )
        ),
        showlegend=False
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    # Personalized Insights

    st.subheader("🤖 Personalized Insight")

    gpa = student["GPA"]
    sleep = student["Sleep_Hours"]
    concentration = student["Concentration_Score"]

    if gpa >= 8:
        st.success(
            "Excellent academic performance."
        )
    elif gpa >= 6:
        st.warning(
            "Average academic performance."
        )
    else:
        st.error(
            "Academic performance needs improvement."
        )

    if sleep < 6:
        st.warning(
            "Sleep duration is below recommended levels."
        )

    if concentration < 70:
        st.warning(
            "Concentration score is relatively low."
        )

else:
    st.info("Please upload the dataset.")