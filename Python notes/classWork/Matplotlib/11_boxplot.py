import matplotlib.pyplot as plt

# Example dataset
data = [7, 8, 5, 6, 9, 12, 15, 14, 6, 7, 8, 9, 10, 11, 20]

# Create boxplot
plt.boxplot(data)

# Add title and labels
plt.title("Boxplot Example")
plt.ylabel("Values")

# Show plot
plt.show()