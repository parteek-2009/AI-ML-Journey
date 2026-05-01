#n stands for number and dim stands for dimentions, so number of dimentions
import numpy as np
array_1d = np.array([3,4,4])
array_2d = np.array([[3,3,4], [6,6,6], [2,2,2]])
array_3d = np.array([[[3,4],[3,2]] , [[3,2],[3,2]] ])
array_4d = np.array([[[[3,3,3],[3,3,2]] ,[[3,3,2], [4,3,2]]] , [[[3,3,3],[3,3,2]] ,[[3,3,2], [4,3,2]]]])
print(array_1d.ndim, array_2d.ndim, array_3d.ndim,array_4d.ndim)