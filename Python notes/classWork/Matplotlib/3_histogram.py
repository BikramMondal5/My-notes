import numpy as np
import matplotlib.pyplot as plt
# Generate random data
data = np.random.randn(1000)
print(data)
print(len(data))
# Create histogram
plt.hist(data, bins=50, 
         alpha=0.7, color='#007EBD',edgecolor="black")
plt.title("Normal Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()