"""we can join 2 or more arrays by concatenate"""
import numpy as np
arr_2d = np.array([[3,4,5],[6,7,8],[1,2,9]])
arr2_2d = np.array([[2,3,4],[3,3,3],[1,2,1]])
arry_add_column = np.concatenate((arr_2d,arr2_2d),axis=1)
arry_add_row = np.concatenate(arr_2d,arr2_2d,axis=0)