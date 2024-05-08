def solution(s):
    answer = "YES"
    n = len(s)
    n1 = 0
    n2 = 0

    if s[0] == ')' or s[n-1] == '(':
        answer = "NO"

    for i in range(n):
        if s[i] == '(':
            if n1 != n2:
                answer = "NO"
                break
            n1 += 1
        elif s[i] == ')':
            n2 += 1
    
    return answer


print(solution("((()))()"))
print(solution("(()(()"))
print(solution("()())"))
print(solution("())("))
print(solution("((())))()("))

#괄호 문제는 거의 스택을 이용해서 푸는 문제(짝을 이루는 문제)

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