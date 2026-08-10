import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv("student_performance_ml.csv")

    plt.hist(
        df["StudyHours"], 
        bins=5, 
        edgecolor="black",
        alpha=0.8,           
        rwidth=0.9
    )

    plt.title("Distribution of Study Hours")
    plt.xlabel("Study Hours")
    plt.ylabel("Number of Students")
    plt.show()

if __name__ == "__main__":
    main()