from collections import deque
N = input()
stack = []
A = deque(map(int, input().split()))
answer = 'Nice'
test = 1

while len(A) != 0 or len(stack) != 0:
    if test in A:
        a = A.popleft()
        while a != test:
            stack.append(a)
            a = A.popleft()
    elif test in stack:
        if stack[-1] == test:
            stack.pop()
        else:
            answer = 'Sad'
            break
    test += 1

print(answer)


# while len(A) == 0 and len(stack) == 0:
#     if i+1 in A:
#         while A[i] == i+1:
#             stack.append(A.pop(i+1))

#     elif i+1 in stack:
#         if stack[-1] != i+1:
#             answer = 'No'
#     i += 1
        
        