"""it is used to specifically go form highr dimentions to 1d array
but making new variable of that changed array and after doing manuplations
with it can change the original array also, but printing will not"""

import numpy as np
orig_array = np.array([[1,2,3],[4,5,6]])
raveled_array = orig_array.ravel()
print(raveled_array)
