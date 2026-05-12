# Perceptron Decision Boundary with Labels 0 and 1

import numpy as np
import matplotlib.pyplot as plt

# Step 1: Create Linearly Separable Dataset
# Class 1
X_class1 = np.array([[2, 3], [3, 3], [3, 4], [5, 5]])
# Class 0
X_class0 = np.array([[1, 1], [2, 1], [2, 2], [3, 1]])

X = np.vstack((X_class1, X_class0))
y = np.array([1]*len(X_class1) + [0]*len(X_class0))

# Step 2: Initialize weights and bias
weights = np.zeros(2)
bias = 0
learning_rate = 0.1
epochs = 20

# Step 3: Perceptron Training (for 0 and 1 labels)
for _ in range(epochs):
    for i in range(len(X)):
        linear_output = np.dot(X[i], weights) + bias
        prediction = 1 if linear_output >= 0 else 0
        
        # Update Rule
        error = y[i] - prediction
        weights = weights + learning_rate * error * X[i]
        bias = bias + learning_rate * error

print("Final Weights:", weights)
print("Final Bias:", bias)

# Step 4: Plot Data and Decision Boundary
plt.figure()

# Plot class 1 and class 0 points
plt.scatter(X_class1[:, 0], X_class1[:, 1], label = "class 1")
plt.scatter(X_class0[:, 0], X_class0[:, 1], label = "class 0")

# Decision boundary: w1*x1 + w2*x2 + b = 0
x_values = np.linspace(0, 6, 100)

# Avoid division by zero
if weights[1] != 0:
    y_values = -(weights[0] * x_values + bias) / weights[1]
    plt.plot(x_values, y_values)

plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("Perceptron Decision Boundary (Labels 0 and 1)")
plt.legend()
plt.show()