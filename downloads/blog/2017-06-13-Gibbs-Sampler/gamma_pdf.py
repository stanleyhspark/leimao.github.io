import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gamma

a = 5
b = 10

fig, ax = plt.subplots(1, 1)
x = np.linspace(gamma.ppf(0.01, a, scale = 1./b),gamma.ppf(0.99, a, scale= 1./b), 100)
ax.plot(x, gamma.pdf(x, a, scale = 1./b),'r-', lw=5, alpha=0.6, label='gamma pdf')
plt.show()