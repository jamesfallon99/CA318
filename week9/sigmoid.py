import numpy as np

def sigmoid(z):
   return 1 / (1 + np.exp(-z))

def sol():
    numpy_array = np.array([[0.24, 0.92, 0.31, 0.4, ],[0.04, 0.61, 0.29, 0.45, ],[0.39, 0.33, 0.18, 0.15, ]])
    s = sigmoid(numpy_array)
    return s

print(sol())