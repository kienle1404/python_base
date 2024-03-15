# Let x be array [[1, 2, 3], [4, 5, 6]]. Convert it to [1 4 2 5 3 6].

import numpy as np

x = np.array([[1, 2, 3], [4, 5, 6]])
y = np.transpose(x)
result = y.reshape(1, 6)

print(y)
print(y.shape)
print(result)
