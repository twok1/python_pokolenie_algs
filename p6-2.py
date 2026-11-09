def find_sum_indexes(nums, value):
    i = k = 0
    for i in range(len(nums)):
        sums = 0
        for k in range(i, len(nums)):
            sums += nums[k]
            if sums == value:
                return (i, k)
    return -1


def sequence_type(nums):
    result = [
        False,
        False,
        False,
        False,
        False,
    ]
    prev = nums[0]
    for i, v in enumerate(nums):
        if i > 0:
            if v == prev:
                result[0] = True
                result[1] = True
            elif v > prev:
                result[2] = True
            elif v < prev:
                result[3] = True
            prev = v
    if all((result[2:4])):
        return 'RANDOM'
    elif all((result[1:3])):
        return 'WEAKLY ASCENDING'
    elif result[2]:
        return 'ASCENDING'
    elif all((result[1:4:2])):
        return 'WEAKLY DESCENDING'
    elif result[3]:
        return 'DESCENDING'
    return 'CONSTANT'
    
        
        
def lowercase_before_uppercase(s: str):
    if any((s.islower(), s.isupper())):
        return True
    good = True
    for sym in s:
        if not good and sym.islower():
            return False
        good = sym.islower()
    return True

# print(lowercase_before_uppercase('beeGEEK'))
# print(lowercase_before_uppercase('BEEgeek'))
# print(lowercase_before_uppercase('beegeek'))
# print(lowercase_before_uppercase('BEEGEEK'))
# print(lowercase_before_uppercase('b'))

def add_one(digits: list):
    plused = 1
    for index in range(len(digits) - 1, -1, -1):
        digits[index] += plused
        plused = digits[index] // 10
        digits[index] = digits[index] % 10
    if plused:
        digits.insert(0, plused)
    return digits
    

# print(add_one([9, 9]))

def drop_digit(digits: str):
    for i in range(len(digits) - 1):
        if int(digits[i]) < int(digits[i + 1]):
            return digits[:i] + digits[i+1:]
    return digits[:-1]

# print(drop_digit('22221'))
# print(drop_digit('11111'))
# print(drop_digit('9614'))
# print(drop_digit('10'))
# data = '34338522144589154889844536212862243681733937663642'
# print(drop_digit(data))
# print('4338522144589154889844536212862243681733937663642')

def adjacent_parity(nums: list):
    pairs = [0, 0]
    for num in nums:
        pairs[num % 2] += 1
    return any((
        any((not pairs[0], not pairs[1])),
        (abs(pairs[0] - pairs[1]) < 2),
    ))


# print(adjacent_parity([5, 2, 2, 7, 1]))         # 5, 2, 7, 2, 1
# print(adjacent_parity([1, 3, 2, 5]))
# print(adjacent_parity([1, 1, 1, 1, 1]))
# print(adjacent_parity([1, 3, 2, 4, 5]))  
# print(adjacent_parity([8, 2, 1, 3, 10, 9])) 

def is_possible_to_split(nums: list):
    half = len(nums) // 2
    nums = tuple(sorted(nums))
    good = True
    for i in range(half):
        good = nums[i] == nums[i + half]
        if not good:
            return good
    return good