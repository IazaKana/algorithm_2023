import math
n = int(input())
A = []
sum = []
k = 0

for i in range(n):
    lists = list(map(int, input().split()))
    A.append(lists)

for i in range(n):
    for j in range(10):
        k += A[i][j]
    sum.append(round(k / 10))
    k = 0

for i in range(1, n+1):
    print('#' + str(i), sum[i-1])