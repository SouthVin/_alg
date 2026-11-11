# custom_iterative.py
# Solving a square root problem using an iterative method (Newton-Raphson)

def newton_sqrt(n, tolerance=1e-7, max_iter=1000):
    """
    Finds the square root of n using the Newton-Raphson iterative method.
    """
    if n < 0:
        raise ValueError("Cannot compute the square root of a negative number.")
    
    x = n / 2.0  # Initial guess
    for i in range(max_iter):
        next_x = 0.5 * (x + (n / x))
        
        # Check for convergence (difference is smaller than tolerance)
        if abs(next_x - x) < tolerance:
            print(f"Converged at iteration {i+1}")
            return next_x
        
        x = next_x
        
    print("Reached maximum iteration limit.")
    return x

if __name__ == "__main__":
    number = 612
    result = newton_sqrt(number)
    print(f"The square root of {number} is approximately {result:.5f}")