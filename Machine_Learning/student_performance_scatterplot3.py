import matplotlib.pyplot as plt
import pandas as pd

def main():
    df = pd.read_csv("student_performance_ml.csv")

    print(df.groupby("FinalResult")["SleepHours"].mean())

    PassStudents = df[df["FinalResult"] == 1]
    FailStudents = df[df["FinalResult"] == 0]

    plt.scatter(
        PassStudents["SleepHours"],
        PassStudents["FinalResult"],
        color="green",
        edgecolors="black",
        label="Pass"
    )

    plt.scatter(
        FailStudents["SleepHours"],
        FailStudents["FinalResult"],
        color="red",
        edgecolors="black",
        label="Fail"
    )

    plt.title("Sleep Hours vs Final Result")
    plt.xlabel("Sleep Hours")
    plt.ylabel("Final Result")
    #plt.yticks([0, 1], ["Fail", "Pass"])
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()