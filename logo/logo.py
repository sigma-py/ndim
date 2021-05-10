import matplotlib.pyplot as plt
from numpy import cos, pi, sin

ax = plt.gca()

n = 24
r0 = 0.5
r1 = 0.5
for k in range(n):
    center = (r0 * cos(2 * k * pi / n), r0 * sin(2 * k * pi / n))
    circle1 = plt.Circle(center, r1, ec="#555", linewidth=2.0, fill=False)
    ax.add_patch(circle1)

# fig.savefig('plotcircles.png')
plt.xlim(-2, 2)
plt.ylim(-2, 2)
ax.set_aspect("equal")
plt.axis("off")

# plt.show()
plt.savefig("logo.svg", transparent=True, bbox_inches="tight")
