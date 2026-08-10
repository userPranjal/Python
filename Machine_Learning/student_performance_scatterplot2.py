import matplotlib.pyplot as plt
import pandas as pd

def main():
    df = pd.read_csv("student_performance_ml.csv")

    PassStudents = df[df["FinalResult"] == 1]
    FailStudents = df[df["FinalResult"] == 0]

    plt.scatter(
        PassStudents["AssignmentsCompleted"],
        PassStudents["FinalResult"],
        color="green",
        edgecolors="black",
        label="Pass"
    )

    plt.scatter(
        FailStudents["AssignmentsCompleted"],
        FailStudents["FinalResult"],
        color="red",
        edgecolors="black",
        label="Fail"
    )

    plt.title("Assignments Completed vs Final Result")
    plt.xlabel("Assignments Completed")
    plt.ylabel("Final Result")
    #plt.yticks([0, 1], ["Fail", "Pass"])
    plt.grid(True)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()