import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def sol():
    # Input data
    X = np.array( ([3,5],[5,1],[10,2]) , dtype = float)

    # output vector
    y = np.array( ([75], [82], [93]) , dtype = float)

    # scale the input and output data
    X = X / np.amax(X,axis=0)
    y = y / 100

    # define network parameters
    size_input = np.shape(X)[1] # number of columns of X
    size_hidden = 3
    size_output = 1

    # Create the weights
    np.random.seed(111)
    W1 = np.random.randn(size_input, size_hidden) #size input and 3 --looked at previous class question to get arguments
    W2 = np.random.randn(size_hidden, size_output)

    # A dot product of the weights by the inputs provides the values for the next layer (z)
    z2 = np.dot(X, W1)

    a2 = sigmoid(z2)
    
    z3 = np.dot(a2, W2)
    y_hat = sigmoid(z3)

    return y_hat