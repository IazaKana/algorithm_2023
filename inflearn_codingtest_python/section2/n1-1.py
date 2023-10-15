def solution(nums):
    answer = 0
    a = min(nums)
    for i in range(len(nums)):
        if nums[i] == a:
            answer = i
    return answer



print(solution([7, 10, 5, 3, 2, 15, 19]))