"""
Statistics module
================

Descriptive statistics, correlation, and probability tools.

Examples:
>>> from mathsolver_pro import statistics
>>> statistics.mean([1,2,3,4,5])
3.0
>>> statistics.std([1,2,3,4,5])
1.4142...
>>> statistics.correlation([1,2,3], [2,4,6])
1.0
"""
import numpy as np
from scipy import stats as sps

def mean(data):
    """Compute the mean of a dataset."""
    return float(np.mean(data))

def std(data):
    """Compute the standard deviation of a dataset."""
    return float(np.std(data, ddof=0))

def median(data):
    """Compute the median of a dataset."""
    return float(np.median(data))

def mode(data):
    """Compute the mode of a dataset."""
    return float(sps.mode(data, keepdims=True).mode[0])

def correlation(x, y):
    """Compute the Pearson correlation coefficient between two datasets."""
    return float(np.corrcoef(x, y)[0,1]) 