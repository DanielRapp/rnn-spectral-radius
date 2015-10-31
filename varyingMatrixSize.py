
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

sizes = range(0, 105, 5)[1:]
coeffs = []
for size in sizes:
    expectedRadius = []
    var = list(np.linspace(0.1, 10, 10))
    for variance in var:
	eigs = []
	variance = variance * 1/np.sqrt(size)
	for i in xrange(1000):
	    W = np.random.randn(size, size)*variance
	    maxEig = max(list(abs(np.linalg.eigvals(W))))
	    eigs.append(maxEig)

	expectedRadius.append(np.mean(eigs))

    d = [ el[0]/el[1] for el in zip(expectedRadius, var) ]
    coeffs.append(np.mean(d))
    print size, coeffs[-1]

plt.plot(sizes, coeffs, '-o', color=[0.5, 0.5, 0.5], linewidth=3)
plt.ylabel('Scaling factor from the\n (normalized) variance to the spectral radius')
plt.xlabel(r'Matrix size ($n$)')
plt.ylim(ymax=1.5)
plt.ylim(ymin=0.0)
fig = plt.gcf()
fig.set_size_inches(10, 5.2)
fig.savefig('normalizedVaryingMatrixSize.png', dpi=100)

