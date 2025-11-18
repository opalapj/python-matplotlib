import matplotlib.pyplot as plt


x = [1, 2, 3, 4]
y = [0, 0.5, 1, 0.2]

# The explicit "Axes" interface.
fig = plt.figure()
ax = fig.subplots()
ax.plot(x, y)

# The implicit "pyplot" interface.
plt.plot(x, y[::-1])
plt.show()
