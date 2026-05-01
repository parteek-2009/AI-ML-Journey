#we will do basic operations in this with whole array
import numpy as np
general_array = np.array([[4,3,2,4],[3,2,5,3]])
add = general_array + 1
multiply = general_array *2
divide = general_array/2
double_divide = general_array//2
modulus = general_array%2
print(general_array)
print(f"add = {add},multiply = {multiply},divide = {divide},modulus = {modulus},double_divide = {double_divide}")
