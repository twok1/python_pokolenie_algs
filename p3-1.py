import math

def is_power_of_four(n):
    return math.log(n, 4).is_integer()

import math

def intersections(a, b, c, k, m):
    # a*x^2 + x*(b-k) + c - m = 0
    d = (b - k)** 2 - 4 * a * (c-m)
    if d < 0:
        return set()
    x1 = (-(b-k) - d ** (1/2))/ (2 * a)
    x2 = (-(b-k) + d ** (1/2))/ (2 * a)
    return set(((x1, k*x1+m), (x2, k*x2+m)))


def optimal_value(nums):
    return 2 * sum(nums) / (2 * len(nums))
