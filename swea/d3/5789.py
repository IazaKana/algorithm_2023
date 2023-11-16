T = int(input())

for i in range(1, T+1):
    N, Q = map(int, input().split())
    box = ['0' for _ in range(N)]
    for j in range(Q):
        L, R = map(int, input().split())
        for k in range(j, j+R-L+1):
            box[k] = str(j+1)

    print('#{}'.format(i),' '.join(box))