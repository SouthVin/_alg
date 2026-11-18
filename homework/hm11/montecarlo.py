"""
Week 11 Assignment: Monte Carlo Method & Numerical Calculus
Course: Introduction to Algorithms

AI Usage Declaration:
This program was written with the assistance of AI (used for structuring the
numerical/Monte Carlo functions, test cases, and documentation comments).
All algorithms and outputs have been reviewed and verified.
"""

import math
import random
import time

# Set a fixed random seed for reproducible test results
random.seed(42)


# ==============================================================================
# 1. Numerical Single-Variable Differentiation and Integration
# ==============================================================================
def diff_1d(f, x, h=1e-5):
    """Compute the numerical derivative f'(x) using the central difference method."""
    return (f(x + h) - f(x - h)) / (2.0 * h)


def integrate_1d_riemann(f, low, high, n=10000):
    """Compute the 1D definite integral of f over [low, high] via midpoint Riemann sum."""
    dx = (high - low) / n
    total = 0.0
    for i in range(n):
        mid = low + (i + 0.5) * dx
        total += f(mid) * dx
    return total


# ==============================================================================
# 2. Monte Carlo Single-Variable Integration
# ==============================================================================
def integrate_1d_mc(f, low, high, samples=100000):
    """Estimate the 1D definite integral of f over [low, high] using Monte Carlo sampling."""
    total = 0.0
    for _ in range(samples):
        x = random.uniform(low, high)
        total += f(x)
    return (high - low) * (total / samples)


# ==============================================================================
# 3. Numerical n-Variable Differentiation (Gradient) and Integration (Hypervolume)
# ==============================================================================
def grad_nd(f, x, h=1e-5):
    """Compute the numerical gradient vector of an n-variable function at point x."""
    grad = []
    for i in range(len(x)):
        x_plus = list(x)
        x_minus = list(x)
        x_plus[i] += h
        x_minus[i] -= h
        df_dxi = (f(x_plus) - f(x_minus)) / (2.0 * h)
        grad.append(df_dxi)
    return grad


def hypervolume_riemann(f, low, high, steps_per_dim=10, max_evals=1_000_000):
    """
    Compute the n-dimensional integral (hypervolume) of f over [low, high]
    using a midpoint Riemann sum.
    """
    n = len(low)
    if n != len(high):
        raise ValueError("low and high must have the same length.")

    total_points = steps_per_dim ** n
    if total_points > max_evals:
        raise OverflowError(
            f"Curse of Dimensionality: {steps_per_dim}^{n} = {total_points:.2e} "
            f"grid evaluations exceed the practical limit ({max_evals:,})."
        )

    dx = [(high[i] - low[i]) / steps_per_dim for i in range(n)]
    cell_volume = math.prod(dx)

    def recursive_sum(dim, current_x):
        if dim == n:
            return f(current_x)
        subtotal = 0.0
        for i in range(steps_per_dim):
            mid = low[dim] + (i + 0.5) * dx[dim]
            current_x.append(mid)
            subtotal += recursive_sum(dim + 1, current_x)
            current_x.pop()
        return subtotal

    return recursive_sum(0, []) * cell_volume


# ==============================================================================
# 4. Monte Carlo n-Variable Integration (Hypervolume)
# ==============================================================================
def hypervolume_mc(f, low, high, samples=100000):
    """
    Estimate the n-dimensional integral (hypervolume) of f over [low, high]
    using uniform Monte Carlo random sampling.
    """
    n = len(low)
    if n != len(high):
        raise ValueError("low and high must have the same length.")

    domain_volume = math.prod(high[i] - low[i] for i in range(n))
    total = 0.0
    for _ in range(samples):
        x = [random.uniform(low[i], high[i]) for i in range(n)]
        total += f(x)
    return domain_volume * (total / samples)


# ==============================================================================
# 5. n-Variable Riemann Integral Function: integral(f, low, high)
# ==============================================================================
def integral(f, low, high, steps_per_dim=10):
    """
    General n-variable Riemann integration function where n = len(low) = len(high).
    """
    return hypervolume_riemann(f, low, high, steps_per_dim=steps_per_dim)


