def solution(nums):
    a = 0
    answer = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            a += 1
            if i == len(nums)-1:
                if a > answer:
                    answer = a

        elif nums[i] == 0:
            if a > answer:
                answer = a
            a = 0
    return answer
                
print(solution([1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1]))
print(solution([0, 0, 1, 0, 1, 0, 0]))
print(solution([1, 1, 1, 1, 1]))
print(solution([1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1]))