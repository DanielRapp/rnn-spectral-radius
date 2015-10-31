
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

data = []
for i in xrange(10000):
    variance = 2
    size = 10
    W = np.random.randn(size, size)*variance
    maxEig = max(list(abs(np.linalg.eigvals(W))))
    data.append(maxEig)

plt.hist(data, bins=np.linspace(0, 15, 100), color=[0.5, 0.5, 0.5], normed=True)
plt.xlabel(r'$\rho(W_{10,2})$')
plt.ylabel(r'P$[ \rho(W_{10,2}) ]$')
fig = plt.gcf()
fig.set_size_inches(10, 5.2)
fig.savefig('spectHist.png', dpi=100)

