import math

# 1. T(n) = T(n-1) + 8, T(1) = 1  => O(n)
def T1_recursive(n):
    if n == 1:
        return 1
    return T1_recursive(n - 1) + 8

def T1_exact(n):
    return 8 * n - 7


# 2. T(n) = 2*T(n-1) + 9, T(1) = 1  => O(2^n)
def T2_recursive(n):
    if n == 1:
        return 1
    return 2 * T2_recursive(n - 1) + 9

def T2_exact(n):
    return 5 * (2 ** n) - 9


# 3. T(n) = 2*T(n/2) + 1, T(1) = 1  => O(n)
def T3_recursive(n):
    if n <= 1:
        return 1
    return 2 * T3_recursive(n // 2) + 1

def T3_exact(n):
    return 2 * n - 1


# 4. T(n) = T(n/2) + 1, T(1) = 1  => O(log n)
def T4_recursive(n):
    if n <= 1:
        return 1
    return T4_recursive(n // 2) + 1

def T4_exact(n):
    return int(math.log2(n)) + 1


# Test unit untuk membandingkan hasil rekursif vs rumus eksak
if __name__ == "__main__":
    print("=== Testing Recurrences ===")
    
    # Test 1 & 2 dengan n = 5
    n_linear = 5
    print(f"T1({n_linear}): Recursive = {T1_recursive(n_linear)}, Exact = {T1_exact(n_linear)}")
    print(f"T2({n_linear}): Recursive = {T2_recursive(n_linear)}, Exact = {T2_exact(n_linear)}")
    
    # Test 3 & 4 dengan n = 16 (pangkat 2)
    n_pow2 = 16
    print(f"T3({n_pow2}): Recursive = {T3_recursive(n_pow2)}, Exact = {T3_exact(n_pow2)}")
    print(f"T4({n_pow2}): Recursive = {T4_recursive(n_pow2)}, Exact = {T4_exact(n_pow2)}")