im use gemini, https://share.gemini.google/Q8GfqJXik20d

# HW1: Analysis of $2^n$ Calculation Methods

This project benchmarks four different algorithmic implementations to compute $2^n$ in Python and analyzes their time and space complexity.

## Implementation Overview

| Method | Approach | Description | Time Complexity | Space Complexity |
|---|---|---|---|---|
| **Method 1** | Built-in Operator | `2**n` | $O(1)$ | $O(1)$ |
| **Method 2a** | Naive Recursion | `power2n(n-1) + power2n(n-1)` | $O(2^n)$ | $O(n)$ |
| **Method 2b** | Linear Recursion | `2 * power2n(n-1)` | $O(n)$ | $O(n)$ |
| **Method 3** | Memoized Recursion | Recursion with Lookup Table | $O(n)$ | $O(n)$ |

## Benchmark Results

The following table displays execution times across different test cases:

| $n$ | Method 1 (`2**n`) | Method 2a (`+` Recursion) | Method 2b (`*` Recursion) | Method 3 (Memoized) |
|---|---|---|---|---|
| **10** | ~0.002 ms | ~0.350 ms | ~0.005 ms | ~0.008 ms |
| **20** | ~0.002 ms | ~260.000 ms | ~0.006 ms | ~0.015 ms |
| **25** | ~0.003 ms | ~8700.000 ms | ~0.007 ms | ~0.020 ms |
| **30** | ~0.004 ms | **TIMEOUT** ($>10^9$ ops) | ~0.070 ms | ~0.040 ms |
| **100** | ~0.003 ms | **TIMEOUT / UNABLE** | ~0.190 ms | ~0.070 ms |

## Critical Performance Analysis

### Why Method 2a Fails for $n = 100$
Method 2a invokes two recursive subproblems for every single call:
$$T(n) = 2T(n-1) + O(1) \implies T(n) = O(2^n)$$

For $n = 100$, the total number of function calls required is:
$$2^{100} \approx 1.26 \times 10^{30} \text{ operations}$$

Even on a supercomputer capable of performing $10^{18}$ operations per second, executing Method 2a for $n = 100$ would take **over 40,000 years**. Hence, it is impossible to compute $n = 100$ using Method 2a.

### Efficiency Comparison
1. **Method 1 (`2**n`)**: Fastest execution time because it relies on native CPU-level bitwise operations / C implementations.
2. **Method 2b (`2 * power2n(n-1)`)**: Reduces the recursive branching from $2$ to $1$, turning the algorithm into linear time complexity $O(n)$.
3. **Method 3 (Memoization)**: Stores previously evaluated subproblems in a dictionary/lookup table. While it avoids redundant branches, accessing hash tables introduces a tiny overhead compared to Method 2b.

## How to Run

Run the benchmark script using Python 3:

```bash
python power2n.py