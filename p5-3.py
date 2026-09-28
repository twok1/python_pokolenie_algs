def fizz_buzz(n):
    n = n - 1
    a = n // 3 - n // 15
    b = n // 5 - n // 15
    c = n // 15
    return a, b , c

def calculate_sum(n):
    return (n - 1) / n

def calculate_sum(n):
    return (((n % 2 or 3) + 2*n - 1) * ((2 * n - 1)//4 + 1)) // 2
    
def max_consecutive_elements(s):
    if not s:
        return 0
    best = cur = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            cur += 1
        else:
            best = max(cur, best)
            cur = 1
    return max(best, cur)


def water_requirement(n):
    return ((4 + (n - 1) * 2) * n) // 2 + 1