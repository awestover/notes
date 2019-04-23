# this is a test using some weird variable names

import matplotlib.pyplot as plt
import numpy as np
σ = 10
μ = 5
N = 100
X = np.random.normal(σ, μ, N)
plt.hist(X)
plt.show()
