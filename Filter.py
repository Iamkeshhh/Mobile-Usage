gpa_filter = st.sidebar.slider(
    "GPA Range",
    float(df.GPA.min()),
    float(df.GPA.max()),
    (
        float(df.GPA.min()),
        float(df.GPA.max())
    )
)
csv = df.to_csv(index=False)

st.download_button(
    "Download Dataset",
    csv,
    "filtered_data.csv",
    "text/csv"
)
import plotly.express as px

corr = df[
    [
        "GPA",
        "Sleep_Hours",
        "Concentration_Score"
    ]
].corr()

fig = px.imshow(
    corr,
    text_auto=True
)

st.plotly_chart(fig)
if "Wilks' lambda" in result:

    st.success("""
    Significant relationship exists between
    mobile phone usage and student outcomes.
    """)