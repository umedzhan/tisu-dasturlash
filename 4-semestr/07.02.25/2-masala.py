# 2-masala.py
import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return np.sqrt(x ** 2 + 2 * x + 1)

x = np.arange(-10, 10.01, 0.1)

plt.plot(x, f(x))
plt.title(r'$\sqrt{x^2 + 2x + 1}$')
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()