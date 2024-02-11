# Let x be a ndarray [10, 10, 3] with all elements set to one. Reshape x so
# that the size of the second dimension equals 150

import numpy as np

arr = np.ones((10, 10, 3))

reshaped_arr = arr.reshape((2, 150))

print(arr)
print(reshaped_arr.shape)
print(reshaped_arr)