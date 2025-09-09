#histogram with different bins
import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)  # 1000 random values
print(data)
plt.figure(figsize=(12,4))

plt.subplot(1,3,1)
plt.hist(data, bins=5, color="skyblue", edgecolor="black")
plt.title("bins=5")

plt.subplot(1,3,2)
plt.hist(data, bins=20, color="orange", edgecolor="black")
plt.title("bins=20")

plt.subplot(1,3,3)
plt.hist(data, bins=[-3,-2,-1,0,1,2,3], color="green", edgecolor="black")
plt.title("Custom bin edges")

plt.tight_layout()
plt.show()
