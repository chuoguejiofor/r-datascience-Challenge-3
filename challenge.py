import pandas as pd

df = pd.read_excel("default of credit card clients.xls", skiprows=1)

df.LIMIT_BAL.median()

df.groupby("SEX")["default payment next month"].mean()
df.groupby("SEX")["LIMIT_BAL"].median()

df["EDUCATION"] = df["EDUCATION"].apply(lambda x: 'High School' if x == 3 else 'Other')
df.groupby("EDUCATION")["default payment next month"].mean()
df.groupby("EDUCATION")["LIMIT_BAL"].median()

def ageGroup(age):
    age = int(age)
    if (age >= 30) & (age <= 39):
        return "30-39"
    elif (age >= 45) & (age <= 55):
        return "45-55"
    else:
        return "other"

df["AGE_GROUP"] = df.AGE.apply(lambda x: ageGroup(x))
df.groupby("AGE_GROUP")["default payment next month"].mean()
df.groupby("AGE_GROUP")["LIMIT_BAL"].median()