"""
Statistics module usage example
==============================

Demonstrates mean, standard deviation, median, mode, and correlation.
"""
from mathsolver_pro import statistics

# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Mean and standard deviation
mean = statistics.mean(x)
std = statistics.std(x)
print(f"Mean: {mean}, Std: {std}")  # Expected: Mean: 3.0, Std: ~1.414

# Median and mode
median = statistics.median(x)
mode = statistics.mode([1, 2, 2, 3, 4])
print(f"Median: {median}, Mode: {mode}")  # Expected: Median: 3.0, Mode: 2.0

# Correlation
corr = statistics.correlation(x, y)
print(f"Correlation: {corr}")  # Expected: 1.0 