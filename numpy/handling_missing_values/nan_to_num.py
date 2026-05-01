"""in this we will replace a nan to a specific value
default value is always zero"""
import numpy as np
array = np.array([2,3,np.nan,6,np.nan])
array2 = np.nan_to_num(array,nan=100)
print(array2)