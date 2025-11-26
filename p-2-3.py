def is_point_in_rectangle(p, rect):
    a, b = rect
    return p[0] in range(a[0] + 1, b[0]) and p[1] in range(a[1] + 1, b[1])

# print(is_point_in_rectangle((3, 0), [(0, 0), (10, 1)]))
# print(is_point_in_rectangle((-5, -6), [(-10, -7), (-4, -2)]))

def draw_graph(f):
    print('y ^')
    for y in range(9, 0, -1):
        if y > 0:
            print(f'{y} |', end='')
        for x in range(1, 10):
            if y == f(x):
                print('  *', end='')
            else:
                print('   ', end='')
        print('')
    print('+--------------------------- > x')
    print('     1  2  3  4  5  6  7  8  9')
                
                
def f(x):
    if x in (1, 2):
        return 1
    return f(x - 1) + f(x - 2)

# draw_graph(f)