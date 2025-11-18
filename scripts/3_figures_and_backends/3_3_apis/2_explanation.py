from matplotlib import pyplot as plt


# plt.plot is called on current figure and current axes

x = [1, 2, 3, 4]
y = [0, 0.5, 1, 0.2]

fig_1, axs_1 = plt.subplots(
    nrows=2,
    ncols=2,
    figsize=(4, 3),
    layout="constrained",
)

current_fig = plt.gcf()
current_ax = plt.gca()
print(f"{fig_1 is current_fig = }")
print(f"{current_ax is axs_1[-1][-1] = }")
plt.plot(x, y)

fig_2, axs_2 = plt.subplot_mosaic(
    mosaic=[["A", "right"], ["B", "right"]],
    figsize=(4, 3),
    layout="constrained",
)

current_fig = plt.gcf()
current_ax = plt.gca()
print(f"{fig_2 is current_fig = }")
print(f"{current_ax._label = }")
plt.plot(x, y)

plt.show()
