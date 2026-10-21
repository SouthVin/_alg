im using gemini, https://gemini.google.com/app/07c2b079e33e2833

# Week 7 Homework: Dynamic Programming vs Text Algorithms

## Problem Chosen
**1. diff : File difference comparison (Longest Common Subsequence - LCS)**

The Longest Common Subsequence (LCS) problem is a classic computer science problem used to find the longest subsequence present in two sequences in the same order. It is the basis for file comparison programs like `diff` and version control systems like `git`.

## Implementations

### 1. Non-Dynamic Programming (Naive Recursion)
*   **Principle:** The problem is broken down recursively. We compare the last characters of the two strings `X` and `Y`. If they match, the length increases by 1, and we recurse on the remaining strings. If they don't match, we branch into two recursive calls (one omitting the last character of `X`, the other omitting the last character of `Y`) and take the maximum result.
*   **Time Complexity:** $O(2^{m+n})$. In the worst case (where no characters match), the algorithm branches out exponentially, resulting in highly redundant calculations.
*   **Space Complexity:** $O(m+n)$. This is due to the maximum depth of the recursive call stack.

### 2. Dynamic Programming (Bottom-Up Tabulation)
*   **Principle:** Dynamic Programming solves the problem by breaking it into overlapping subproblems and storing the results of these subproblems in a 2D table (`L`) to avoid redundant calculations. `L[i][j]` stores the length of the LCS for the prefix of `X` of length `i` and the prefix of `Y` of length `j`.
*   **Time Complexity:** $O(m \times n)$. We use two nested loops to fill a table of size $(m+1) \times (n+1)$, where `m` and `n` are the lengths of the two strings.
*   **Space Complexity:** $O(m \times n)$. An auxiliary 2D array is created to store the states of the subproblems. *(Note: Space can be optimized to $O(\min(m,n))$ by storing only two rows, but the 2D matrix is standard for educational purposes).*

## Comparison Summary

| Feature | Non-Dynamic (Recursion) | Dynamic Programming |
| :--- | :--- | :--- |
| **Approach** | Top-down, splits into subproblems but recalculates overlapping ones. | Bottom-up, stores subproblem results to avoid recalculation. |
| **Time Complexity** | $O(2^{m+n})$ (Exponential - Very Slow) | $O(m \times n)$ (Polynomial - Fast) |
| **Space Complexity** | $O(m+n)$ (Call stack) | $O(m \times n)$ (2D Array Memory) |
| **Best Use Case** | Small strings (e.g., length < 15). | Large strings, files, or genomic sequences. |

When you run the provided `lcs_comparison.py` script, you will notice that the Dynamic Programming approach is significantly faster than the Recursive approach, and this speed gap will grow exponentially as the string length increases.