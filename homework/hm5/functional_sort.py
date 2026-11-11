# functional_sort.py

# 1. Custom Map, Filter, Reduce without loops (using recursion)
def my_map(func, lst):
    if not lst:
        return []
    return [func(lst[0])] + my_map(func, lst[1:])

def my_filter(func, lst):
    if not lst:
        return []
    if func(lst[0]):
        return [lst[0]] + my_filter(func, lst[1:])
    else:
        return my_filter(func, lst[1:])

def my_reduce(func, lst, initial):
    if not lst:
        return initial
    return my_reduce(func, lst[1:], func(initial, lst[0]))

# 2. Bubble Sort implemented entirely without loops using custom reduce and recursion
def bubble_pass(lst):
    """Does a single pass of bubble sort using my_reduce."""
    if not lst:
        return []
        
    def step(acc, x):
        # acc is a tuple: (list_so_far, current_max)
        seq, curr_max = acc
        if x > curr_max:
            return (seq + [curr_max], x)
        else:
            return (seq + [x], curr_max)
            
    # Initial state for reduce: (empty_list, first_element)
    seq, max_val = my_reduce(step, lst[1:], ([], lst[0]))
    return seq + [max_val]

def bubble_sort(lst):
    """Recursively apply bubble_pass to sort the list (No loops allowed)."""
    if len(lst) <= 1:
        return lst
        
    passed = bubble_pass(lst)
    
    # Sort the remaining items and append the correctly placed largest element
    return bubble_sort(passed[:-1]) + [passed[-1]]

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    
    print("Original List:", arr)
    sorted_arr = bubble_sort(arr)
    print("Sorted List (Bubble Sort without loops):", sorted_arr)
    
    # Testing custom map and filter just to show they work
    print("\nTesting Custom map (x * 2):", my_map(lambda x: x*2, [1, 2, 3]))
    print("Testing Custom filter (x > 2):", my_filter(lambda x: x>2, [1, 2, 3, 4]))