import matplotlib.pyplot as plt
import numpy as np


y = np.random.randn(100)  # make 4 random data sets

x = np.arange(len(y))  # make an ordinal for this
fig, axs = plt.subplots(2, 1, layout="constrained")
axs[0].plot(x, y)
axs[0].set_title("Automatic ticks")

axs[1].plot(x, y)
axs[1].set_xticks(
    ticks=np.arange(0, 100, 30),  # Tick locators.
    labels=["zero", "30", "sixty", "90"],  # Tick formatters.
)
# axs[1].set_xticks([])  # Pass an empty list (set_xticks([])) to remove all ticks.
axs[1].set_yticks([-1.5, 0, 1.5])  # note that we don't need to specify labels
axs[1].set_title("Manual ticks")
plt.show()
