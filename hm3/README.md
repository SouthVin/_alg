im use gemini, https://share.gemini.google/kqa4Jhq3oPrK

```markdown
# Homework 3: Boolean Satisfiability (SAT) Problem Solver

This repository contains a Python implementation of a systematic truth table generator designed to solve the **Boolean Satisfiability (SAT) Problem** using an **Exhaustive Search (Brute Force)** approach.

---

## 📌 Problem Overview

The **Boolean Satisfiability Problem (SAT)** is the problem of determining if there exists an interpretation (assignment of `True` and `False` values to variables) that satisfies a given Boolean formula. In other words, it checks whether a formula can evaluate to `True`.

SAT was the first problem proven to be **NP-complete** (Cook–Levin theorem).

---

## 💡 Algorithm & Implementation

The approach used in this homework generates a full truth table systematically:
1. **Variable Mapping**: Extracts $n$ Boolean variables present in the logical expression.
2. **Truth Value Combination Generation**: Generates all $2^n$ possible binary combinations of truth assignments using `itertools.product`.
3. **Evaluation**: Evaluates the Boolean expression for each assignment row using Python's `eval()` function in a scoped environment.
4. **Satisfiability Check**:
   - **SATISFIABLE**: If at least one assignment yields `True`.
   - **UNSATISFIABLE**: If all $2^n$ combinations yield `False`.

---

## ⏱️ Time & Space Complexity

| Metric | Complexity | Explanation |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(2^n \cdot k)$ | Requires evaluating $2^n$ total truth combinations for $n$ variables, where $k$ is the length of the expression. |
| **Space Complexity** | $\mathcal{O}(2^n + n)$ | Stores the generated truth combinations in memory. |

---

## 🚀 How to Run

### Prerequisites
- Python 3.x installed on your machine.

### Execution
1. Clone this repository or download `sat_solver.py`.
2. Run the script using terminal/command prompt:
   ```bash
   python sat_solver.py

```

---

## 📊 Sample Output

```text
Test Case 1:
Ekspresi: (A or B) and (not C)
----------------
A | B | C | Result
----------------
0 | 0 | 0 | 0
0 | 0 | 1 | 0
0 | 1 | 0 | 1
0 | 1 | 1 | 0
1 | 0 | 0 | 1
1 | 0 | 1 | 0
1 | 1 | 0 | 1
1 | 1 | 1 | 0
----------------

Status: SATISFIABLE
Kombinasi yang bernilai True:
{'A': False, 'B': True, 'C': False}
{'A': True, 'B': False, 'C': False}
{'A': True, 'B': True, 'C': False}

```

```

```