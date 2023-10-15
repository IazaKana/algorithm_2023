n = int(input())
A = [0] * (n+1)

for i in range(n+1):
    A[i] = 2 ** i

print(*A)