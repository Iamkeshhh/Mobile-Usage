import streamlit as st
import pandas as pd

st.title("📊 Data Explorer")

uploaded_file = st.sidebar.file_uploader(
    "Upload CSV",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    usage = st.sidebar.multiselect(
        "Mobile Usage",
        options=df["Daily_Mobile_Usage"].unique(),
        default=df["Daily_Mobile_Usage"].unique()
    )

    filtered_df = df[
        df["Daily_Mobile_Usage"].isin(usage)
    ]

    st.dataframe(filtered_df)

    st.write(filtered_df.describe())