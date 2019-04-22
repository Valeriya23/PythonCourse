import numpy as np
import matplotlib.pyplot as plt
poisson = np.random.poisson(8, 10000)
plt.hist(poisson)
plt.show()
