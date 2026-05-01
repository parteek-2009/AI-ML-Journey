"""we will change the infinity values with a specific number"""
import numpy as np
array = np.array([1,2,np.inf,5,-np.inf])
array2 = np.nan_to_num(array,posinf=3,neginf=3)
print(array2)