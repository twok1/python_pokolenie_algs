from itertools import zip_longest


def polynomial_sum(p1, p2):
    result = tuple(reversed(tuple((i1 + i2 for i1, i2 in zip_longest(reversed(p1), reversed(p2), fillvalue=0)))))
    first_non_zero = next((i for i, x in enumerate(result) if x != 0), 0)
    return result[first_non_zero:]

import re

def polynomial(p):
    result = []
    
    def argument(arg, degree, num):
        if not arg:
            return ''
        result = f'+{arg}x^{degree}' if arg > 0 else f'{arg}x^{degree}'
        result = re.sub(r'x\^0', r'', result)
        result = result.replace('+', '') if not num else result
        result = re.sub(r'^([+-])1x', r'\1x', result)
        result = re.sub(r'^1x', r'x', result)
        result = re.sub(r'x\^1$', 'x', result)
        return result
        
    
    for num, arg in enumerate(p):
        degree = len(p) - num - 1
        result.append(argument(arg, degree, num))
    return ''.join(result)
        
        

# print(polynomial((-1, -1)))
print(polynomial((1, 3, -1, 1, -2)))
# print(polynomial((1, 1, 1)))

def polynomial_creator(p):
    def f(x):
        result = []
        def argument(arg, degree, num):
            if not arg:
                return ''
            result = f'+{arg}*x**{degree}' if arg > 0 else f'{arg}*x**{degree}'
            result = re.sub(r'\*x\*\*0', r'', result)
            result = result.replace('+', '') if not num else result
            result = re.sub(r'^([+-])1\*x', r'\1x', result)
            result = re.sub(r'^1\*x', r'x', result)
            result = re.sub(r'x\*\*1$', 'x', result)
            return result
            
        
        for num, arg in enumerate(p):
            degree = len(p) - num - 1
            result.append(argument(arg, degree, num))
        return eval(''.join(result).replace('x', f'({x})'))
    return f



def polynomial_product(p1, p2):
    result = []
    
    def argument(arg, degree, num):
        if not arg:
            return ''
        result = f'+{arg}x^{degree}' if arg > 0 else f'{arg}x^{degree}'
        result = re.sub(r'x\^0', r'', result)
        result = result.replace('+', '') if not num else result
        result = re.sub(r'^([+-])1x', r'\1x', result)
        result = re.sub(r'^1x', r'x', result)
        result = re.sub(r'x\^1$', 'x', result)
        return result
        
    
    for num, arg in enumerate(p):
        degree = len(p) - num - 1
        result.append(argument(arg, degree, num))
    return ''.join(result)