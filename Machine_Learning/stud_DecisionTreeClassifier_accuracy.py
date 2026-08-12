# Calculate accuracy score 

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.metrics import accuracy_score

def main():
    stud_data = pd.read_csv("student_performance_ml.csv")

    X = stud_data.drop("FinalResult", axis=1)
    Y = stud_data["FinalResult"]

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)

    model = DecisionTreeClassifier()

    model = model.fit(X_train,Y_train)

    print("Decision Tree model trained successfully")

    Y_pred = model.predict(X_test)

    result = pd.DataFrame({
        "Actual": Y_test.values,
        "Predicted": Y_pred
    })

    print("\nActual vs Predicted Results:")
    print(result)
    
    Result = accuracy_score(Y_test,Y_pred)

    print("Accuracy is : ",round(Result*100,2),"%")

if __name__ == "__main__":
    main()
