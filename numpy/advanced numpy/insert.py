"""in this we insert an element in 1d and a row or column in 2d
axis 0 means row wise
axis 1 means column wise"""
import numpy as np
original_array = np.array([1,2,3,4])
one_d = np.insert(original_array,2,1,axis=None)
print(one_d)
original_array2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
two_d_row = np.insert(original_array2,1,[5,5,5],axis=0)
two_d_column = np.insert(original_array2,1,[5,5,5],axis=1)
print(two_d_column)
print(two_d_row)

