# Train the model using fit()

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

def main():
    stud_data = pd.read_csv("student_performance_ml.csv")

    X = stud_data.drop("FinalResult", axis=1)
    Y = stud_data["FinalResult"]

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)

    model = DecisionTreeClassifier()

    model = model.fit(X_train,Y_train)

    print("Decision Tree model trained successfully")

if __name__ == "__main__":
    main()
