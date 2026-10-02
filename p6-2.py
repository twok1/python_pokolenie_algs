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

        