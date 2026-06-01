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

st.sidebar.header("🎛 Dashboard Filters")

usage_filter = st.sidebar.multiselect(
    "Select Mobile Usage Group",
    options=df["Daily_Mobile_Usage"].unique(),
    default=df["Daily_Mobile_Usage"].unique()
)

gpa_range = st.sidebar.slider(
    "GPA Range",
    float(df["GPA"].min()),
    float(df["GPA"].max()),
    (
        float(df["GPA"].min()),
        float(df["GPA"].max())
    )
)

sleep_range = st.sidebar.slider(
    "Sleep Hours",
    float(df["Sleep_Hours"].min()),
    float(df["Sleep_Hours"].max()),
    (
        float(df["Sleep_Hours"].min()),
        float(df["Sleep_Hours"].max())
    )
)

conc_range = st.sidebar.slider(
    "Concentration Score",
    int(df["Concentration_Score"].min()),
    int(df["Concentration_Score"].max()),
    (
        int(df["Concentration_Score"].min()),
        int(df["Concentration_Score"].max())
    )
)

filtered_df = df[
    (df["Daily_Mobile_Usage"].isin(usage_filter)) &
    (df["GPA"].between(gpa_range[0], gpa_range[1])) &
    (df["Sleep_Hours"].between(sleep_range[0], sleep_range[1])) &
    (df["Concentration_Score"].between(conc_range[0], conc_range[1]))
]
