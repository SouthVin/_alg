import numpy as np
import random
import math

# Sample 2D City Coordinates
CITIES = {
    'A': (0, 0),
    'B': (1, 5),
    'C': (5, 2),
    'D': (6, 6),
    'E': (8, 3),
    'F': (3, 7),
    'G': (2, 2)
}

CITY_NAMES = list(CITIES.keys())
COORDS = np.array(list(CITIES.values()))
NUM_CITIES = len(CITY_NAMES)

# Compute Euclidean Distance Matrix
DIST_MATRIX = np.zeros((NUM_CITIES, NUM_CITIES))
for i in range(NUM_CITIES):
    for j in range(NUM_CITIES):
        DIST_MATRIX[i, j] = np.linalg.norm(COORDS[i] - COORDS[j])


def get_tour_distance(path):
    """Calculates total closed-loop Euclidean distance for a given path sequence."""
    total_dist = 0.0
    for i in range(len(path)):
        u = path[i]
        v = path[(i + 1) % len(path)]
        total_dist += DIST_MATRIX[u, v]
    return total_dist


def format_path(path):
    """Converts index path into readable city names."""
    return " -> ".join([CITY_NAMES[idx] for idx in path]) + f" -> {CITY_NAMES[path[0]]}"


# ---------------------------------------------------------
# 1. Greedy Algorithm (Nearest Neighbor)
# ---------------------------------------------------------
def greedy_tsp(start_node=0):
    unvisited = set(range(NUM_CITIES))
    current = start_node
    path = [current]
    unvisited.remove(current)

    while unvisited:
        next_node = min(unvisited, key=lambda node: DIST_MATRIX[current, node])
        path.append(next_node)
        unvisited.remove(next_node)
        current = next_node

    return path, get_tour_distance(path)


# ---------------------------------------------------------
# 2. Improvement Method (2-Opt Local Search)
# ---------------------------------------------------------
def improvement_tsp():
    path = list(range(NUM_CITIES))
    best_dist = get_tour_distance(path)
    improved = True

    while improved:
        improved = False
        for i in range(1, NUM_CITIES - 1):
            for j in range(i + 1, NUM_CITIES):
                # Perform 2-opt edge swap (subsegment reversal)
                new_path = path[:i] + path[i:j + 1][::-1] + path[j + 1:]
                new_dist = get_tour_distance(new_path)
                if new_dist < best_dist:
                    path = new_path
                    best_dist = new_dist
                    improved = True
                    break
            if improved:
                break

    return path, best_dist


# ---------------------------------------------------------
# 3. Hill Climbing Algorithm
# ---------------------------------------------------------
def hill_climbing_tsp(max_iterations=1000):
    current_path = list(range(NUM_CITIES))
    random.shuffle(current_path)
    current_dist = get_tour_distance(current_path)

    for _ in range(max_iterations):
        # Generate neighbor by swapping two random cities
        i, j = random.sample(range(NUM_CITIES), 2)
        neighbor_path = current_path.copy()
        neighbor_path[i], neighbor_path[j] = neighbor_path[j], neighbor_path[i]
        neighbor_dist = get_tour_distance(neighbor_path)

        # Accept move only if strictly better
        if neighbor_dist < current_dist:
            current_path = neighbor_path
            current_dist = neighbor_dist

    return current_path, current_dist


# ---------------------------------------------------------
# 4. Simulated Annealing
# ---------------------------------------------------------
def simulated_annealing_tsp(initial_temp=1000.0, cooling_rate=0.995, max_iterations=2000):
    current_path = list(range(NUM_CITIES))
    random.shuffle(current_path)
    current_dist = get_tour_distance(current_path)

    best_path = list(current_path)
    best_dist = current_dist
    temp = initial_temp

    for _ in range(max_iterations):
        if temp < 1e-4:
            break

        i, j = sorted(random.sample(range(NUM_CITIES), 2))
        candidate_path = current_path[:i] + current_path[i:j + 1][::-1] + current_path[j + 1:]
        candidate_dist = get_tour_distance(candidate_path)

        delta = candidate_dist - current_dist

        # Metropolis acceptance criterion
        if delta < 0 or random.random() < math.exp(-delta / temp):
            current_path = candidate_path
            current_dist = candidate_dist
            if current_dist < best_dist:
                best_path = list(current_path)
                best_dist = current_dist

        temp *= cooling_rate

    return best_path, best_dist


# ---------------------------------------------------------
# 5. Gradient Descent (Continuous Surrogate Optimization)
# ---------------------------------------------------------
def gradient_descent_tsp(learning_rate=0.05, max_iterations=1000):
    # Continuous priority vector where argsort(x) yields permutation order
    x = np.random.randn(NUM_CITIES)

    def loss_fn(vec):
        order = np.argsort(vec)
        return get_tour_distance(order)

    best_x = np.copy(x)
    best_dist = loss_fn(x)
    eps = 1e-3

    for _ in range(max_iterations):
        grad = np.zeros(NUM_CITIES)
        current_loss = loss_fn(x)

        # Finite-difference numerical gradient calculation
        for i in range(NUM_CITIES):
            x_step = np.copy(x)
            x_step[i] += eps
            grad[i] = (loss_fn(x_step) - current_loss) / eps

        # Update continuous priority parameters with slight stochastic exploratory noise
        x = x - learning_rate * grad + np.random.normal(0, 0.01, size=NUM_CITIES)
        current_dist = loss_fn(x)

        if current_dist < best_dist:
            best_dist = current_dist
            best_x = np.copy(x)

    best_path = list(np.argsort(best_x))
    return best_path, best_dist


# ---------------------------------------------------------
# Execution and Comparison
# ---------------------------------------------------------
if __name__ == "__main__":
    algorithms = [
        ("1. Greedy Algorithm", greedy_tsp),
        ("2. Improvement Method (2-Opt)", improvement_tsp),
        ("3. Hill Climbing Algorithm", hill_climbing_tsp),
        ("4. Simulated Annealing", simulated_annealing_tsp),
        ("5. Gradient Descent", gradient_descent_tsp),
    ]

    print("=" * 70)
    print("      TRAVELLING SALESPERSON PROBLEM (TSP) OPTIMIZATION METHODS")
    print("=" * 70)

    for name, algo_fn in algorithms:
        path, distance = algo_fn()
        print(f"\nMethod: {name}")
        print(f"Path:     {format_path(path)}")
        print(f"Distance: {distance:.4f}")

    print("\n" + "=" * 70)