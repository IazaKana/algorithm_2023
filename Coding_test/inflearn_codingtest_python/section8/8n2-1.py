def solution(s):
    stack = []
    for i in s:
        if i == '#':
            if len(stack) > 0:
                stack.pop()
        else:
            stack.append(i)

    return "".join(stack)

print(solution("abc##ec#ab"))
print(solution("#abc##ec#ab"))
print(solution("kefd#ef##s##"))
print(solution("teac#cher##er"))
print(solution("englitk##shabcde##ff##ef##ashe####"))
print(solution("itistime####gold"))

#join함수 사용법