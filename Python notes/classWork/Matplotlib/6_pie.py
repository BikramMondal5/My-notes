#shows both values and percentage
import matplotlib.pyplot as plt

# Your data
labels = ['Python', 'Java', 'JavaScript', 
          'C++', 'Other']

values = [35, 60, 82, 12, 92]
colors = ["skyblue", "lightgreen", "orange", "pink","red"]
explode = [0, 0.1, 0, 0,0.2]  # Explode 2nd and 5th slice

# Custom formatting function
def fmt(pct, allvals):
    absolute = int(round(pct/100. * sum(allvals)))
    return f"{absolute} ({pct:.1f}%)"

# Plot pie chart
plt.pie(
    values,
    autopct=lambda pct: fmt(pct, values),  # show value + percentage
    startangle=90,
    labels=labels,
    colors=colors,
    explode=explode,
    shadow=True,
    wedgeprops={'edgecolor': 'black'}
)


plt.title("Pie Chart with Values & Percentages")
plt.show()

