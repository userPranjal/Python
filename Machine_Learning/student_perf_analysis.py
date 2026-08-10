# Basic pandas functions calculation

import pandas as pd

DataPath = "student_performance_ml.csv"

df = pd.read_csv(DataPath)

print("Dataset Loaded Successfully")

ResultCount = df['FinalResult'].value_counts()

print("Distribution of Final Result : ")
print(ResultCount)

PassCount = df["FinalResult"].value_counts().get(1, 0)
FailCount = df["FinalResult"].value_counts().get(0, 0)

TotalStudents = len(df)

PassPercentage = (PassCount / TotalStudents) * 100
FailPercentage = (FailCount / TotalStudents) * 100

print("Total Students :", TotalStudents)
print("Passed Students:", PassCount)
print("Failed Students:", FailCount)

print("Pass Percentage:", round(PassPercentage, 2), "%")
print("Fail Percentage:", round(FailPercentage, 2), "%")