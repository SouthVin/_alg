im use gemini, https://share.gemini.google/Wsz2ecOZdGZz

# Homework 2: Recurrence Relations and Time Complexity Analysis

This repository contains step-by-step mathematical derivations, exact formulas, Big-O time complexity analysis, and Python verification code for the recurrence relations assigned in **Introduction to Algorithms (HW2)**.

---

## 📋 Overview of Solutions

| Recurrence Relation | Base Condition | Exact Formula $T(n)$ | Time Complexity $O(\cdot)$ |
| :--- | :--- | :--- | :--- |
| **1.** $T(n) = T(n-1) + 8$ | $T(1) = 1$ | $T(n) = 8n - 7$ | $O(n)$ |
| **2.** $T(n) = 2T(n-1) + 9$ | $T(1) = 1$ | $T(n) = 5 \cdot 2^n - 9$ | $O(2^n)$ |
| **3.** $T(n) = 2T(n/2) + 1$ | $T(1) = 1$ | $T(n) = 2n - 1$ | $O(n)$ |
| **4.** $T(n) = T(n/2) + 1$ | $T(1) = 1$ | $T(n) = \log_2 n + 1$ | $O(\log n)$ |

---

## 📐 Detailed Mathematical Derivations

### Problem 1: $T(n) = T(n-1) + 8, \quad T(1) = 1$

#### Substitution / Expansion:
$$\begin{aligned} T(n) &= T(n-1) + 8 \\ &= (T(n-2) + 8) + 8 = T(n-2) + 2(8) \\ &= (T(n-3) + 8) + 2(8) = T(n-3) + 3(8) \\ &\;\;\vdots \\ &= T(n-k) + k \cdot 8 \end{aligned}$$

#### Applying Base Case:
Set $n - k = 1 \implies k = n - 1$:
$$\begin{aligned} T(n) &= T(1) + 8(n - 1) \\ &= 1 + 8n - 8 \\ &= 8n - 7 \end{aligned}$$

* **Exact Closed-Form Result:** $T(n) = 8n - 7$
* **Big-O Complexity:** $O(n)$

---

### Problem 2: $T(n) = 2T(n-1) + 9, \quad T(1) = 1$

#### Substitution / Expansion:
$$\begin{aligned} T(n) &= 2 T(n-1) + 9 \\ &= 2(2 T(n-2) + 9) + 9 = 2^2 T(n-2) + 2 \cdot 9 + 9 \\ &= 2^2(2 T(n-3) + 9) + 2 \cdot 9 + 9 = 2^3 T(n-3) + 2^2 \cdot 9 + 2 \cdot 9 + 9 \\ &\;\;\vdots \\ &= 2^k T(n-k) + 9 \sum_{i=0}^{k-1} 2^i \end{aligned}$$

#### Applying Base Case:
Set $n - k = 1 \implies k = n - 1$:
$$T(n) = 2^{n-1} T(1) + 9 \sum_{i=0}^{n-2} 2^i$$

Using the geometric series summation formula $\sum_{i=0}^{m} 2^i = 2^{m+1} - 1$:
$$\begin{aligned} T(n) &= 2^{n-1}(1) + 9(2^{n-1} - 1) \\ &= 2^{n-1} + 9 \cdot 2^{n-1} - 9 \\ &= 10 \cdot 2^{n-1} - 9 \\ &= 5 \cdot 2^n - 9 \end{aligned}$$

* **Exact Closed-Form Result:** $T(n) = 5 \cdot 2^n - 9$ (or $10 \cdot 2^{n-1} - 9$)
* **Big-O Complexity:** $O(2^n)$

---

### Problem 3: $T(n) = 2T(n/2) + 1, \quad T(1) = 1$

*(Assume $n = 2^k$ for integer decomposition)*

#### Substitution / Expansion:
$$\begin{aligned} T(n) &= 2 T(n/2) + 1 \\ &= 2(2 T(n/4) + 1) + 1 = 4 T(n/4) + 2 + 1 \\ &= 4(2 T(n/8) + 1) + 2 + 1 = 8 T(n/8) + 4 + 2 + 1 \\ &\;\;\vdots \\ &= 2^k T\left(\frac{n}{2^k}\right) + \sum_{i=0}^{k-1} 2^i \end{aligned}$$

#### Applying Base Case:
Set $\frac{n}{2^k} = 1 \implies k = \log_2 n$:
$$\begin{aligned} T(n) &= 2^{\log_2 n} T(1) + \sum_{i=0}^{\log_2 n - 1} 2^i \\ &= n \cdot (1) + (2^{\log_2 n} - 1) \\ &= n + n - 1 \\ &= 2n - 1 \end{aligned}$$

* **Exact Closed-Form Result:** $T(n) = 2n - 1$
* **Big-O Complexity:** $O(n)$

---

### Problem 4: $T(n) = T(n/2) + 1, \quad T(1) = 1$

*(Assume $n = 2^k$ for integer decomposition)*

#### Substitution / Expansion:
$$\begin{aligned} T(n) &= T(n/2) + 1 \\ &= (T(n/4) + 1) + 1 = T(n/4) + 2 \\ &= (T(n/8) + 1) + 2 = T(n/8) + 3 \\ &\;\;\vdots \\ &= T\left(\frac{n}{2^k}\right) + k \end{aligned}$$

#### Applying Base Case:
Set $\frac{n}{2^k} = 1 \implies k = \log_2 n$:
$$\begin{aligned} T(n) &= T(1) + \log_2 n \\ &= 1 + \log_2 n \end{aligned}$$

* **Exact Closed-Form Result:** $T(n) = \log_2 n + 1$
* **Big-O Complexity:** $O(\log n)$

---

## 🐍 Python Verification Script

Below is the Python implementation verifying both the recursive definitions and exact mathematical closed-form equations:

```python
import math

# 1. T(n) = T(n-1) + 8, T(1) = 1
def T1_recursive(n):
    if n <= 1:
        return 1
    return T1_recursive(n - 1) + 8

def T1_exact(n):
    return 8 * n - 7

# 2. T(n) = 2*T(n-1) + 9, T(1) = 1
def T2_recursive(n):
    if n <= 1:
        return 1
    return 2 * T2_recursive(n - 1) + 9

def T2_exact(n):
    return 5 * (2 ** n) - 9

# 3. T(n) = 2*T(n/2) + 1, T(1) = 1
def T3_recursive(n):
    if n <= 1:
        return 1
    return 2 * T3_recursive(n // 2) + 1

def T3_exact(n):
    return 2 * n - 1

# 4. T(n) = T(n/2) + 1, T(1) = 1
def T4_recursive(n):
    if n <= 1:
        return 1
    return T4_recursive(n // 2) + 1

def T4_exact(n):
    return int(math.log2(n)) + 1

if __name__ == "__main__":
    print("=== Recurrence Verification ===")
    
    n_val = 5
    print(f"T1({n_val}): Recursive = {T1_recursive(n_val)}, Exact = {T1_exact(n_val)}")
    print(f"T2({n_val}): Recursive = {T2_recursive(n_val)}, Exact = {T2_exact(n_val)}")
    
    n_pow2 = 16
    print(f"T3({n_pow2}): Recursive = {T3_recursive(n_pow2)}, Exact = {T3_exact(n_pow2)}")
    print(f"T4({n_pow2}): Recursive = {T4_recursive(n_pow2)}, Exact = {T4_exact(n_pow2)}")