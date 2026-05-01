"""just like ravel it will change from any dimention to 1d dimention
but it will always return a copy so making a variable and then doing manuplations to 
it will not affect any original data"""
import numpy as np
array1 = np.array([[1,2,3],[4,5,6]])
array2 = array1.flatten()
print(array2)