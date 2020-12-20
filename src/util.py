import numpy as np

# One hot encodes an integer into an array of 0s and 1s


def one_hot_encode(y):
    encoded_y = np.zeros(10)
    encoded_y[y] = 1
    return encoded_y

# Takes an array of probabilities, replaces the highest probabiliy with 1, and the rest with 0s


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

# Takes in the X and y, and prepares them for the NN class used in Task 2. This involves:
# - flattening the tensor
# - converting tensores to numpy arrays
# - transposing the input, so that features are rows, and samples are colums
# - one-hot encoding all targets
# Returns two numpy arrays for targets and features


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

# Takes the features and targe arrays, and slices them using the specied psotions.
# Useful for reducing the size of the training set for the purposes of testing the network.


def shorten(X, y, start, end):
    features = X[:, start:end]
    target = y[:, start:end]
    return features, target

# Takes in a one-hot encoding array of 0s and 1s, and translates it back to an integer.


def decode(encoded_y):
    value = 0
    for i in range(len(encoded_y)):
        if encoded_y[i] == 1:
            value = i
    return value
