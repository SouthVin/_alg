# sym_diff.py

def sym_diff(expr, var='x'):
    """
    Recursive symbolic differentiation.
    Expression is represented as tuples: ('+', left, right), ('*', left, right), etc.
    """
    # Rule 1: Derivative of a constant is 0
    if isinstance(expr, (int, float)):
        return 0
    
    # Rule 2: Derivative of the variable is 1, other variables are 0
    if isinstance(expr, str):
        return 1 if expr == var else 0
    
    # Extract operator and operands
    op = expr[0]
    
    if op == '+':
        # (u + v)' = u' + v'
        return ('+', sym_diff(expr[1], var), sym_diff(expr[2], var))
        
    elif op == '-':
        # (u - v)' = u' - v'
        return ('-', sym_diff(expr[1], var), sym_diff(expr[2], var))
        
    elif op == '*':
        # (u * v)' = u'v + uv'
        u, v = expr[1], expr[2]
        du = sym_diff(u, var)
        dv = sym_diff(v, var)
        return ('+', ('*', du, v), ('*', u, dv))
        
    else:
        raise ValueError(f"Unknown operator: {op}")

def print_expr(expr):
    """Helper to print the tuple expression as a readable string."""
    if isinstance(expr, (int, float, str)):
        return str(expr)
    return f"({print_expr(expr[1])} {expr[0]} {print_expr(expr[2])})"

if __name__ == "__main__":
    # Example expression: f(x) = (x * x) + (2 * x)
    expr = ('+', ('*', 'x', 'x'), ('*', 2, 'x'))
    
    derivative = sym_diff(expr, 'x')
    
    print(f"Original f(x): {print_expr(expr)}")
    print(f"Derivative f'(x): {print_expr(derivative)}")