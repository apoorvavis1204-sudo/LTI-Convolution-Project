"""
Convolution of Signals in a Linear Time-Invariant (LTI) System
Run: python convolution_lti.py

The script:
1. Defines two discrete-time signals x[n] and h[n].
2. Computes y[n] = x[n] * h[n] using linear convolution.
3. Plots the input signals and the output.
4. Prints the numerical convolution result.
"""

import numpy as np
import matplotlib.pyplot as plt

# Step 1: Define the discrete-time input signal x[n]
x = np.array([1, 2, 1, 0])
nx = np.arange(0, len(x))

# Step 2: Define the impulse response h[n] of the LTI system
h = np.array([1, 1, 1])
nh = np.arange(0, len(h))

# Step 3: Perform linear convolution
y = np.convolve(x, h, mode="full")
ny = np.arange(0, len(y))

# Step 4: Display the result
print("Input signal x[n]:", x)
print("Impulse response h[n]:", h)
print("Output signal y[n] = x[n] * h[n]:", y)

# Step 5: Plot input signals and convolution output
fig, axes = plt.subplots(3, 1, figsize=(9, 8))

axes[0].stem(nx, x)
axes[0].set_title("Input Signal x[n]")
axes[0].set_xlabel("n")
axes[0].set_ylabel("Amplitude")
axes[0].grid(True)

axes[1].stem(nh, h)
axes[1].set_title("Impulse Response h[n]")
axes[1].set_xlabel("n")
axes[1].set_ylabel("Amplitude")
axes[1].grid(True)

axes[2].stem(ny, y)
axes[2].set_title("Output Signal y[n] = x[n] * h[n]")
axes[2].set_xlabel("n")
axes[2].set_ylabel("Amplitude")
axes[2].grid(True)

plt.tight_layout()
plt.savefig("convolution_graph.png", dpi=300, bbox_inches="tight")
plt.show()
