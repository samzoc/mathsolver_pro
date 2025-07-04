"""
Geometry module usage example
============================

Demonstrates distance, triangle area, convex hull, and plotting.
"""
from mathsolver_pro import geometry

# Distance between two points
p1, p2 = (0, 0), (3, 4)
d = geometry.distance(p1, p2)
print(f"Distance between {p1} and {p2}: {d}")  # Expected: 5.0

# Area of a triangle
A, B, C = (0, 0), (1, 0), (0, 1)
area = geometry.triangle_area(A, B, C)
print(f"Area of triangle ABC: {area}")  # Expected: 0.5

# Convex hull
pts = [(0, 0), (1, 0), (0, 1), (1, 1), (0.5, 0.5)]
hull = geometry.convex_hull(pts)
print(f"Convex hull: {hull}")  # Expected: [(0,0), (1,0), (1,1), (0,1)] 