def calculate_sum(n):
    result = ((1 + n) * n // 2) ** 2
    return int(result)

def get_exam_position(n, k):
    def count_of_nums(n):
        return n // 2 + n % 2
    if k % 2:
        return count_of_nums(k)
    else:
        return count_of_nums(n) + count_of_nums(k)

def count_solutions(n):
    counter = 0
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            z = n - 3*x - 2*y
            if z > 0:
                counter += 1
    return counter

def area_of_tree(n):
    return (n * 2 + 1) + (2 + n * 2) * n // 2


def diff_even_odd(a, b):
    sum_even = ((a + a%2) + (b - b%2)) * (b//2 - (a-1)//2) // 2
    sum_odd = ((a // 2 * 2 + 1) + (b - (b + 1) % 2)) * (b-a+1 - (b//2 - (a-1)//2)) // 2
    return sum_even - sum_odd


# print(diff_even_odd(1, 1))
# print(diff_even_odd(3, 8))
# print(diff_even_odd(1, 10))
# print(diff_even_odd(10, 10))

from decimal import Decimal

def calculate_product(n):
    return format(Decimal(1)/ Decimal(n), 'f')


def calculate_sum(n):
    if not n % 2:
        return - (1 + n) * n // 2
    return - (1 + n - 1) * (n - 1) // 2 + n * n
    
# print(calculate_sum(5))

def sold_out(n, m):
    result = max(2*m - 2*n + 2, 1)
    return  result

def calculate_sum(n):
    return (2**(n + 1) - 1)


def number_of_handshakes(n):
    return n * (n - 1) // 2

import math
def count_friends(k):
    return int(1 + math.sqrt(1 + 8*k)) // 2