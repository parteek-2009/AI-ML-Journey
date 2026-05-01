import numpy as np
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr_1= np.delete(arr,0,axis=0)
arr_2 = np.delete(arr,0,axis=1)
print(arr_1)
print(arr_2)