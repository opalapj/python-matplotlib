import matplotlib.pyplot as plt
import numpy as np


angle = np.arange(0.0, 4 * np.pi, 0.1)
y = np.cos(angle)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7, 2.7), layout="constrained")

(l1,) = ax1.plot(angle, y)
ax1_ = ax1.twinx()
(l2,) = ax1_.plot(angle, range(len(angle)), "C1")
ax1_.legend(
    handles=[l1, l2],
    labels=["Sine (left)", "Straight (right)"],
)

ax2.plot(angle, y)
ax2.set_xlabel("Angle [rad]")
ax2_ = ax2.secondary_xaxis(
    location="top",
    functions=(np.rad2deg, np.deg2rad),
)
ax2_.set_xlabel("Angle [°]")

plt.show()
