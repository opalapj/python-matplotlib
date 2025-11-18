import matplotlib.pyplot as plt


x = [1, 2, 3, 4]
y = [1, 4, 2, 3]

fig, ax = plt.subplots()  # Create a figure containing a single Axes.
ax.plot(x, y)  # Plot some data on the Axes.
plt.show()  # Show the figure.
