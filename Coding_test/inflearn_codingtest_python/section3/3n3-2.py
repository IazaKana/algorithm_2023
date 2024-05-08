from collections import Counter

def solution(nums):
    nums = Counter(nums)
    result = 1000000
    for x in nums:
        if x == nums[x]:
            result = min(result, x)

    if result == 1000000:
        result = -1

    return result

print(solution([1, 2, 3, 1, 3, 3, 2, 4]))
print(solution([1, 2, 3, 3, 3, 2, 4, 5, 5, 5]))
print(solution([1, 1, 2, 5, 5, 5, 5, 5, 3, 3, 3, 3, 5]))
print(solution([7, 6, 7, 7, 8, 8, 8, 8, 7, 5, 7, 7, 7, 8, 8]))