import matplotlib.pyplot as plt
import pandas as pd

def main():
    df = pd.read_csv("student_performance_ml.csv")

    plt.scatter(
        df['StudyHours'],
        df['PreviousScore'],
        marker = "o",
        alpha=0.8,
        edgecolors="black",
        linewidths=1,
        label = "Students"
    )

    plt.title("Scatter Plot")
    plt.xlabel("Study Hours")
    plt.ylabel("Previous Score")
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()