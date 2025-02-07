import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return (x ** 2 + 3 * x - 5)

x = np.arange(-10, 10.01, 0.1)

plt.plot(x, f(x))
plt.title(r'$\left(x^2+3x-5\right)^4$')
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()