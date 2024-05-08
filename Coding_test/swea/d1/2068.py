n = int(input())
A = []

for i in range(n):
    lists = list(map(int, input().split()))
    A.append(max(lists))

for i in range(n):
    print('#' + str(i+1), A[i])