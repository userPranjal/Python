import pandas as pd

DataPath = "student_performance_ml.csv"

df = pd.read_csv(DataPath)

print("Dataset Loaded Successfully")

print("Shape of Dataset : ",df.shape)

print("Total number of students : ",df.shape[0])

PassCount = (df["FinalResult"] == 1).sum()
FailCount = (df["FinalResult"] == 0).sum()

print("Passed Students :", PassCount)
print("Failed Students :", FailCount)