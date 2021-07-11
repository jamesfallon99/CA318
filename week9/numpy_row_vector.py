import numpy as np
def sol():
    np.random.seed(111)

    numpy_array = np.random.randn(3, 1)
    row = numpy_array.T #T transposes the vector... so (3,1) becomes (1,3)
    return row
print(sol())