# ==============================================================================
# 6. n-Variable Monte Carlo Integral Function: mc_integral(f, low, high)
# ==============================================================================
def mc_integral(f, low, high, samples=100000):
    """
    General n-variable Monte Carlo integration function where n = len(low) = len(high).
    """
    return hypervolume_mc(f, low, high, samples=samples)


def sum_of_squares(x):
    """Test function f(x) = x_1^2 + x_2^2 + ... + x_n^2."""
    return sum(xi ** 2 for xi in x)


# ==============================================================================
# Test Examples
# ==============================================================================
if __name__ == "__main__":
    print("=== 1. Single-Variable Numerical Differentiation & Integration ===")
    f1 = lambda x: x ** 2
    print(f"f(x) = x^2 at x = 3 | Numerical diff = {diff_1d(f1, 3):.6f} (Exact = 6.000000)")
    print(f"Integral of x^2 on [0, 1] | Riemann = {integrate_1d_riemann(f1, 0, 1):.6f} (Exact = {1/3:.6f})")

    print("\n=== 2. Single-Variable Monte Carlo Integration ===")
    print(f"Integral of x^2 on [0, 1] | Monte Carlo = {integrate_1d_mc(f1, 0, 1, 100000):.6f} (Exact = {1/3:.6f})")

    print("\n=== 3. n-Variable Numerical Differentiation (Gradient) & Integration ===")
    f_3d = lambda x: x[0]**2 + 2 * (x[1]**2) + 3 * (x[2]**2)
    point = [1.0, 2.0, 3.0]
    grad = [round(g, 6) for g in grad_nd(f_3d, point)]
    print(f"Gradient of x1^2 + 2*x2^2 + 3*x3^2 at [1, 2, 3] = {grad} (Exact = [2.0, 8.0, 18.0])")
    vol_3d = hypervolume_riemann(f_3d, [0, 0, 0], [1, 1, 1], steps_per_dim=20)
    print(f"3D Integral on [0, 1]^3 (Riemann) = {vol_3d:.6f} (Exact = 2.000000)")

    print("\n=== 4. n-Variable Monte Carlo Integration (Hypervolume) ===")
    # Estimate the volume of a 3D unit sphere: x^2 + y^2 + z^2 <= 1 inside [-1, 1]^3
    unit_sphere = lambda x: 1.0 if sum(xi ** 2 for xi in x) <= 1.0 else 0.0
    sphere_vol = hypervolume_mc(unit_sphere, [-1, -1, -1], [1, 1, 1], samples=200000)
    print(f"3D Unit Sphere Hypervolume (Monte Carlo) = {sphere_vol:.6f} (Exact = {4/3 * math.pi:.6f})")

    print("\n=== 5. n-Variable Riemann Integration: integral(f, low, high) ===")
    print("Test function: f(x) = x_1^2 + ... + x_n^2 on [0, 1]^n")
    for dim in [1, 2, 5, 100]:
        low = [0.0] * dim
        high = [1.0] * dim
        exact = dim / 3.0
        t0 = time.perf_counter()
        try:
            steps = 100 if dim <= 2 else 10
            res = integral(sum_of_squares, low, high, steps_per_dim=steps)
            dt = time.perf_counter() - t0
            print(f"Dim = {dim:3d} | Steps/dim = {steps:3d} | Result = {res:.6f} | Exact = {exact:.6f} | Time = {dt:.4f}s")
        except OverflowError as err:
            print(f"Dim = {dim:3d} | Failed -> {err}")

    print("\n=== 6. n-Variable Monte Carlo Integration: mc_integral(f, low, high) ===")
    print("Test function: f(x) = x_1^2 + ... + x_n^2 on [0, 1]^n")
    for dim in [1, 2, 5, 100]:
        low = [0.0] * dim
        high = [1.0] * dim
        exact = dim / 3.0
        t0 = time.perf_counter()
        res = mc_integral(sum_of_squares, low, high, samples=100000)
        dt = time.perf_counter() - t0
        print(f"Dim = {dim:3d} | Samples = 100,000 | Result = {res:.6f} | Exact = {exact:.6f} | Time = {dt:.4f}s")