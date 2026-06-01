import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📈 Interactive Visualizations")

uploaded_file = st.sidebar.file_uploader(
    "Upload CSV",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    metric = st.selectbox(
        "Select Variable",
        [
            "GPA",
            "Sleep_Hours",
            "Concentration_Score"
        ]
    )

    fig = px.box(
        df,
        x="Daily_Mobile_Usage",
        y=metric,
        color="Daily_Mobile_Usage",
        title=f"{metric} vs Mobile Usage"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    bar = px.bar(
        df.groupby("Daily_Mobile_Usage")[metric]
          .mean()
          .reset_index(),
        x="Daily_Mobile_Usage",
        y=metric,
        color="Daily_Mobile_Usage"
    )

    st.plotly_chart(
        bar,
        use_container_width=True
    )