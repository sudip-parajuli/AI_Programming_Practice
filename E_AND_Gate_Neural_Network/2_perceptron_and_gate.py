# 8_perceptron_and_gate.py

import numpy as np

# Input: [Bias, X1, X2]
inputs = np.array([
    [1, 0, 0],
    [1, 0, 1],
    [1, 1, 0],
    [1, 1, 1]
])

# AND Gate output
targets = np.array([0, 0, 0, 1])

# Initialize weights and set learning rate
weights = np.zeros(3)
learning_rate = 1
epochs = 10

# Activation function
def activation(x):
    return 1 if x >= 0 else 0

# Perceptron Training
for epoch in range(epochs):
    print(f"Epoch {epoch+1}")
    for i in range(len(inputs)):
        x = inputs[i]
        target = targets[i]
        output = activation(np.dot(weights, x))
        error = target - output
        weights += learning_rate * error * x
        print(f" Input: {x[1:]}, Output: {output}, Error: {error}, Updated Weights: {weights}")
    print("-" * 40)

# Final Test
print("Final weights after training:", weights)
print("Testing Perceptron on AND gate:")
for x in inputs:
    out = activation(np.dot(weights, x))
    print(f"Input: {x[1:]}, Output: {out}")
