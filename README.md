# MathSolver Pro

MathSolver Pro is a modular, advanced mathematics library for Python, designed for professionals, researchers, and students. It provides high-performance tools for algebra, statistics, calculus, geometry, and financial engineering, with optional C++ acceleration for critical routines.

## Features
- Symbolic and numeric algebra
- Advanced statistics and probability
- Calculus: derivatives, integrals, optimization, ODE/PDE
- Geometry: analytic, solid, computational
- Financial engineering: derivatives pricing, risk, portfolio, XVA, ML
- Automatic fallback between C++ and pure Python
- Extensive documentation and practical examples
- Jupyter notebooks and benchmarks included

## Installation
```bash
pip install mathsolver-pro
```

## Quick Example
```python
from mathsolver_pro import algebra, statistics, calculus, geometry, financial

# Algebra: solve quadratic equation
roots = algebra.solve_quadratic(1, -3, 2)
print("Roots:", roots)

# Statistics: mean and standard deviation
mean = statistics.mean([1,2,3,4,5])
std = statistics.std([1,2,3,4,5])
print("Mean:", mean, "Std:", std)

# Calculus: symbolic derivative
import sympy as sp
x = sp.symbols('x')
deriv = calculus.derivative(x**2 + 2*x)
print("Derivative:", deriv)

# Geometry: area of triangle
area = geometry.triangle_area((0,0), (1,0), (0,1))
print("Triangle area:", area)

# Financial: Black-Scholes call price
call = financial.black_scholes_call(100, 100, 1, 0.05, 0.2)
print("Call price:", call)
```

## Documentation
- See the `docs/` folder or the online documentation for full API reference and tutorials.
- Example scripts are in `examples/`, Jupyter notebooks in `notebooks/`, and performance tests in `benchmarks/`.

## License
This project is licensed under the MIT License.
