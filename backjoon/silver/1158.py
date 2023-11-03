N, K = map(int, input().split())
num = 0
answer = []
A = list()
for i in range(1, N+1):
    A.append(i)

for i in range(N):
    num += (K-1)
    if num >= len(A):
        num %= len(A)
    answer.append(A[num])
    A.pop(num)

print('<', end='')
print(*answer, sep=', ', end='')
print('>')