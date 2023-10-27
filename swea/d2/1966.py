n = int(input())

for i in range(n):
    a = int(input())
    A = list(map(int, input().split()))
    A.sort()
    print('#' + str(i+1), end=' ')
    print(*A)