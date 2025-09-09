#marker and grid

import matplotlib.pyplot as plt
x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]
plt.plot(x, y)

# Change line style and color
#plt.plot(x, y, 'r--', linewidth=2)
# Using hex colors
#plt.plot(x, y, color='#007EBD',linestyle='-.')

# Add markers and grid
plt.plot(x, y, marker='o', 
         markersize=8)
plt.grid(True, linestyle=':')

# Customize axis
plt.xlim(0, 5)
plt.ylim(0, 20)

plt.title("Simple Squared Function")
plt.xlabel("X values")
plt.ylabel("X squared")


plt.show()
