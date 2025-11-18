import matplotlib.pyplot as plt
import numpy as np
from matplotlib.dates import ConciseDateFormatter


dates = np.arange(
    start=np.datetime64("2021-11-15"),
    stop=np.datetime64("2021-12-25"),
    step=np.timedelta64(1, "h"),
)
data = np.cumsum(np.random.randn(len(dates)))

fig, ax = plt.subplots(figsize=(5, 2.7), layout="constrained")
ax.plot(dates, data)
ax.xaxis.set_major_formatter(ConciseDateFormatter(ax.xaxis.get_major_locator()))
plt.show()
