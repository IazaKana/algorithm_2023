def solution(nums):
    sum = 0
    for i in range(len(nums)):
        if nums[i] == '(':
            sum += 1
        elif nums[i] == ')':
            sum -= 1
            if sum == -1:
                return "NO"
            
    return "YES" if sum == 0 else "NO"

print(solution("((()))()"))
print(solution("(()(()"))
print(solution("()())"))
print(solution("())("))
print(solution("((())))()("))

def solution(s):
    answer = "YES"
    stack = []
    for x in s:
        if x == ')':
            if len(stack) == 0:
                return "NO"
            stack.pop()
        else:
            stack.append(x)

    if len(stack) > 0:
        return "NO"

    return answer