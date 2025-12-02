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
    
