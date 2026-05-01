"""it can have single row and multiple columns 
but cannot have multiple rows and single column
if you try it will automatically create a single row"""
import numpy as np
one_row_array = np.array([1,2,3,4])
one_column_array = np.array([1,
                             2,
                             3,
                             4])
print(one_row_array)
print(one_column_array)
""" they both are same in result """