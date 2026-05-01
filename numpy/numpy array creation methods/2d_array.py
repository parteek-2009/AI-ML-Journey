"""it can have multiple rows and multiple columns
also called matrix as we studied
just like class 12th matrices we can add and subract them
they are only called matrix because they look structrually
like them also they dont follow the multiplication rule
of matrices"""
import numpy as np
two_d_array1 = np.array([
    [2,3,56,64],
    [3,4,6,45],
    [3,4,5,5]
])
two_d_array2 = np.array([
    [2,3,6,6],
    [3,4,6,5],
    [4,6,3,3]
])
add_result_array = (two_d_array1+two_d_array2)
multiplicative_result = (two_d_array1*two_d_array2)
print(multiplicative_result)


