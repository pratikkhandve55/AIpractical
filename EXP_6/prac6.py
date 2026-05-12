import numpy as np

# Activation function
def activation(x):
    return np.where(x >= 0, 1, -1)

# Input patterns
X = np.array([
    [1, -1, 1],
    [-1, 1, -1]
])

# Output patterns
Y = np.array([
    [1, 1],
    [-1, -1]
])

# Weight matrix initialization
W = np.zeros((X.shape[1], Y.shape[1]))

# Training using outer product
for i in range(len(X)):
    W += np.outer(X[i], Y[i])

print("Weight Matrix W:")
print(W)

# Test input
x_test = np.array([1, -1, 1])

print("\nInitial X:", x_test)

# Recall Y
y = activation(np.dot(x_test, W))
print("Recalled Y:", y)

# Recall X
x_recalled = activation(np.dot(y, W.T))
print("Recalled X:", x_recalled)