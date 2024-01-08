import math
N = 10 ** 6
A = [0] * (N + 1)

for i in range(2, N+1):
    A[i] = i

for i in range(2, int(math.sqrt(N))+1):
    if A[i] == 0:
        continue
    for j in range(i+i, N+1, i):
        A[j] = 0

for i in range(N+1):
    if A[i] != 0:
        print(A[i], end=' ')