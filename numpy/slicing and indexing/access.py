#in this we will access a particular element in an array
import numpy as np
one_d_array = np.array([3,4,4,4])
two_d_array = np.array([[3,3], [2,2]])
three_d_array = np.array([[[4,4],[3,3]],[[2,2],[1,1]]])
print(one_d_array[1])
print(two_d_array[0,1])
print(three_d_array[0,1,0])