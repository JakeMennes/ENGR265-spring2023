import matplotlib.pyplot as plt
from scipy.special import factorial
import numpy as np

n = np.arange(start=1, step=1, stop=10)
factorials = factorial(n)

plt.scatter(n, factorials)
plt.plot(n, factorials)
plt.title('Growth of N!')
plt.show()
