import time

def lcs_recursive(X, Y, m, n):
    """
    Non-Dynamic Programming approach: Naive Recursion
    Returns the length of the Longest Common Subsequence of X[0..m-1] and Y[0..n-1]
    """
    # Base Case: If either string is empty, the common subsequence is 0
    if m == 0 or n == 0:
        return 0
    
    # If the last characters match, add 1 to the result and check the rest
    elif X[m-1] == Y[n-1]:
        return 1 + lcs_recursive(X, Y, m-1, n-1)
    
    # If the last characters do not match, find the max of two possibilities:
    # 1. Ignoring the last character of X
    # 2. Ignoring the last character of Y
    else:
        return max(lcs_recursive(X, Y, m, n-1), lcs_recursive(X, Y, m-1, n))


def lcs_dp(X, Y):
    """
    Dynamic Programming approach: Bottom-up Tabulation
    Returns the length of the Longest Common Subsequence of X and Y
    """
    m = len(X)
    n = len(Y)
    
    # Create a 2D array to store lengths of longest common subsequence
    # L[i][j] contains length of LCS of X[0..i-1] and Y[0..j-1]
    L = [[0 for _ in range(n+1)] for _ in range(m+1)]

    # Build the L matrix in bottom-up fashion
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
                
    # L[m][n] contains the final answer
    return L[m][n]

if __name__ == '__main__':
    # Test strings
    S1 = "AGGTAB"
    S2 = "GXTXAYB"
    
    print(f"String 1: {S1}")
    print(f"String 2: {S2}")
    print("-" * 30)

    # 1. Test Dynamic Programming Approach
    start_time_dp = time.perf_counter()
    dp_result = lcs_dp(S1, S2)
    end_time_dp = time.perf_counter()
    print(f"DP Approach Result: {dp_result}")
    print(f"DP Approach Time  : {end_time_dp - start_time_dp:.8f} seconds")
    
    print("-" * 30)

    # 2. Test Non-Dynamic Programming (Recursive) Approach
    start_time_rec = time.perf_counter()
    rec_result = lcs_recursive(S1, S2, len(S1), len(S2))
    end_time_rec = time.perf_counter()
    print(f"Recursive Approach Result: {rec_result}")
    print(f"Recursive Approach Time  : {end_time_rec - start_time_rec:.8f} seconds")