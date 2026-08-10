# Basic pandas functions calculation

import pandas as pd

DataPath = "student_performance_ml.csv"

df = pd.read_csv(DataPath)

print("Dataset Loaded Successfully")

print("Average Study Hours : ",round(df['StudyHours'].mean(),2))

print("Average Attendance : ",round(df['Attendance'].mean(),2))

print("Maximum Previous Score : ",df['PreviousScore'].max())

print("Minimum Sleep Hours : ",df['SleepHours'].min())