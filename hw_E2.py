import numpy as np
import matplotlib.pyplot as plt
pareto= np.random.pareto(20,100)
plt.hist(pareto)
plt.show()
