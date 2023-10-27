n = int(input())

for i in range(n):
    m = int(input())
    A = [[0]]*m
    for j in range(m):
        A[j] = (list(map(int, input().split())))
    
    #90도
    B = [[0] * m for _ in range(m)]
    for j in range(m):
        for k in range(m):
            B[j][k] = A[m-1-k][j]
    print(B)
    
    # #180도
    C = [[0] * m for _ in range(m)]
    for j in range(m):
        for k in range(m):
            C[j][k] = B[m-1-k][j]

    # #270도
    # D = [[0 for _ in range(m)] for _ in range(m)]
    D = [[0] * m for _ in range(m)]
    for j in range(m):
        for k in range(m):
            D[j][k] = C[m-1-k][j]

    print('#' + str(i+1))
    for j in range(m):
        print(''.join(map(str, B[j])), end=' ')
        print(''.join(map(str, C[j])), end=' ')
        print(''.join(map(str, D[j])), end=' ')
        print()
    

#이중배열 선언시 얕은 복사 주의, for문으로 선언하는거 익숙해지기
#join함수 숙지