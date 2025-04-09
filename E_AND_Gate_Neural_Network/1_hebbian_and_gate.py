

import numpy as np

# Input: [Bias, X1, X2]
inputs = np.array([
    [1, 0, 0],
    [1, 0, 1],
    [1, 1, 0],
    [1, 1, 1]
])

# Target output for AND gate
targets = np.array([0, 0, 0, 1])

# Initialize weights to 0
weights = np.zeros(3)

# Hebbian Learning Rule: w = w + x * y
for i in range(len(inputs)):
    weights += inputs[i] * targets[i]

# Activation function
def activation(x):
    return 1 if x >= 1 else 0

# Prediction
print("Trained weights:", weights)
print("Testing AND gate using Hebbian Neural Net:")
for i in range(len(inputs)):
    x = inputs[i]
    output = activation(np.dot(weights, x))
    print(f"Input: {x[1:]} → Output: {output} (Target: {targets[i]})")
