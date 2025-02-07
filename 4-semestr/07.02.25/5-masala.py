# 5-masala
import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return np.log(x ** 2 + 1)

x = np.arange(-1, 1.001, 0.001)

plt.plot(x, f(x))
plt.title(r'$ln\left(x^2 + 1\right)$')
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()