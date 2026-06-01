import streamlit as st
import pandas as pd

from statsmodels.multivariate.manova import MANOVA
from scipy.stats import shapiro

import statsmodels.api as sm
from statsmodels.formula.api import ols

st.title("📚 MANOVA Analysis")

uploaded_file = st.sidebar.file_uploader(
    "Upload CSV",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.subheader("Normality Test")

    for col in [
        "GPA",
        "Sleep_Hours",
        "Concentration_Score"
    ]:

        stat,p = shapiro(df[col])

        st.write(
            f"{col} : p-value = {round(p,4)}"
        )

    if st.button("Run MANOVA"):

        manova = MANOVA.from_formula(
            'GPA + Sleep_Hours + Concentration_Score ~ Daily_Mobile_Usage',
            data=df
        )

        st.text(
            str(manova.mv_test())
        )

    if st.button("Run ANOVA"):

        variables = [
            'GPA',
            'Sleep_Hours',
            'Concentration_Score'
        ]

        for var in variables:

            st.subheader(var)

            model = ols(
                f'{var} ~ C(Daily_Mobile_Usage)',
                data=df
            ).fit()

            table = sm.stats.anova_lm(
                model,
                typ=2
            )

            st.dataframe(table)