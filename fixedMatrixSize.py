
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

data = []
var = list(np.linspace(0.1, 10, 100))
for variance in var:
    eigs = []
    for i in xrange(1000):
	size = 10
	W = np.random.randn(size, size)*variance
	maxEig = max(list(abs(np.linalg.eigvals(W))))
	eigs.append(maxEig)

    data.append(np.mean(eigs))

# Uncomment to get coefficient
#d = [ el[0]/el[1] for el in zip(data, var) ]
#print np.mean(d)

plt.plot(var, data, '-o', color=[0.5, 0.5, 0.5], linewidth=3)
plt.ylabel(r'E$\{ \rho(W_{10,v})\}$')
plt.xlabel(r'Variance ($v$)')
fig = plt.gcf()
fig.set_size_inches(10, 5.2)
fig.savefig('fixedMatrixSize.png', dpi=100)


