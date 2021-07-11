import numpy as np

def cost(y, y_hat):
    c = sum(0.5 * (y - y_hat)**2)
    return c

y = np.array([[1], [2]])
y_hat = np.array([[2], [2]])
print(cost(y, y_hat))