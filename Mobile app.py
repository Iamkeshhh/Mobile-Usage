import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Student Mobile Usage Dashboard",
    page_icon="📱",
    layout="wide"
)

st.title("📱 Mobile Phone Usage Impact Dashboard")

st.markdown("""
### MANOVA Analysis on Students

Independent Variable:
- Daily Mobile Usage

Dependent Variables:
- GPA
- Sleep Hours
- Concentration Score
""")

uploaded_file = st.file_uploader(
    "Upload Dataset",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.success("Dataset Loaded Successfully")

    col1,col2,col3,col4 = st.columns(4)

    col1.metric(
        "Students",
        len(df)
    )

    col2.metric(
        "Average GPA",
        round(df["GPA"].mean(),2)
    )

    col3.metric(
        "Average Sleep",
        round(df["Sleep_Hours"].mean(),2)
    )

    col4.metric(
        "Average Concentration",
        round(df["Concentration_Score"].mean(),2)
    )

    st.dataframe(df)

else:
    st.info("Upload CSV File")