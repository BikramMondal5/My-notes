#shows only percentage
import matplotlib.pyplot as plt
labels = ['Python', 'Java', 'JavaScript', 
          'C++', 'Other']

values = [35, 60, 82, 12, 92]
colors = ["skyblue", "lightgreen", "orange", "pink","red"]
explode = [0, 0.1, 0, 0,0.2]  # Explode 2nd and 5th slice

plt.pie(
    values,
    labels=labels,
    colors=colors,
    explode=explode,
    autopct="%1.1f%%",
    shadow=True,
    startangle=90,
    wedgeprops={'edgecolor': 'black'}
)

plt.title("Example Pie Chart")
plt.show()
