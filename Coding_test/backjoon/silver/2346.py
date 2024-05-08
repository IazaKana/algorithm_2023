from collections import deque
N = int(input())
A = deque(enumerate(map(int, input().split()), start=1))

for i in range(N):
    p = A.popleft()
    print(p[0], end = ' ')
    if p[1] > 0:
        A.rotate(-(p[1]-1))
    else:
        A.rotate(-p[1])