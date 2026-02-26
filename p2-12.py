from math import floor, log10

def count_digits(n):
    return floor(log10(n)) + 1


from math import log2

def is_power_of_two(n):
    return log2(n).is_integer()


from math import log2, ceil

def closest_exponent(n):
    return ceil(log2(n))

from math import log2

def iterated_log(n):
    i = 0
    while n > 1:
        n = log2(n)
        i += 1
    return i

from math import log10, floor

def count_powers(num):
    n = 0
    result = 0
    while result != num:
        n += 1
        result = result * 10 ** (floor(log10(2 ** n)) + 1) + 2 ** n
    return n

print(count_powers(248))
print(count_powers(24816))
print(count_powers(2))
