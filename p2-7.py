from itertools import zip_longest


def polynomial_sum(p1, p2):
    result = tuple(reversed(tuple((i1 + i2 for i1, i2 in zip_longest(reversed(p1), reversed(p2), fillvalue=0)))))
    first_non_zero = next((i for i, x in enumerate(result) if x != 0), 0)
    return result[first_non_zero:]

p1 = (1, 7, 0, -4)               # P1(x) = x^3 + 7x^2 - 4
p2 = (-1, 0, 0, 2)               # P2(x) = -x^3 + 2

print(polynomial_sum(p1, p2))    # P1(x) + P2(x) = 7x^2 - 2

p1 = (1, 2, 3, 4, 5)             # P1(x) = x^4 + 2x^3 + 3x^2 + 4x + 5
p2 = (1,)                        # P2(x) = 1

print(polynomial_sum(p1, p2))    # P1(x) + P2(x) = x^4 + 2x^3 + 3x^2 + 4x + 6