import itertools

def solve_sat(expression, variables):
    """
    Menyelesaikan masalah SAT dengan menyebutkan seluruh kemungkinan tabel kebenaran.
    
    :param expression: String ekspresi boolean (gunakan sintaks Python: and, or, not)
    :param variables: List dari nama variabel dalam ekspresi
    """
    n = len(variables)
    # Menghasilkan semua kombinasi True/False sebanyak 2^n
    # itertools.product([False, True], repeat=3) -> (F,F,F), (F,F,T), ...
    truth_combinations = list(itertools.product([False, True], repeat=n))
    
    print(f"Ekspresi: {expression}")
    
    # Mencetak header tabel
    header = " | ".join(variables) + " | Result"
    print("-" * len(header))
    print(header)
    print("-" * len(header))
    
    satisfiable_assignments = []
    
    # Mengevaluasi setiap kombinasi
    for combo in truth_combinations:
        # Memetakan nama variabel ke nilai kebenarannya (contoh: {'A': True, 'B': False})
        env = dict(zip(variables, combo))
        
        # Mengevaluasi ekspresi boolean dengan nilai dari env
        result = eval(expression, {}, env)
        
        # Mencetak baris tabel (menggunakan 1 untuk True, 0 untuk False agar rapi)
        row_values = " | ".join([str(int(val)) for val in combo])
        print(f"{row_values} | {int(result)}")
        
        # Jika hasilnya True, simpan kombinasi ini sebagai solusi
        if result:
            satisfiable_assignments.append(env)
            
    print("-" * len(header))
    
    # Kesimpulan Akhir
    if satisfiable_assignments:
        print("\nStatus: SATISFIABLE")
        print("Kombinasi yang bernilai True:")
        for sol in satisfiable_assignments:
            print(sol)
        return True
    else:
        print("\nStatus: UNSATISFIABLE")
        return False

# --- PENGUJIAN ---
if __name__ == "__main__":
    # Contoh 1: Ekspresi yang Satisfiable (Bisa bernilai True)
    # (A OR B) AND (NOT C)
    vars_1 = ["A", "B", "C"]
    expr_1 = "(A or B) and (not C)"
    
    print("Test Case 1:")
    solve_sat(expr_1, vars_1)
    print("\n" + "="*40 + "\n")
    
    # Contoh 2: Ekspresi yang Unsatisfiable (Kontradiksi, selalu False)
    # A AND (NOT A)
    vars_2 = ["A"]
    expr_2 = "A and (not A)"
    
    print("Test Case 2:")
    solve_sat(expr_2, vars_2)