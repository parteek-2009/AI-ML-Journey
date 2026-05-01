""" IN this we will add 1d array to 2d array and the elemtns of 1d
array will add up to two d array indexing wise 
but the the elements in a row should be same"""
import numpy as np
"""----------------------------------------------------------------------------------------"""
"""horizontally"""
one_d_array_h = np.array([1,1,1])
two_d_array_h = np.array([[1,1,1],[2,2,2]])
adding = one_d_array_h+two_d_array_h
print(adding)
"""------------------------------------------------------------------------------------------"""
"""vertically without reshaping(with 2d dimention)"""
one_d_array_v1 = np.array([[1],[1]])
two_d_array_v1 = np.array([[1,1,1],[2,2,2]])
adding = one_d_array_v1+two_d_array_v1
print(adding)
"""-------------------------------------------------------------------------------------------"""
"""vertically with reshaping 1d array"""
one_d_array_v2 = np.array([1,1])
reshaped = one_d_array_v2.reshape(2,1)
two_d_array_v2 = np.array([[1,1,1],[2,2,2]])
adding = reshaped+two_d_array_v2
print(adding)