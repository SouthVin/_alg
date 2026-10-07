im use gemini,https://share.gemini.google/sD4Bmu9LPtVU

# Week 5 Homework: Recursion, Functional Programming, Lambda Calculus

This repository contains solutions for the Week 5 Introduction to Algorithms assignment. The primary focus of this week is utilizing Recursion, Functional Programming, and Lambda Calculus concepts to solve computational problems.

## 1. Tower of Hanoi (`hanoi.py`)
This script solves the classic Tower of Hanoi problem using two distinct approaches:
* **Recursive Method:** A standard mathematical recursion representing `T(n) = 2*T(n-1) + 1`.
* **Iterative Method (No Recursion):** A loop-based approach that utilizes a Stack to simulate the call stack memory, explicitly forbidding recursive function calls.

## 2. Symbolic Differentiation (`sym_diff.py`)
This script implements a function `sym_diff(expr)` to perform symbolic differentiation using pure recursion. 
* Mathematical expressions are represented as nested abstract syntax trees using tuples (e.g., `('+', 'x', ('*', 2, 'x'))`).
* The function evaluates derivation rules (Constant, Addition, Subtraction, Product) recursively to generate the derivative expression.

## 3. Functional Bubble Sort (`functional_sort.py`)
This script solves the Bubble Sort problem strictly using functional programming paradigms.
* **Constraints Met:** **No `for` or `while` loops are used in the entire script.**
* Implemented custom `my_map`, `my_filter`, and `my_reduce` functions using pure recursion.
* The Bubble Sort logic is executed by utilizing `my_reduce` to perform a single adjacent-swapping pass (`bubble_pass`), and then standard recursion is applied to fully sort the remaining unsorted elements.

## How to Run
Ensure you have Python 3 installed. You can run each file directly from the terminal:
```bash
python hanoi.py
python sym_diff.py
python functional_sort.py