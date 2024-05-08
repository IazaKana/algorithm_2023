from collections import deque
n = int(input())

a = deque()

for i in range(n):
    c = int(input())
    if c != 0:
        a.append(c)
    elif c == 0:
        