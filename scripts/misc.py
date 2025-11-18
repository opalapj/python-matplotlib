import matplotlib.pyplot as plt


plt.get_fignums()  # Return a list of existing figure numbers.
plt.get_figlabels()  # Return a list of existing figure labels.

plt.gcf()  # Get the current figure. If there is currently no figure on the pyplot figure stack, a new one is created using figure().
plt.gca()  # Get the current axes. If there is currently no Axes on this Figure, a new one is created using figure.add_subplot().

fig1 = plt.figure()  # Create a new figure, or activate an existing figure.
fig2 = plt.subplots()  # Create a figure and a set of subplots.

plt.subplot()  # Add an Axes to the current figure or retrieve an existing Axes.
plt.axes()  # Add an Axes to the current figure and make it the current Axes.
ax3 = plt.axes(
    label="third"
)  # Add an Axes to the current figure and make it the current Axes.

plt.ion()  # Enable interactive mode.
plt.ioff()  # Disable interactive mode.
plt.isinteractive()  # Return whether plots are updated after every plotting command.
plt.show()  # Display all open figures. https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib-pyplot-show
plt.close(
    "all"
)  # Close a figure window. https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.close.html#matplotlib-pyplot-close

# In interactive mode:
# - newly created figures will be shown immediately;
# - figures will automatically redraw on change;
# - pyplot.show will not block by default.

# In non-interactive mode:
# - newly created figures and changes to figures will not be reflected until explicitly asked to be;
# - pyplot.show will block by default.

fig, ax = plt.subplots()
ax.plot([0, 1, 2], [0, 1, 1])
plt.title("title")
