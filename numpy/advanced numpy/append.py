"""data will append at the end """
import numpy as np
original_array = np.array([[1,2,3],[4,5,6]])
appended_array_column = np.append(original_array,[[7],[8]],axis=1)
appended_array_row = np.append(original_array, [[7,8,9]],axis=0)
print(appended_array_column)
print(appended_array_row)

