im using gemini, 

# Week 9 Assignment: Search Algorithms

This repository contains Python implementations and detailed explanations for the Week 9 search algorithm assignment in the Introduction to Algorithms course. It covers Depth-First Search (DFS), Breadth-First Search (BFS), A* Heuristic Search, and Lee's Circuit Routing Algorithm.

---

## Problems & Algorithm Descriptions

### 1. Rat in a Maze Problem
* **Algorithm**: Depth-First Search (DFS)
* **How it works**:
  * The maze is represented as a 2D grid where `0` denotes walkable paths and `1` denotes walls.
  * DFS starts from `(0, 0)` and explores as deep as possible along each branch before backtracking.
  * A visited set tracks explored cells. When encountering a dead end or wall, backtracking reverts to the previous decision point until the destination `(N-1, M-1)` is reached.

---

### 2. Wolf, Sheep, Cabbage River Crossing Problem
* **Algorithm**: Breadth-First Search (BFS)
* **How it works**:
  * State is represented by a 4-tuple `(Farmer, Wolf, Sheep, Cabbage)` where `0` indicates the left bank and `1` indicates the right bank.
  * Invalid state constraints:
    * Wolf and sheep cannot be left alone without the farmer.
    * Sheep and cabbage cannot be left alone without the farmer.
  * BFS expands all valid state transitions level by level, guaranteeing the discovery of the shortest path (minimum steps) to bring all items safely to the target state `(1, 1, 1, 1)`.

---

### 3. Eight Queens Problem
* **Algorithm**: DFS with Backtracking
* **How it works**:
  * Places 8 queens on an $8 \times 8$ chessboard such that no two queens attack each other (sharing the same row, column, or diagonal).
  * The algorithm attempts to place a queen row by row, checking safety conditions via `is_safe()`.
  * If a valid column is found, it recursively moves to the next row; if no valid column exists, it backtracks and undoes the last step. It returns all **92 distinct solutions**.

---

### 4. NPC Pathfinding to Player
* **Algorithm**: A* Search Algorithm
* **How it works**:
  * The NPC navigates around obstacles to locate the player's position using the cost function:
    $$f(n) = g(n) + h(n)$$
    * $g(n)$: Exact movement cost from the start node to current node $n$.
    * $h(n)$: Estimated heuristic cost from $n$ to the player position (calculated using Manhattan Distance: $|x_1 - x_2| + |y_1 - y_2|$).
  * A min-heap priority queue expands nodes with the lowest $f(n)$ value first, achieving optimal pathfinding efficiency in grid-based game environments.

---

### 5. IC Design Circuit Routing Problem
* **Algorithm**: Lee's Algorithm (Maze Routing / BFS)
* **How it works**:
  * Connects two terminal pins (Pin A and Pin B) on an integrated circuit (IC) grid while avoiding obstacles and existing wire traces.
  * Lee's algorithm utilizes BFS wavefront expansion from Pin A to guarantee finding the shortest wiring route.
  * Once the wavefront reaches Pin B, the path is reconstructed by backtracking along decrementing distance step markers to Pin A.

---

## Execution Instructions

1. Ensure Python 3.x is installed on your system.
2. Run the main script in your terminal:
```bash
python main.py