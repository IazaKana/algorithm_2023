import sys
from collections import Counter, deque
n, m = map(int, input().split())
A = deque()

for i in range(n):
    a = sys.stdin.readline().strip()
    if len(a) >= m:
        A.append(a)

B = Counter(A)
print(B)
print(B.items())
C = sorted(B.items(), key = lambda x : (-x[1], -len(x[0]), x[0]))

for i in C:
    print(i[0])

