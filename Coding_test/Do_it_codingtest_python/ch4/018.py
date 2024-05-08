n = int(input())
A = [0] * n
sum = 0

for i in range(n):
    A[i] = int(input())

A.sort()

for i in range(n):
    sum += A[i] * (n-i)

print(sum)