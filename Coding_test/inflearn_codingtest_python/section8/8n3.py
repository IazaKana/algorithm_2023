def solution(s):
    answer = ""
    stack = []
    n = len(s)
    for i in range(n):
        if s[i] == s[i-1]:
            stack.pop(s[i])
        else:
            stack.append(s[i])
            
    return "".join(stack)

print(solution("acbbcaa"))
print(solution("bacccaba"))
print(solution("aabaababbaa"))
print(solution("bcaacccbaabccabbaa"))
print(solution("cacaabbc"))

def solution(s):
    stack = []
    for x in s:
        if stack and stack[-1] == x: # stack이 참이라면 -> stack에 무언가가 있음
            stack.pop()
        else:
            stack.append(x)
            
    return "".join(stack)