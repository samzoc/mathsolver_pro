import numpy as np
import time
from mathsolver_pro import geometry

print("Geometry benchmarks")

# Distance benchmark
a = np.random.rand(100000, 2)
b = np.random.rand(100000, 2)
t0 = time.time()
d = [geometry.distance(a[i], b[i]) for i in range(100000)]
t1 = time.time()
print(f"100k distances (2D): {t1-t0:.3f} s")

# Polygon area benchmark
poly = np.random.rand(10000, 2)
t0 = time.time()
area = geometry.polygon_area(poly)
t1 = time.time()
print(f"Polygon area (10k vertices): {t1-t0:.3f} s")

# Convex hull benchmark
t0 = time.time()
hull = geometry.convex_hull(poly)
t1 = time.time()
print(f"Convex hull (10k points): {t1-t0:.3f} s") 