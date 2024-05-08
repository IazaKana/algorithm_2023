def solution(nums):
    stack = []
    count = 0
    for i in nums:
        if len(stack) >= 2 and stack[-1] == 2 and stack[-2] == 1 and i == 1:
            stack.pop()
            stack.pop()
            count += 1
        else:
            stack.append(i)
        
    return count

print(solution([1, 1, 1, 2, 1, 1, 2, 1, 2, 1]))
print(solution([2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 2, 1]))
print(solution([1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1]))
print(solution([2, 1, 1, 1, 2, 1, 2]))
print(solution([1, 1, 1, 1, 1, 1, 1]))