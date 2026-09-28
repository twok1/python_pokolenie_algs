def linear_search(nums, target, reverse=False):
    search = range(len(nums)) if not reverse else range(len(nums)-1, -1, -1)
    for i in search:
        if nums[i] == target:
            return i
    return -1
        
        
def equal(n):
    for i in range(len(n)):
        if i == n[i]:
            return i
    return -1

def search_insert_position(nums: list, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
        elif nums[i] > target:
            return i
    return len(nums)

def count_numbers(n, k):
    res = 0
    for i in range(1, n+1):
        if i - sum(int(k) for k in str(i)) >= k:
            res += 1
    return res

def nine_divisors(n):
    result = 0
    for i in range(1, n + 1):
        divisors = 0
        for k in range(1, i+1):
            if i // k * k == i:
                divisors += 1
        if divisors == 9:
            result += 1
    return result


def find_number(nums):
    for i in range(0, len(nums) - 1, 2):
        if nums[i] != nums[i+1]:
            return nums[i]
    return nums[-1]


def doubling_the_value(nums, value):
    for i in nums:
        if i == value:
            value *= 2
    return value


def count_occurrences(nums, target, start, end):
    result = 0
    i = start
    while i < end:
        if nums[i] == target:
            result += 1
        i += 1
    return result


def elements_in_the_range(nums, start, end):
    return not bool(set(set(range(start, end+1))).difference(nums))


def check_letters(s: str):
    result = ['0'] * 26
    for i in s.lower():
        if 97 <= ord(i) <= 126:
            result[ord(i) - 97] = '1'
    return ''.join(result)


def find_peaks(nums):
    result = 0
    for i in range(1, len(nums) - 1):
        if nums[i-1] < nums[i] > nums[i+1]:
            result += 1
    return result


def kth_occurrence(nums, target, k):
    for num, sym in enumerate(nums):
        if sym == target:
            k -= 1
        if not k:
            return num
    return -1


def find_sum_indexes(nums, value):
    i = 0
    while i < len(nums):
        k = i
        sums = nums[k]
        while sums <= value:
            if sums == value:
                return (i, k)
            k += 1
            sums += nums[k]
            if sums > value:
                break
        i += 1
    return -1


print(find_sum_indexes([1, 5, 1, 2, 4, 7, 6], 7))      # подсписок [1, 5, 1]
print(find_sum_indexes([8, 7, 3, 4, 5, 33, 14], 7))    # подсписок [7]
print(find_sum_indexes([1], 2))                        # подходящего подсписка нет



