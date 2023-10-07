n, m = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

for i in range(n):
    if A[i] == m:
        print(i+1)
        break