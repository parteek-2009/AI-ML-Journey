"""we can use this to find an element that we left in a missing
value 
nan means [not a number]
it will return true or false"""

import numpy as np
array = np.array([[1,2,np.nan],[np.nan,5,6]])
print(np.isnan(array))
""" changing nan to specific values """
array[0,2] = 3
array[1,0] = 1
print(array)