"""use to split an array into parts 
three funcitons in it 
split function(equal parts), vsplit,hsplit"""
import numpy as np
two_d = np.array([[1,2,3],[4,5,6],[7,8,9]])
split1 = np.hsplit(two_d,3)
split2= np.vsplit(two_d,3)
split3 = np.split(two_d,3)
print(split3)