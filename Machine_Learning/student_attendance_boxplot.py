import matplotlib.pyplot as plt
import pandas as pd

def main():
    df = pd.read_csv("student_performance_ml.csv")

    plt.boxplot(
        df["Attendance"],
        patch_artist=True
    )

    plt.title("Boxplot of Attendance")
    plt.ylabel("Attendance (%)")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()