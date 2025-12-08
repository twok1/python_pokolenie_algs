def linear_coefficients(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    k = (y2 - y1) / (x2 - x1)
    b = (y1 * x2 - y2 * x1) / (x2 - x1)
    return (k, b)

# print(linear_coefficients((1, 2), (2, 3)))
# print(linear_coefficients((0, 0), (1, 5)))
# print(linear_coefficients((0, 2), (2, 2)))

def on_one_line(p1, p2, p3):
    x1, y1, x2, y2, x3, y3 = *p1, *p2, *p3
    k = (y2 - y1) / (x2 - x1)
    b = y1 - k * x1
    return y3 == k * x3 + b
    
# print(on_one_line((1, 1), (2, 2), (3, 3)))

def equation_of_line(values):
    b = values[0]
    k = values[1] - b
    i = 0
    while i < len(values) - 3:
        if not on_one_line(*zip((i, i+1, i+2), values[i:i+3])):
            return None
        i += 1
    if b > 0:
        if k == 1:
            return f'y = x + {b}'
        elif k == 0:
            return f'y = {b}'
        elif k == -1:
            return f"y = -x + {b}"
        else:
            return f"y = {k}x + {b}"
    elif b == 0:
        b = ''
        if k == 1:
            return 'y = x'
        elif k == 0:
            return 'y = 0'
        elif k == -1:
            return 'y = -x'
        else:
            return f'y = {k}x'
    else:
        if k == 1:
            return f'y = x - {abs(b)}'
        elif k == 0:
            return f'y = {b}'
        elif k == -1:
            return f'y = -x - {abs(b)}'
        else:
            return f'y = {k}x - {abs(b)}'
    

# print(equation_of_line([0, 1, 2, 3, 4]))
# print(equation_of_line([1, 3, 5, 7, 9]))
# print(equation_of_line([6, 6, 6, 6, 6]))
# print(equation_of_line([1, 1, 2, 2, 2]))
# print(equation_of_line([0, -2, -4, -6, -8]))
# print(equation_of_line([0, -1, -2, -3, -4]))

def quadratic_values(a, b, c, start=0, step=1):
    def f(x):
        return a * x ** 2 + b * x + c
    return list(((x, f(x)) for x in range(start, start + 10 * step, step)))

# print(quadratic_values(-1, -1, -1))

def solve(a, b, c):
    d = b ** 2 - 4 * a * c
    if d < 0:
        return set()
    else:
        return set((-b + i * d ** 0.5)/ (2 * a) for i in (-1, 1))
    
# print(solve(1, -5, 6))
# print(solve(1, -2, 1))


# print(solve(5, -2, 1))

def quadratic(x1, x2):
    def suffix(num, post=''):
        prefix = '-' if num < 0 else '+'
        return f' {prefix} {abs(num)}{post}'.replace(' 1x', ' x') if num else ''
    b = - (x1 + x2)
    c = x1 * x2
    return f'x^2{suffix(b, 'x')}{suffix(c)} = 0'

# print(quadratic(1, 2))
# print(quadratic(0, 1))

def quadratic_intersections(a1, b1, c1, a2, b2, c2):
    a, b, c = a1 - a2, b1 - b2, c1 - c2
    def f(x):
        return a1 * x ** 2 + b1 * x + c1
    if a != 0:
        d = b ** 2 - 4 * a * c
        if d >= 0:
            result = sorted(set((-b + i * d ** 0.5) / (2 * a) for i in (-1, 1)))
        else:
            result = ()
        return {(x, f(x)) for x in result}
    else:
        return {(- c / b, f(- c / b))} if b != 0 else set()


print(quadratic_intersections(1, -2, 1, -1, -1, 7))
print(quadratic_intersections(1, 2, 3, 4, 5, 6))
print(quadratic_intersections(2, 2, 5, 2, 2, 1))