import time
import sys

# Increase recursion depth limit for safety if testing larger n values
sys.setrecursionlimit(2000)


def power2n_1(n: int) -> int:
    """Method 1: Built-in exponentiation operator.

    Time Complexity: O(1) / hardware-level multiplication
    Space Complexity: O(1)
    """
    return 2 ** n


def power2n_2a(n: int) -> int:
    """Method 2a: Naive Recursive method (binary tree recursive calls).

    Time Complexity: O(2^n)
    Space Complexity: O(n) call stack
    """
    if n == 0:
        return 1
    return power2n_2a(n - 1) + power2n_2a(n - 1)


def power2n_2b(n: int) -> int:
    """Method 2b: Linear Recursive method (single recursive call per level).

    Time Complexity: O(n)
    Space Complexity: O(n) call stack
    """
    if n == 0:
        return 1
    return 2 * power2n_2b(n - 1)


def power2n_3(n: int, memo: dict = None) -> int:
    """Method 3: Recursive with Memoization (Lookup Table / Dynamic Programming).

    Time Complexity: O(n)
    Space Complexity: O(n) for memo table + call stack
    """
    if memo is None:
        memo = {}
    
    if n == 0:
        return 1
    if n in memo:
        return memo[n]
    
    memo[n] = power2n_3(n - 1, memo) + power2n_3(n - 1, memo)
    return memo[n]


def run_benchmark(n_values: list):
    """Runs performance benchmarks across all methods for various values of n."""
    print("=" * 75)
    print(f"{'n':<6} | {'Method 1 (2**n)':<15} | {'Method 2a (2a)':<15} | {'Method 2b (2b)':<15} | {'Method 3 (Memo)':<15}")
    print("=" * 75)

    for n in n_values:
        times = {}

        # Test Method 1
        start = time.perf_counter()
        res1 = power2n_1(n)
        times['m1'] = time.perf_counter() - start

        # Test Method 2a (Skip for n > 28 to prevent execution freeze)
        if n <= 28:
            start = time.perf_counter()
            res2a = power2n_2a(n)
            times['m2a'] = f"{time.perf_counter() - start:.6f}s"
            assert res1 == res2a, "Method 2a result mismatch!"
        else:
            times['m2a'] = "TIMEOUT/HANG"

        # Test Method 2b
        start = time.perf_counter()
        res2b = power2n_2b(n)
        times['m2b'] = time.perf_counter() - start
        assert res1 == res2b, "Method 2b result mismatch!"

        # Test Method 3
        start = time.perf_counter()
        res3 = power2n_3(n)
        times['m3'] = time.perf_counter() - start
        assert res1 == res3, "Method 3 result mismatch!"

        # Print benchmark row
        m1_str = f"{times['m1']:.6f}s"
        m2b_str = f"{times['m2b']:.6f}s"
        m3_str = f"{times['m3']:.6f}s"
        print(f"{n:<6} | {m1_str:<15} | {times['m2a']:<15} | {m2b_str:<15} | {m3_str:<15}")

    print("=" * 75)


def main():
    print("--- Algorithm Analysis Homework: Computing 2^n ---\n")
    
    # Run comparative benchmark across small and large values
    test_n = [10, 20, 25, 28, 100]
    run_benchmark(test_n)

    print("\n--- Detailed Result for n = 100 ---")
    n = 100
    print(f"Calculated 2^100:")
    print(f"Value = {power2n_1(n)}")
    print("\nNote on Method 2a for n = 100:")
    print("Method 2a has exponential time complexity O(2^n). For n = 100, it requires approximately")
    print("2^100 (~1.26 x 10^30) operations, which would take billions of years to complete on modern hardware.")


if __name__ == "__main__":
    main()