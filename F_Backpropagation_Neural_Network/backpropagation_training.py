"""Backpropagation is a supervised learning algorithm used in multilayer feedforward neural networks. It works by:

Forward propagating the input to compute output.

Calculating the error at the output.

Backpropagating the error to update weights."""

import numpy as np

# Sigmoid and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
def sigmoid_derivative(x):
    return x * (1 - x)

# Input and target output
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

y = np.array([[0], [0], [0], [1]])  # AND gate output

# Initialize weights and biases
np.random.seed(42)
input_layer_neurons = X.shape[1]  # 2 inputs
hidden_neurons = 2
output_neurons = 1

# Weights
hidden_weights = np.random.uniform(size=(input_layer_neurons, hidden_neurons))
output_weights = np.random.uniform(size=(hidden_neurons, output_neurons))

# Biases
hidden_bias = np.random.uniform(size=(1, hidden_neurons))
output_bias = np.random.uniform(size=(1, output_neurons))

# Training settings
learning_rate = 0.5
epochs = 10000

# Training loop
for epoch in range(epochs):
    # Forward Propagation
    hidden_input = np.dot(X, hidden_weights) + hidden_bias
    hidden_output = sigmoid(hidden_input)

    final_input = np.dot(hidden_output, output_weights) + output_bias
    final_output = sigmoid(final_input)

    # Backpropagation
    error = y - final_output
    d_output = error * sigmoid_derivative(final_output)

    error_hidden = d_output.dot(output_weights.T)
    d_hidden = error_hidden * sigmoid_derivative(hidden_output)

    # Update weights and biases
    output_weights += hidden_output.T.dot(d_output) * learning_rate
    output_bias += np.sum(d_output, axis=0, keepdims=True) * learning_rate
    hidden_weights += X.T.dot(d_hidden) * learning_rate
    hidden_bias += np.sum(d_hidden, axis=0, keepdims=True) * learning_rate

# Final output after training
print("Final output after training:")
print(np.round(final_output, 3))

# Test Predictions
print("\nTest Results (rounded):")
for i in range(len(X)):
    pred = sigmoid(np.dot(sigmoid(np.dot(X[i], hidden_weights) + hidden_bias), output_weights) + output_bias)
    print(f"Input: {X[i]} → Output: {np.round(pred[0], 3)}")
