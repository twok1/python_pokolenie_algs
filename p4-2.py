
from math import log


def mystery(n):
    return n ** 2 - 1

def mystery(n):
    if n % 2:
        return n + 1
    else:
        return n + 2
    

def mystery(n):
    return sum((i for i in range(n + 1)))

def mystery(n):
    d = {
        1: 0,
        0: 1,
        8: 2,
        9: 1,
        3: 0,
        4: 0,
        6: 1,
        2: 0,
    }
    if n // 10 == 0:
        return d[n % 10]
    else:
        return mystery(n // 10) + d[n % 10]

def sum_of_squares(n):
    return sum((i ** 2 for i in range(1, n + 1)))


def even_odd(nums):
    return len({i % 2 for i in nums}) == 1

def hamming_distance(s1, s2):
    result = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            result += 1
    return result


# print(hamming_distance('abcd', 'efgh'))


def longest_substring_without_vowels(s):
    this_line, result = 0, 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in s:
        if i in vowels:
            result = max(result, this_line)
            this_line = 0
        else:
            this_line += 1
    return max(result, this_line)

# print(longest_substring_without_vowels('bcdgf'))         # bcdgf


def min_digit_sum(a, b):
    def sum_digits(num):
        if num < 10:
            return num
        return sum_digits(num // 10) + num % 10
    prom = tuple(sum_digits(i) for i in range(a, b+1))
    m = min(prom)
    result = tuple(1 if i == m else 0 for i in prom)
    return(sum(result))

# print(min_digit_sum(5, 18345))


def  avg_values(nums):
    result =[]
    if nums :
        result = [float(nums[0])] 
        for i, k in enumerate(nums[1:],start=1):
            result.append(sum((nums[0:i + 1])) / (i + 1))
    return result
    
# print(avg_values([]))
# print(avg_values([10, 20, 30, 40, 50]))

from math import floor, log10

def divisible(n):
    result = 0
    for i in range(floor(log10(n)) + 1):
        k = n // (10 ** i) % 10
        if k and int(n / k) == n / k:
            result += 1
    return result
            
            

# print(divisible(22))

from math import ceil, log10

def make_palindrome(n):
    def get_i_num(num, i):
        return num // (10 ** i) % 10
    def check_palindrome(num):
        for i in range(ceil(log10(num)/2)):
            print(get_i_num(num, i))
    k = 0
    def recur(n):
        
        if k == 5:
            return -1
    check_palindrome(n)

make_palindrome(121)
make_palindrome(1221)