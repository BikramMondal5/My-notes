import pandas as pd
import matplotlib.pyplot as plt

class ScoreVisualizer:
    def __init__(self, students, test1_scores, test2_scores):
        self.df = pd.DataFrame({
            "Student": students,
            "Test1": test1_scores[:len(students)],
            "Test2": test2_scores[:len(students)]
        })
        # Replace None with NaN and ensure numeric
        self.df['Test1'] = pd.to_numeric(self.df['Test1'], errors="coerce")
        self.df['Test2'] = pd.to_numeric(self.df['Test2'], errors="coerce")

    def plot_test1_distribution(self):
        plt.figure(figsize=(8,5))
        self.df['Test1'].dropna().plot(kind="hist", bins=10, rwidth=0.8)
        plt.title("Test-1 Marks Distribution")
        plt.xlabel("Marks")
        plt.ylabel("Number of Students")
        plt.show()

    def plot_test2_distribution(self):
        plt.figure(figsize=(8,5))
        self.df['Test2'].dropna().plot(kind="hist", bins=10, rwidth=0.8, color="orange")
        plt.title("Test-2 Marks Distribution")
        plt.xlabel("Marks")
        plt.ylabel("Number of Students")
        plt.show()

    def plot_test1_attendance(self):
        absent1 = self.df['Test1'].isna().sum()
        present1 = self.df['Test1'].notna().sum()
        plt.pie([present1, absent1], labels=["Present", "Absent"], autopct="%1.1f%%", colors=["skyblue","lightcoral"])
        plt.title("Test-1 Attendance")
        plt.show()

    def plot_test2_attendance(self):
        absent2 = self.df['Test2'].isna().sum()
        present2 = self.df['Test2'].notna().sum()
        plt.pie([present2, absent2], labels=["Present", "Absent"], autopct="%1.1f%%", colors=["lightgreen","salmon"])
        plt.title("Test-2 Attendance")
        plt.show()

    def plot_average_comparison(self):
        plt.bar(["Test-1", "Test-2"], [self.df['Test1'].mean(), self.df['Test2'].mean()], color=["blue","orange"])
        plt.title("Average Marks Comparison")
        plt.ylabel("Average Marks")
        plt.show()

# Example usage:
students = [f"Student_{i}" for i in range(1, 64)]
test1_scores = [45, 50, 39, 42, 0, None, 48, 36, 52, 47] * 6 + [40, 44, 0]
test2_scores = [50, 55, 41, 38, 0, 42, 53, None, 49, 60] * 6 + [35, 48, 0]

visualizer = ScoreVisualizer(students, test1_scores, test2_scores)
visualizer.plot_test1_distribution()
visualizer.plot_test2_distribution()
visualizer.plot_test1_attendance()
visualizer.plot_test2_attendance()
visualizer.plot_average_comparison()