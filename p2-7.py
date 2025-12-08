from itertools import zip_longest


def polynomial_sum(p1, p2):
    result = tuple(reversed(tuple((i1 + i2 for i1, i2 in zip_longest(reversed(p1), reversed(p2), fillvalue=0)))))
    first_non_zero = next((i for i, x in enumerate(result) if x != 0), 0)
    return result[first_non_zero:]

import re

def polynomial(p):
    result = []
    
    def argument(arg, degree):
        if arg == 0 and degree == 0:
            return ''
        elif degree == 0:
            return str(arg) if arg < 0 else f'+{arg}'
        elif arg == 1:
            return 
    
    for num, arg in enumerate(p):
        degree = len(p) - num
        
        

print(polynomial((-1, -1)))
print(polynomial((1, 3, -1, 1, -2)))
print(polynomial((1, 1, 1)))