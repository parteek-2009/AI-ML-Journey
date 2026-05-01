"""using reshaping we can go form lower dimentions to higher
dimentions and higher dimentions to lower dimentions"""
import numpy as np
arr = np.array([1,2,3,4])
arr_reshaped = arr.reshape(2,2)
print(arr_reshaped)# 1D to 2D array
arr_3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
arr_2d = arr_3d.reshape(4,3)
print(arr_2d)#3d to 2d array