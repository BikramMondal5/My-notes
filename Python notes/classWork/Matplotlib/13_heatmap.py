# Create data for heatmap
import matplotlib.pyplot as plt
import numpy as np
data = np.random.rand(10, 12)
# Create heatmap
plt.figure(figsize=(10, 8))
heatmap = plt.imshow(data, cmap='viridis')
plt.colorbar(heatmap)
# Add labels
plt.title("Sample Heatmap")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
# Optional: Add text annotations
for i in range(10):
    for j in range(12):
        plt.text(j, i, f'{data[i, j]:.2f}', 
            ha='center', va='center')
plt.show()
