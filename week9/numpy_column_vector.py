import numpy as np
def sol():
    np.random.seed(111)

    array = np.random.randn(3, 1)
    return array
print(sol())