import numpy as np


def one_hot_encode(y):
    encoded_y = np.zeros(10)
    encoded_y[y] = 1
    return encoded_y


def encode_probabilities(y):
    max_prob = 0
    max_prob_pos = 0

    for i in range(len(y)):
        if y[i] > max_prob:
            max_prob = y[i]
            max_prob_pos = i

    encoded_y = np.zeros(y.shape)
    encoded_y[max_prob_pos] = 1
    return encoded_y


def preprocess(X, y, set_features_as_rows=True):
    m = len(X)
    n = len(X[0]) ** 2
    # preprocess X... flatten
    X = X.numpy().reshape(m, n)
    # preproces y... one_hot_encode it
    y_encoded = []
    for i in range(len(y)):
        encoding = one_hot_encode(y[i])
        y_encoded.append(encoding)
    y = y_encoded
    # Convert to numpy arrays
    X = np.array(X)
    y = np.array(y)
    # Transpose if you want features as rows and samples as columns
    if set_features_as_rows:
        X = X.transpose()
        y = y.transpose()
    return X, y


def shorten(X, y, start, end):
    features = X[:, start:end]
    target = y[:, start:end]
    # np.array([X[, start:length]])
    # target = np.array([y[, start:length]])
    return features, target


def decode(encoded_y):
    value = 0
    for i in range(len(encoded_y)):
        if encoded_y[i] == 1:
            value = i
    return value
