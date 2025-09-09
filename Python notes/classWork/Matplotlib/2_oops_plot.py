import matplotlib.pyplot as plt
# Create figure and axes objects
fig, ax = plt.subplots()
x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]
# Plot on the axes object
ax.plot(x, y, marker='o', 
        label="Data Points")
ax.set_title("Components of Matplotlib")
ax.set_xlabel("X-Axis")
ax.set_ylabel("Y-Axis")
ax.legend()

plt.show()
'''
import matplotlib.pyplot as plt
x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]
plt.plot(x, y)
plt.title("Simple Squared Function")
plt.xlabel("X values")
plt.ylabel("X squared")
plt.show()
'''