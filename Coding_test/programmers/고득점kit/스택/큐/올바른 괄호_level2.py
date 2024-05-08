def solution(s):
    answer = True
    
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) == 0:
                stack.append(i)
            elif stack[-1] == '(':
                stack.pop()
    
    if stack:
        answer = False

    return answer