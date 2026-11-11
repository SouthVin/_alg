# lambda_calculus.py

class Expr:
    def free_vars(self):
        pass
    def substitute(self, var, val):
        pass

class Var(Expr):
    """Represents a Variable, e.g., 'x'"""
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def free_vars(self):
        return {self.name}

    def substitute(self, var, val):
        if self.name == var:
            return val
        return self

class Abs(Expr):
    """Represents an Abstraction (Function), e.g., 'λx.M'"""
    def __init__(self, param, body):
        self.param = param
        self.body = body

    def __str__(self):
        return f"(λ{self.param}.{self.body})"

    def free_vars(self):
        return self.body.free_vars() - {self.param}

    def substitute(self, var, val):
        if self.param == var:
            return self
        
        # Alpha-conversion to avoid variable capture
        if self.param in val.free_vars() and var in self.body.free_vars():
            new_param = self.param + "'"
            new_body = self.body.substitute(self.param, Var(new_param))
            return Abs(new_param, new_body.substitute(var, val))
            
        return Abs(self.param, self.body.substitute(var, val))

class App(Expr):
    """Represents an Application, e.g., '(M N)'"""
    def __init__(self, func, arg):
        self.func = func
        self.arg = arg

    def __str__(self):
        return f"({self.func} {self.arg})"

    def free_vars(self):
        return self.func.free_vars() | self.arg.free_vars()

    def substitute(self, var, val):
        return App(self.func.substitute(var, val), self.arg.substitute(var, val))

def reduce_step(expr):
    """Performs one step of Beta-reduction (Normal Order)"""
    if isinstance(expr, App):
        if isinstance(expr.func, Abs):
            # Beta Reduction Rule: (λx.M) N -> M[x := N]
            return expr.func.body.substitute(expr.func.param, expr.arg), True
        
        # Try reducing the left side (function)
        new_func, reduced = reduce_step(expr.func)
        if reduced:
            return App(new_func, expr.arg), True
            
        # Try reducing the right side (argument)
        new_arg, reduced = reduce_step(expr.arg)
        if reduced:
            return App(expr.func, new_arg), True
            
    elif isinstance(expr, Abs):
        # Reduce inside the abstraction body
        new_body, reduced = reduce_step(expr.body)
        if reduced:
            return Abs(expr.param, new_body), True
            
    return expr, False

def run_interpreter(expr):
    """Runs the interpreter and prints every step of the calculation"""
    print(f"Input : {expr}")
    step = 1
    while True:
        expr, reduced = reduce_step(expr)
        if not reduced:
            break
        print(f"Step {step}: {expr}")
        step += 1
    print("Result: Normal form reached.\n" + "-"*40)


if __name__ == "__main__":
    print("=== Lambda Calculus Interpreter ===\n")

    # Example 1: Identity Function
    # (λx.x) y  -> y
    id_func = Abs("x", Var("x"))
    expr1 = App(id_func, Var("y"))
    print("Test 1: Identity Function")
    run_interpreter(expr1)

    # Example 2: TRUE conditional
    # TRUE a b = (λx.λy.x) a b  -> a
    true_func = Abs("x", Abs("y", Var("x")))
    expr2 = App(App(true_func, Var("a")), Var("b"))
    print("Test 2: TRUE Conditional")
    run_interpreter(expr2)

    # Example 3: Variable Capture (Alpha-Conversion test)
    # (λx.λy.x y) y -> (λy'.y y')
    expr3 = App(Abs("x", Abs("y", App(Var("x"), Var("y")))), Var("y"))
    print("Test 3: Alpha-Conversion (Preventing Variable Capture)")
    run_interpreter(expr3)