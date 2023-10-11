n = int(input())
A = []
sum = []
k = 0

for i in range(1, n+1):
    lists = list(map(int, input().split()))
    A.append(lists)

for i in range(n):
    for j in range(10):
        if A[i][j] % 2 == 1:
            k += A[i][j]
    sum.append(k)
    k = 0

for i in range(1, n+1):
    print('#' + str(i), sum[i-1])

# 여러 수 한번에 입력받는법