# 3-masala
import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return 1 / (x ** 3 + x - 2) ** 2

x = np.arange(0.80, 1.1, 0.001)

plt.plot(x, f(x))
plt.title(r'$\frac{1}{(x^3 + x - 2)^2}$')
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()