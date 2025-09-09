#line style and color

import matplotlib.pyplot as plt
x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]
plt.plot(x, y)

# Change line style and color
plt.plot(x, y, 'r--', linewidth=2, color='#007EBD',linestyle='-.')
# Using hex colors
#plt.plot(x, y, color='#007EBD',linestyle='-.')

plt.title("Simple Squared Function")
plt.xlabel("X values")
plt.ylabel("X squared")


plt.show()
