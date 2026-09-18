

def one_truth(flags: list):
    return flags.count(True) == 1


# def one_truth(flags):
#     return sum(flags) == 1


# print(one_truth([True]))
# print(one_truth([False, False, False, False, False]))


# def one_truth(flags: list):
#     result = 0
#     for i in flags:
#         if i:
#             result += 1
#         if result > 1:
#             return False
#     if result:
#         return True
#     return False


# print(one_truth([True]))
# print(one_truth([False, False, False, False, False, True]))
# print(one_truth([False, False, False, False, False]))
# print(one_truth([True, True, False, False, False]))

import re

def parse_max(s):
    result = tuple(map(int, (i for i in re.split(r'[a-zA-Z]+', s, flags=0) if i)))
    if result:
        return max(result)
    return -1


# print(parse_max('100klh564abc365bg'))
# print(parse_max('0'))
# print(parse_max('asfasgh'))

def equilibrium(nums: list):
    nums = [0] + nums + [0]
    for i in range(1, len(nums)):
        if sum(nums[:i]) == sum(nums[i+1:]):
            return i - 1
    return -1

# print(equilibrium([1, 1, 1, 1, 1]))
# print(equilibrium([4, 0, 0]))
# print(equilibrium([2, 1, 1]))

def letter_by_sum(letters):
    total = sum(ord(char) - ord('a') + 1 for char in letters)
    index = total % 26
    if index == 0:
        index = 26
    return chr(ord('a') + index - 1)

# print(letter_by_sum(['z', 'z']))

def is_perfect_possible(key, answers):
    result = tuple(a == b for a, b in zip(key, answers) if a != '*')
    return all(not i for i in result) or all(result)

# print(is_perfect_possible(['A', 'B', 'C', '*', '*'], ['A', 'B', 'C', 'D', 'E']))
# print(is_perfect_possible(['A', 'B', 'B', '*', '*'], ['A', 'B', 'C', 'A', 'B']))
# print(is_perfect_possible(['A', 'B', 'C', '*', '*'], ['D', 'E', 'F', 'A', 'B']))

def count_animals(heads, legs):
    if legs % 2:
        return None
    rabbits = (legs - 2 * heads) / 2
    ducks = heads - rabbits
    if int(rabbits) == rabbits and int(ducks) == ducks and ducks >= 0 and rabbits >= 0:
        return int(ducks), int(rabbits)
    return None

# print(count_animals(2, 6))
# print(count_animals(10, 20))
# print(count_animals(6, 24))
# print(count_animals(1, 1))
# print(count_animals(0, 0))
# print(count_animals(0, 100))

def is_order(nums, strict = True):
    asc = (nums == sorted(nums) or nums == sorted(nums, reverse=True))
    if strict:
        return asc and len(set(nums)) == len(nums)
    else:
        return asc and len(set(nums)) <= len(nums)

# print(is_order([1, 2, 3, 4, 5], strict=True))
# print(is_order([1, 2, 2, 3, 3]))
# print(is_order([1, 2, 3, 4, 5], strict=False))
# print(is_order([-2, -1, 1, 2, 2, 3, 5], strict=False))
# print(is_order([1, 3, 2, 4, 5], strict=False))
# print(is_order([1], strict=True))

def wave(nums):
    for i in range(0, len(nums) - 1, 2):
        nums[i], nums[i+1] = nums[i+1], nums[i]

# data = [1, 2, 3, 4, 5] # [2, 1, 4, 3, 5]
# wave(data)
# print(data)
# data = [2, 4, 7, 8, 9, 10] # [4, 2, 8, 7, 10, 9]
# wave(data)
# print(data)
# data = [1, 1, 1, 1, 1, 1]
# wave(data)
# print(data)

def count_days(cur):
    days = 0
    while cur % 2:
        days += 1
        cur = (cur - 1) / 2
    return days
    
# print(count_days(23))