import pandas as pd

DataPath = "student_performance_ml.csv"

df = pd.read_csv(DataPath)

print("Dataset Loaded Successfully")
print("\nFirst 5 records from dataset are : ")
print(df.head())

print("\nLast 5 records from dataset are : ")
print(df.tail())

print("Shape of Dataset : ",df.shape)

print("Column names : ",list(df.columns))

print("Column Datatype : ",list(df.dtypes))