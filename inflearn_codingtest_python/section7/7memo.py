def solution(nums, weight):
    left = 0
    right = len(nums)
    while left < right:
        mid = (left + right) // 2
        if weight > nums[mid]:
            left = mid + 1
        else:
            right = mid
    return -1 if right == len(nums) else right