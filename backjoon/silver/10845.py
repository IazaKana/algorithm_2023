from collections import deque
import sys

N = int(input())
B = deque()

for i in range(N):
    A = sys.stdin.readline().split()
    if A[0] == 'push':
        B.append(A[1])
    elif A[0] == 'pop':
        if len(B) > 0:
            print(B.popleft())
        else:
            print(-1)
    elif A[0] == 'size':
        print(len(B))
    elif A[0] == 'empty':
        if len(B) == 0:
            print(1)
        else:
            print(0)
    elif A[0] == 'front':
        if len(B) == 0:
            print(-1)
        else:
            print(B[0])
    elif A[0] == 'back':
        if len(B) == 0:
            print(-1)
        else:
            print(B[-1])