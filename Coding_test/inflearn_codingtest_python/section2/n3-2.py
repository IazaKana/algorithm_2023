def solution(nums):
    max_len = 0
    pre_len = 0
    for x in nums:
        if x == 1:
            pre_len += 1
            if pre_len > max_len:
                max_len = pre_len
        else:
            pre_len = 0
    
    return max_len

print(solution([1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1]))
print(solution([0, 0, 1, 0, 1, 0, 0]))
print(solution([1, 1, 1, 1, 1]))
print(solution([1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1]))