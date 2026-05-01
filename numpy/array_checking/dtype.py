#we will check the datatype of a particular array(float,str,int)
#do not mix the data in numpy it works best at homogenious data
import numpy as np
array_str = np.array(["apple","banana"])
array_int = np.array([3,4,3])
array_float = np.array([4.0,3.3])
print(array_str.dtype,array_int.dtype,array_float.dtype)