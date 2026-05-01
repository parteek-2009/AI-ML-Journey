#In this we will find out how to get a particular range of items in an array
#slice format[start,stop,step]
import numpy as np
array_oneD = np.array([0,1,2,3,4])
print(array_oneD[0:3])#last element will be exculuded
print(array_oneD[::-1])#to reverse all element in an array
print(array_oneD[0:5:2])
array_twoD = np.array([[1,2,3,4],[5,6,7,8]])
print(array_twoD[0,0:3])
array_threeD = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(array_threeD[0,1,:])
