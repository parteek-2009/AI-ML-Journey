#arange function is like range function of python
#it return our range in array
#have to pass(start,stop,step) where step is defaultly one and stop will be excluded
import numpy as np
without_step = np.arange(1,10)
with_step = np.arange(1,10,3)
print(f"without step the range is : {without_step}")
print(f"with step the range is : {with_step}")
