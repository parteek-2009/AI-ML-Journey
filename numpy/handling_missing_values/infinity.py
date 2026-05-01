"""in this we will check is there any value
which is infinty or not if it is it will return true
"""
import numpy as np
array = np.array([1,2,np.inf,4,-np.inf])
print(np.isinf(array))