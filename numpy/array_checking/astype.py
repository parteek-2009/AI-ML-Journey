#use to change a certain datatype to another
#note = do changes which are possible 
import numpy as np
arr_int = np.array([2,3])
arr_float = arr_int.astype(float)
print(arr_int)
print(arr_float)
arr_str = np.array(["3","33"])
arr_str_to_int = arr_str.astype(int)
print(arr_str)
print(arr_str_to_int)