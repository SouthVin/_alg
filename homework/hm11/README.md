i use gemini, https://share.gemini.google/rHw4cfUGsDqW

# Week 11 Assignment: Monte Carlo Method & Numerical Calculus

## AI Usage Declaration
**Yes, AI was used in this assignment.**  
AI assistance was utilized to help organize the Python implementation (`montecarlo.py`), verify mathematical formulas, structure the test cases, and draft this `README.md` documentation. All code has been executed, tested, and verified locally.

---

## Overview
This project implements numerical differentiation, Riemann integration, and Monte Carlo integration for both single-variable and $n$-variable functions in Python. It also demonstrates the **Curse of Dimensionality** by comparing grid-based Riemann integration against random Monte Carlo sampling across 1D, 2D, 5D, and 100D spaces.

### Implemented Tasks
1. **Single-Variable Numerical Differentiation & Integration**:
   - `diff_1d(f, x, h)`: Uses the central difference formula $\frac{f(x+h) - f(x-h)}{2h}$.
   - `integrate_1d_riemann(f, low, high, n)`: Uses the midpoint Riemann sum.
2. **Single-Variable Monte Carlo Integration**:
   - `integrate_1d_mc(f, low, high, samples)`: Estimates $\int_a^b f(x)\,dx \approx (b - a)\frac{1}{N}\sum_{i=1}^N f(x_i)$.
3. **Multivariable ($n$-D) Numerical Gradient & Hypervolume Integration**:
   - `grad_nd(f, x, h)`: Computes partial derivatives $\nabla f(\mathbf{x}) = \left[\frac{\partial f}{\partial x_1}, \dots, \frac{\partial f}{\partial x_n}\right]$.
   - `hypervolume_riemann(f, low, high, steps_per_dim)`: Recursively partitions an $n$-dimensional hyperrectangle into $k^n$ grid cells.
4. **Multivariable ($n$-D) Monte Carlo Integration**:
   - `hypervolume_mc(f, low, high, samples)`: Uniformly samples random points inside the $n$-dimensional hyperrectangle and scales the average function value by the domain's hypervolume. Tested by estimating the volume of a 3D unit sphere ($\frac{4}{3}\pi \approx 4.18879$).
5. **General $n$-D Riemann Integration (`integral(f, low, high)`)**:
   - Tested on $f(\mathbf{x}) = x_1^2 + x_2^2 + \dots + x_n^2$ over $[0, 1]^n$ for $n \in \{1, 2, 5, 100\}$.
6. **General $n$-D Monte Carlo Integration (`mc_integral(f, low, high)`)**:
   - Tested on the exact same function $f(\mathbf{x}) = \sum_{i=1}^n x_i^2$ over $[0, 1]^n$ for $n \in \{1, 2, 5, 100\}$.

---

## How to Run
No external libraries are required (uses Python's built-in `math`, `random`, and `time` modules):

```bash
python montecarlo.py