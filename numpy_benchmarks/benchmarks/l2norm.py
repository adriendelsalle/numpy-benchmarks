#from: http://stackoverflow.com/questions/7741878/how-to-apply-numpy-linalg-norm-to-each-row-of-a-matrix/7741976#7741976
#setup: import numpy as np ; np.random.seed(0); N = 1000; x = np.random.rand(N,N)
#run: l2norm(x)

#pythran export l2norm(float64[][])
import numpy as np
def l2norm(x):
    return np.sqrt(np.sum(np.abs(x)**2, 1))
