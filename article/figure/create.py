from math import pi

import dufte
import matplotlib.pyplot as plt
import numpy
import tikzplotlib

plt.style.use(dufte.style)


def nsphere(n):
    if n == 1:
        return 2
    elif n == 2:
        return 2 * pi

    return nsphere(n - 2) * 2 * pi / (n - 2)


def nball(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2

    return nball(n - 2) * 2 * pi / n


x = numpy.arange(21)
y0 = [nball(n) for n in x]
y1 = [nsphere(n) for n in x[1:]]

plt.plot(x, y0, "o", label="n-ball")
plt.plot(x[1:], y1, "o", label="n-sphere")
dufte.legend()
plt.xlabel("n")
# plt.show()
tikzplotlib.save("fig1.tex")
