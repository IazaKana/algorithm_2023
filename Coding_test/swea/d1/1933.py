n = int(input())
A = []

for i in range(1, n+1):
    if n % i == 0:
        A.append(i)

print(*A)