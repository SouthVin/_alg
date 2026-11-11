import heapq
from collections import deque

# ==========================================
# 1. Rat in a Maze Problem (DFS)
# ==========================================
def solve_maze_dfs(maze):
    """
    0: Open path
    1: Wall / Obstacle
    """
    rows, cols = len(maze), len(maze[0])
    start, end = (0, 0), (rows - 1, cols - 1)
    path = []
    visited = set()

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False
        if maze[r][c] == 1 or (r, c) in visited:
            return False

        visited.add((r, c))
        path.append((r, c))

        if (r, c) == end:
            return True

        # Move in 4 directions: Up, Down, Left, Right
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if dfs(r + dr, c + dc):
                return True

        path.pop()  # Backtrack
        return False

    if dfs(0, 0):
        return path
    return None


# ==========================================
# 2. Wolf, Sheep, Cabbage River Crossing (BFS)
# ==========================================
def is_valid_river_state(state):
    farmer, wolf, sheep, cabbage = state
    # Wolf eats sheep if farmer is absent
    if wolf == sheep and farmer != wolf:
        return False
    # Sheep eats cabbage if farmer is absent
    if sheep == cabbage and farmer != sheep:
        return False
    return True

def solve_river_crossing_bfs():
    # State: (Farmer, Wolf, Sheep, Cabbage), 0 = Left bank, 1 = Right bank
    start = (0, 0, 0, 0)
    target = (1, 1, 1, 1)

    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        curr, path = queue.popleft()
        if curr == target:
            return path

        f, w, s, c = curr
        nf = 1 - f  # Farmer switches side

        # Possible items the farmer can bring: alone, wolf, sheep, or cabbage
        possible_moves = [(nf, w, s, c)]
        if f == w:
            possible_moves.append((nf, nf, s, c))
        if f == s:
            possible_moves.append((nf, w, nf, c))
        if f == c:
            possible_moves.append((nf, w, s, nf))

        for next_state in possible_moves:
            if is_valid_river_state(next_state) and next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [next_state]))

    return None


# ==========================================
# 3. Eight Queens Problem (DFS)
# ==========================================
def solve_eight_queens_dfs():
    solutions = []

    def is_safe(board, row, col):
        for r in range(row):
            c = board[r]
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True

    def dfs(row, board):
        if row == 8:
            solutions.append(list(board))
            return

        for col in range(8):
            if is_safe(board, row, col):
                board.append(col)
                dfs(row + 1, board)
                board.pop()

    dfs(0, [])
    return solutions


# ==========================================
# 4. NPC Finding Player Problem (A* Search)
# ==========================================
def solve_npc_a_star(grid, start, goal):
    rows, cols = len(grid), len(grid[0])

    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Manhattan Distance

    # Min-Heap Priority Queue: (f_score, g_score, current_node, path)
    open_set = [(heuristic(start, goal), 0, start, [start])]
    visited = {}

    while open_set:
        f, g, curr, path = heapq.heappop(open_set)

        if curr in visited and visited[curr] <= g:
            continue
        visited[curr] = g

        if curr == goal:
            return path

        r, c = curr
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                neighbor = (nr, nc)
                new_g = g + 1
                if neighbor not in visited or new_g < visited[neighbor]:
                    new_f = new_g + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (new_f, new_g, neighbor, path + [neighbor]))

    return None


# ==========================================
# 5. IC Design Circuit Routing (Lee's Algorithm / BFS)
# ==========================================
def solve_ic_routing_lee(grid, pin_a, pin_b):
    rows, cols = len(grid), len(grid[0])
    queue = deque([pin_a])
    parent = {pin_a: None}

    while queue:
        curr = queue.popleft()
        if curr == pin_b:
            break

        r, c = curr
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == 0 and (nr, nc) not in parent:
                    parent[(nr, nc)] = (r, c)
                    queue.append((nr, nc))

    if pin_b not in parent:
        return None

    # Reconstruct path from pin_b back to pin_a
    curr = pin_b
    path = []
    while curr:
        path.append(curr)
        curr = parent[curr]
    return path[::-1]


# ==========================================
# Execution / Testing
# ==========================================
if __name__ == "__main__":
    print("=== 1. Rat in a Maze (DFS) ===")
    maze_map = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0]
    ]
    print("Path found:", solve_maze_dfs(maze_map))

    print("\n=== 2. Wolf, Sheep, Cabbage River Crossing (BFS) ===")
    river_path = solve_river_crossing_bfs()
    print("Total steps:", len(river_path) - 1)
    for step, state in enumerate(river_path):
        print(f"Step {step}: (Farmer, Wolf, Sheep, Cabbage) = {state}")

    print("\n=== 3. Eight Queens Problem (DFS) ===")
    queens_solutions = solve_eight_queens_dfs()
    print("Total solutions found:", len(queens_solutions))
    print("Sample solution 1:", queens_solutions[0])

    print("\n=== 4. NPC Finding Player (A* Algorithm) ===")
    game_grid = [
        [0, 0, 0, 0, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    npc_start, player_pos = (0, 0), (4, 4)
    print("A* Path:", solve_npc_a_star(game_grid, npc_start, player_pos))

    print("\n=== 5. IC Circuit Routing (Lee's Algorithm / BFS) ===")
    chip_grid = [
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    pin1, pin2 = (0, 0), (0, 4)
    print("Routing Path:", solve_ic_routing_lee(chip_grid, pin1, pin2))