"""it is just simpler version of concatcenate
there are two things in  this: V stack and H stack"""
import numpy as np
array = np.array([1,2,3])
array1 = np.array([4,5,6])
vstack = np.vstack(((array,array1)))#can make 2d array with 1d array
hstack = np.hstack(((array,array1)))
# print(hstack)
# print(vstack)

array_1d = np.array([[1,2,3],[4,5,6]])
array_1d1 = np.array([[1,1,1],[2,2,2]])
twoD_vstack = np.vstack(((array_1d,array_1d1)))
twoD_hstack = np.hstack(((array_1d,array_1d1)))
# print(twoD_vstack)
# print(twoD_hstack)