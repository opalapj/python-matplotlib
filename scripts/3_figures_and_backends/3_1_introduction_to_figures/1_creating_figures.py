from matplotlib import pyplot as plt


# https://matplotlib.org/stable/users/explain/figure/figure_intro.html#creating-figures

# A simple grid of Axes can be achieved with pyplot.subplots (which
# simply wraps Figure.subplots):
fig, axs = plt.subplots(
    nrows=2,
    ncols=2,
    figsize=(4, 3),
    layout="constrained",
)

# More complex grids can be achieved with pyplot.subplot_mosaic (which
# wraps Figure.subplot_mosaic):
fig, axs = plt.subplot_mosaic(
    mosaic=[
        ["A", "right"],
        ["B", "right"],
    ],
    figsize=(4, 3),
    layout="constrained",
)

# Sometimes we want to have a nested layout in a Figure, with two or more
# sets of Axes that do not share the same subplot grid. We can use
# add_subfigure or subfigures to create virtual figures inside a parent
# Figure; see Figure subfigures for more details.
fig = plt.figure(
    layout="constrained",
    facecolor="lightskyblue",
)
fig.suptitle("Figure")

fig_L, fig_R = fig.subfigures(
    nrows=1,
    ncols=2,
)
fig_L.set_facecolor("thistle")
fig_L.suptitle("Left subfigure")
fig_R.set_facecolor("paleturquoise")
fig_R.suptitle("Right subfigure")

axs_L = fig_L.subplots(
    nrows=2,
    ncols=1,
    sharex=True,
)
axs_L[1].set_xlabel("x [m]")

axs_R = fig_R.subplots(
    nrows=1,
    ncols=2,
    sharey=True,
)
axs_R[0].set_title("Axes 1")

plt.show()
