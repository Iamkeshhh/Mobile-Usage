import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from statsmodels.multivariate.manova import MANOVA
from scipy.stats import shapiro
df = pd.read_csv("mobile_phone_usage_students_MANOVA.csv")

df.head()
print(df.info())

print("\nSummary Statistics")
print(df.describe())

print("\nGroup Counts")
print(df['Daily_Mobile_Usage'].value_counts())
plt.figure(figsize=(8,5))
sns.boxplot(x='Daily_Mobile_Usage', y='GPA', data=df)
plt.title("Mobile Usage vs GPA")
plt.show()
plt.figure(figsize=(8,5))
sns.boxplot(x='Daily_Mobile_Usage', y='Sleep_Hours', data=df)
plt.title("Mobile Usage vs Sleep Hours")
plt.show()
plt.figure(figsize=(8,5))
sns.boxplot(x='Daily_Mobile_Usage', y='Concentration_Score', data=df)
plt.title("Mobile Usage vs Concentration")
plt.show()
print(df.isnull().sum())
for col in ['GPA','Sleep_Hours','Concentration_Score']:
    stat,p = shapiro(df[col])
    
    print(f"\n{col}")
    print("Statistic =",stat)
    print("p-value =",p)
    
    if p > 0.05:
        print("Data is Normally Distributed")
    else:
        print("Data is NOT Normally Distributed")
        corr = df[['GPA','Sleep_Hours','Concentration_Score']].corr()

plt.figure(figsize=(6,4))
sns.heatmap(corr,
            annot=True,
            cmap='coolwarm')

plt.title("Correlation Matrix")
plt.show()
manova = MANOVA.from_formula(
    'GPA + Sleep_Hours + Concentration_Score ~ Daily_Mobile_Usage',
    data=df
)

print(manova.mv_test())
import statsmodels.api as sm
from statsmodels.formula.api import ols

variables = ['GPA',
             'Sleep_Hours',
             'Concentration_Score']

for var in variables:

    print("\n"+"="*50)
    print("ANOVA FOR:",var)

    model = ols(
        f'{var} ~ C(Daily_Mobile_Usage)',
        data=df
    ).fit()

    table = sm.stats.anova_lm(model, typ=2)

    print(table)
    group_means = df.groupby(
    'Daily_Mobile_Usage'
)[['GPA',
   'Sleep_Hours',
   'Concentration_Score']].mean()

print(group_means)
group_means.plot(
    kind='bar',
    figsize=(10,6)
)

plt.title(
    "Average GPA, Sleep Hours and Concentration by Mobile Usage"
)

plt.ylabel("Mean Value")
plt.xticks(rotation=0)

plt.show()
print("""
INTERPRETATION GUIDE

If Wilks' Lambda p-value < 0.05:
Reject H0

Conclusion:
Mobile phone usage has a significant impact on at least one
of GPA, Sleep Hours, or Concentration Score.

If p-value > 0.05:
Fail to Reject H0

Conclusion:
Mobile phone usage does not significantly affect the dependent variables.
""")