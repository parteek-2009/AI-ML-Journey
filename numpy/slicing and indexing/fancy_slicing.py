#if you want elements from an array in random steps in the form of an array you can use this
import numpy as np
universal_array = np.array([1,2,3,4,5,6,7,8,9])
sub_array = universal_array[[0,3,4,8]]
print(sub_array)
