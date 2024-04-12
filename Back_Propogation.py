import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def backpropagation(weights, inputs, outputs):
    error = outputs - sigmoid(np.dot(inputs, weights))
    gradient = error * sigmoid(np.dot(inputs, weights)) * (1 - sigmoid(np.dot(inputs, weights)))
    weights = weights - np.dot(inputs.T, gradient)
    return weights

inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
outputs = np.array([0, 1, 1, 0])
weights = np.array([[0.5, 0.5], [0.5, 0.5]])

for i in range(100):
    weights = backpropagation(weights, inputs, outputs)

print(weights)