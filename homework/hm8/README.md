using gemini, https://share.gemini.google/bPPl8370eSHp

# Traveling Salesperson Problem (TSP) — Code Architecture & Algorithm Mechanics

This repository contains Python implementations and explanations of **5 optimization algorithms** used to solve the **Traveling Salesperson Problem (TSP)** for the *Introduction to Algorithms* Week 7 assignment.

---

## 📌 Problem Overview

The **Traveling Salesperson Problem (TSP)** seeks the shortest closed tour that visits a set of $N$ cities exactly once and returns to the starting city.

Given city coordinates $C = \{(x_1, y_1), (x_2, y_2), \dots, (x_N, y_N)\}$, the distance between city $i$ and city $j$ is calculated using Euclidean distance:

$$d(i, j) = \sqrt{(x_i - x_j)^2 + (y_i - y_j)^2}$$

---

## 🛠️ Code Architecture & Structural Mechanics

The codebase inside `tsp_solver.py` is organized into modular sections:

### 1. Data Preparation & Distance Matrix
- **City Representation**: Coordinates are stored in a dictionary `CITIES` mapping city names to $(x, y)$ coordinate tuples.
- **Precomputed Distance Matrix (`DIST_MATRIX`)**: A symmetric $N \times N$ matrix precalculates all pairwise Euclidean distances. This eliminates repetitive distance calculations during optimization loops and improves overall speed.

### 2. Core Helper Functions
- `get_tour_distance(path)`: Sums Euclidean distances along the sequence array `path` and uses modulo indexing `(i + 1) % len(path)` to close the loop from the final city back to the starting city.
- `format_path(path)`: Maps numeric indices back to human-readable city labels (e.g., `[0, 6, 2]` $\rightarrow$ `A -> G -> C -> A`).

---

## 🔬 Algorithm Explanations & How They Work

### 1. Improvement Method (2-Opt Local Search)
- **Function**: `improvement_tsp()`
- **Mechanism**: Evaluates subsegments $[i, j]$ within the path sequence and reverses them via array slicing (`path[i:j+1][::-1]`).
- **Logic**: Inverting a subsegment uncrosses intersecting path edges. If reversing a subsegment yields a strictly shorter total distance, the path updates immediately. The loop continues until no further 2-edge reversal produces an improvement.

### 2. Hill Climbing Algorithm
- **Function**: `hill_climbing_tsp(max_iterations=1000)`
- **Mechanism**: Generates candidate moves by swapping two random cities (`path[i], path[j] = path[j], path[i]`).
- **Logic**: Evaluates the candidate route against the current route. If the new path distance is strictly shorter, it accepts the swap; otherwise, it discards the change and continues iterating.

### 3. Simulated Annealing
- **Function**: `simulated_annealing_tsp(initial_temp=1000.0, cooling_rate=0.995, max_iterations=2000)`
- **Mechanism**: Combines 2-opt subsegment swaps with a Metropolis temperature decay process.
- **Logic**: 
  - Always accepts shorter routes ($\Delta < 0$).
  - Accepts worse routes ($\Delta \ge 0$) with probability $P = \exp(-\Delta / T)$.
  - High initial temperatures ($T$) allow global exploration to escape local minima. As temperature cools down ($T \to 0$), the search transitions to strict local optimization.

### 4. Gradient Descent (Continuous Relaxation)
- **Function**: `gradient_descent_tsp(learning_rate=0.05, max_iterations=1000)`
- **Mechanism**: Maps discrete city sequences into continuous weight vectors $x \in \mathbb{R}^N$, where ordering is determined via `np.argsort(x)`.
- **Logic**: Since discrete permutations lack analytical gradients, partial derivatives are estimated numerically using finite differences $\frac{\text{loss}(x + \epsilon) - \text{loss}(x)}{\epsilon}$. Priority weights update opposite to the gradient vector with slight stochastic noise.

### 5. Greedy Algorithm (Nearest Neighbor)
- **Function**: `greedy_tsp(start_node=0)`
- **Mechanism**: Constructive strategy that maintains an `unvisited` set of cities.
- **Logic**: Starting from `start_node`, it selects the closest unvisited city at each step using `min(unvisited, key=...)` until all cities are visited, then appends the return path to the origin.

---

## 🔗 Assignment References

- [Course Reference Repository (ccc115a/alg)](https://github.com/ccc115a/alg/tree/main/_more/homework/week7-tsp)
- [Homework Baseline Reference](https://github.com/zerorezerorezero/alg/tree/778f0933b4e53393608043259cefb4b1ffa09a06/homework/week8)