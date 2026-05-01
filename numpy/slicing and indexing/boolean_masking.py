#this is used to filter data from an array by giving a specific condition
import numpy as np
universal_array = np.array([1,2,3,4,4,5,65,34,33,656,34])
more_than_hundred = universal_array[universal_array >= 10]
print(more_than_hundred)