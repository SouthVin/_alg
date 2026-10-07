# hanoi.py

def hanoi_recursive(n, source, auxiliary, target):
    """Solve Tower of Hanoi using Recursion."""
    if n > 0:
        hanoi_recursive(n - 1, source, target, auxiliary)
        print(f"Move disk {n} from {source} to {target}")
        hanoi_recursive(n - 1, auxiliary, source, target)

def hanoi_iterative(n, source, auxiliary, target):
    """Solve Tower of Hanoi without Recursion (using a Stack)."""
    # Stack stores tuples of: (disk_number, source, auxiliary, target, is_ready)
    stack = [(n, source, auxiliary, target, False)]
    
    while stack:
        disk, src, aux, tgt, is_ready = stack.pop()
        
        if disk == 0:
            continue
            
        if is_ready:
            print(f"Move disk {disk} from {src} to {tgt}")
        else:
            # Simulate the call stack in reverse order
            stack.append((disk - 1, aux, src, tgt, False))
            stack.append((disk, src, aux, tgt, True))
            stack.append((disk - 1, src, tgt, aux, False))

if __name__ == "__main__":
    n = 3
    print("=== Hanoi Recursive ===")
    hanoi_recursive(n, 'A', 'B', 'C')
    
    print("\n=== Hanoi Iterative ===")
    hanoi_iterative(n, 'A', 'B', 'C')