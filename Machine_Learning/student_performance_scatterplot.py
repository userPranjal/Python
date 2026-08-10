import matplotlib.pyplot as plt
import pandas as pd

def main():
    df = pd.read_csv("student_performance_ml.csv")

    PassStudents = df[df["FinalResult"] == 1]
    FailStudents = df[df["FinalResult"] == 0]

    plt.scatter(
        PassStudents['StudyHours'],
        PassStudents['PreviousScore'],
        marker = "o",
        alpha=0.8,
        edgecolors="black",
        linewidths=1,
        color="darkgreen",
        label = "Pass"
    )

    plt.scatter(
            FailStudents['StudyHours'],
            FailStudents['PreviousScore'],
            marker = "o",
            alpha=0.8,
            edgecolors="black",
            linewidths=1,
            color="darkred",
            label = "Fail"
    )

    plt.title("Scatter Plot")
    plt.xlabel("Study Hours")
    plt.ylabel("Previous Score")
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()