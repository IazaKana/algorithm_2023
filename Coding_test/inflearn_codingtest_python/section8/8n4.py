def solution(nums):
    answer = 0
    stack = []
    for x in nums:
        if stack[-2] == 1 and stack[-1] == 2 and x == 1 and len(stack) >= 2:
            stack.pop()
            stack.pop()
            answer += 1
        else:
            stack.append(x)

        
    return answer
    
#stack[-2] 조건에 -2를 먼저하면 오류?

print(solution([1, 1, 1, 2, 1, 1, 2, 1, 2, 1]))
print(solution([2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 2, 1]))
print(solution([1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1]))
print(solution([2, 1, 1, 1, 2, 1, 2]))
print(solution([1, 1, 1, 1, 1, 1, 1]))

def solution(nums):
    answer = 0
    stack = []
    for x in nums:
        if x == 1 and len(stack) >= 2 and stack[-1] == 2 and stack[-2] == 1:
            answer += 1
            stack.pop()
            stack.pop()
        else:
            stack.append(x)
    
    return answer