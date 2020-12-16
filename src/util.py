import numpy as np


def one_hot_encode(y):
    encoded_y = np.zeros(10)
    encoded_y[y] = 1
    return encoded_y


def preprocess(X, y, m, n):
    # preprocess X... flatten
    X = X.numpy().reshape(m, n)
    # preproces y... one_hot_encode it
    y_encoded = []
    for i in range(len(y)):
        encoding = one_hot_encode(y[i])
        y_encoded.append(encoding)
    y = y_encoded
    return X, y
