# 4-masala
import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return np.exp(x ** 2 + 3 * x)

x = np.arange(9, 10.001, 0.001)

plt.plot(x, f(x))
plt.title(r'$e^{x^2 + 3x}$')
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()