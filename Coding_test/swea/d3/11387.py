M = int(input())

for i in range(1, M+1):
    D, L, N = map(int, input().split())
    sum = 0
    for j in range(N):
        a = D + (D * j * L) // 100
        sum += a
    print('{}{} {}'.format('#', i, sum))