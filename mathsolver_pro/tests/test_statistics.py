import numpy as np
from mathsolver_pro import statistics

def test_mean():
    assert statistics.mean([1,2,3,4,5]) == 3.0

def test_std():
    assert np.isclose(statistics.std([1,2,3,4,5]), 1.4142, atol=1e-3)

def test_median():
    assert statistics.median([1,2,3,4,5]) == 3.0

def test_mode():
    assert statistics.mode([1,2,2,3,4]) == 2.0

def test_correlation():
    assert np.isclose(statistics.correlation([1,2,3], [2,4,6]), 1.0) 