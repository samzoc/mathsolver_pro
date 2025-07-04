import numpy as np
from mathsolver_pro import geometry

def test_distance():
    assert np.isclose(geometry.distance((0,0), (3,4)), 5.0)

def test_triangle_area():
    a, b, c = (0,0), (1,0), (0,1)
    assert np.isclose(geometry.triangle_area(a, b, c), 0.5)

def test_polygon_perimeter():
    square = [(0,0), (1,0), (1,1), (0,1)]
    assert np.isclose(geometry.polygon_perimeter(square), 4.0)

def test_polygon_area():
    square = [(0,0), (1,0), (1,1), (0,1)]
    assert np.isclose(geometry.polygon_area(square), 1.0)

def test_circle_area():
    assert np.isclose(geometry.circle_area(1), np.pi)

def test_circle_perimeter():
    assert np.isclose(geometry.circle_perimeter(1), 2*np.pi)

def test_sphere_volume():
    assert np.isclose(geometry.sphere_volume(1), 4/3*np.pi)

def test_sphere_surface():
    assert np.isclose(geometry.sphere_surface(1), 4*np.pi)

def test_convex_hull():
    pts = [(0,0), (1,0), (0,1), (1,1), (0.5,0.5)]
    hull = geometry.convex_hull(pts)
    assert set(hull) == set([(0,0), (1,0), (1,1), (0,1)])

def test_rotate_2d():
    p = (1,0)
    p_rot = geometry.rotate_2d(p, np.pi/2)
    assert np.allclose(p_rot, (0,1), atol=1e-7)

def test_translate():
    assert geometry.translate((1,2), (3,4)) == (4,6) 