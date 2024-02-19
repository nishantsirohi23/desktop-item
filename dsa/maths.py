a = [2, 4, 4, 5, 6, 6]

def is_divisible_by_k(subsequence, k):
    for i in range(len(subsequence) - 1):
        if (subsequence[i] + subsequence[i + 1]) % k != 0:
            return False
    return True

def backtrack(a, k, n, current_sum, sol):
    if current_sum % k == 0 and len(sol) > 1:
        if is_divisible_by_k(sol, k):
            print(sol)
    
    for i in range(k, n):
        if (current_sum + a[i]) % k == 0:
            sol.append(a[i])
            backtrack(a, i + 1, n, current_sum + a[i], sol)
            sol.pop()

# Example usage
backtrack(a, 0, len(a), 0, [])
output = 