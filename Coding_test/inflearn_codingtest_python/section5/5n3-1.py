def solution(nums, target):
    answer = [0]*2
    nums.sort()
    left = 0
    right = len(nums) - 1
    while left < right:
        sumN = nums[left] + nums[right]
        if sumN == target:
            return [nums[left], nums[right]]
        if sumN < target:
            left += 1
        else:
            right -= 1
            
    return answer