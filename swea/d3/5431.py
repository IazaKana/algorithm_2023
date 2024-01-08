T = int(input())

for i in range(1, T+1):
    N, K = map(int, input().split())
    ch = [0] * (N+1)
    ch[0] = 1
    A = list(map(int, input().split()))
    for j in range(len(A)):
        ch[A[j]] = 1
    print('{}{}'.format('#', i), end=' ')
    for j in range(len(ch)):
        if ch[j] == 0:
            print(j, end=' ')
    print()