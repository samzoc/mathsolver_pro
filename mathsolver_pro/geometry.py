"""
Geometry module
==============

Analytic, solid, and computational geometry: distances, areas, perimeters, volumes, intersections, transformations, convex hull, and plotting.

Examples:
>>> from mathsolver_pro import geometry
>>> geometry.distance((0,0), (3,4))
5.0
>>> geometry.triangle_area((0,0), (1,0), (0,1))
0.5
>>> geometry.convex_hull([(0,0), (1,0), (0,1), (1,1), (0.5,0.5)])
[(0, 0), (1, 0), (1, 1), (0, 1)]
"""
import numpy as np
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt

def distance(p1, p2):
    """Euclidean distance between two points (2D/3D)."""
    return float(np.linalg.norm(np.array(p1) - np.array(p2)))

def triangle_area(a, b, c):
    """Area of a triangle (2D/3D)."""
    a, b, c = map(np.array, (a, b, c))
    return 0.5 * np.linalg.norm(np.cross(b-a, c-a))

def polygon_perimeter(vertices):
    v = np.array(vertices)
    return float(np.sum(np.linalg.norm(v - np.roll(v, -1, axis=0), axis=1)))

def polygon_area(vertices):
    v = np.array(vertices)
    x, y = v[:,0], v[:,1]
    return 0.5 * abs(np.dot(x, np.roll(y, -1)) - np.dot(y, np.roll(x, -1)))

def circle_area(r):
    return float(np.pi * r**2)

def circle_perimeter(r):
    return float(2 * np.pi * r)

def sphere_volume(r):
    return float(4/3 * np.pi * r**3)

def sphere_surface(r):
    return float(4 * np.pi * r**2)

def convex_hull(points):
    points = np.array(points)
    hull = ConvexHull(points)
    return [tuple(points[v]) for v in hull.vertices]

def rotate_2d(p, theta, center=(0,0)):
    p, center = np.array(p), np.array(center)
    R = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
    return tuple(np.dot(R, p-center) + center)

def translate(p, v):
    return tuple(np.array(p) + np.array(v))

def plot_polygon(vertices, show=True):
    v = np.array(vertices)
    plt.plot(*np.append(v, [v[0]], axis=0).T, marker='o')
    plt.axis('equal')
    if show:
        plt.show()
    return v

def plot_convex_hull(points, show=True):
    hull_pts = convex_hull(points)
    plot_polygon(hull_pts + [hull_pts[0]], show=show)
    return hull_pts 