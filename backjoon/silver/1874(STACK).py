import sys

n = int(input())
stack = []
count = 0
answer = []
check = 0


for i in range(n):
    a = int(sys.stdin.readline())
    #스택의 수와 입력받은 값의 차이
    if a < count:
        if a == stack[-1]:
            stack.pop()
            answer.append('-')
        else:
            check = 1
            break

    elif a > count:
        for j in range(a - count):
            count += 1
            answer.append('+')
            stack.append(count)
        stack.pop()
        answer.append('-')

if check == 0:
    for k in answer:
        print(k)
elif check == 1:
    print('NO')