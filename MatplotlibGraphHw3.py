print("-----Question 1------")
print("create chart of programing language popularity: ")
#imports matplotlib
import matplotlib.pyplot as plt

#creates the languages, popularity, colors and sets one end of the chart to stick out from the others
languages = 'Java', 'Python', 'PHP', 'Javascript', 'C#', 'C++'
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]
explode = (0.1, 0, 0, 0, 0, 0)
# Plots the actual chart
plt.pie(popularity, explode=explode, labels=languages, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()
