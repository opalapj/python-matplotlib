# Runtime:
# 1. say hello
# 2. create plot and wait for close (due to interactive mode off and plt.show())
# 3. say goodbye

# For debugging step by step, it is necessary to activate:
# - plt.ion() - start interactive mode to inspect figure creation step by step
# - plt.ioff() - end interactive mode to preserve one of plt.show() behavior
#   i.e. blocking runtime and waiting for the figure to close.

# Debug with python -m pdb debugging_example.py
# Debugging with PyCharm does not work properly.


import matplotlib.pyplot as plt


def say_hello():
    print("hello")


def say_goodbye():
    print("goodbye")


def create_plot():
    plt.ion()
    fig = plt.figure(
        figsize=(4, 2),
        facecolor="lightskyblue",
        layout="constrained",
    )
    fig.suptitle("A nice Matplotlib Figure")
    ax = fig.add_subplot()
    ax.set_title(
        "Axes",
        loc="left",
        fontstyle="oblique",
        fontsize="medium",
    )
    plt.ioff()
    plt.show()


def main():
    say_hello()
    create_plot()
    say_goodbye()


if __name__ == "__main__":
    main()
