n = int(input())


for i in range(n):
    A = [[0]] * 9
    answer = 1
    for j in range(9):
        A[j] = list(map(int, input().split()))
    for j in range(9):
        B = [0] * 9
        for k in range(9):
            if A[j][k] in B:
                answer = 0
            B[k] = A[j][k]
    #행탐색
    
    for k in range(9):
        B = [0] * 9
        for j in range(9):
            if A[j][k] in B:
                answer = 0
            B[j] = A[j][k]
    #열탐색

    for j in range(0, 7, 3):
        for k in range(0, 7, 3):
            B = [[0]*3] * 3
            for nx in range(3):
                for ny in range(3):
                    if A[j+nx][k+ny] in B:
                        answer = 0
                    B[nx][ny] = A[j+nx][k+ny]
    
    print('#' + str(i+1), answer)

#====================================


    
n = int(input())


for i in range(n):
    A = [[0]] * 9
    answer = 1
    for j in range(9):
        A[j] = list(map(int, input().split()))
    for j in range(9):
        B = [0] * 10
        for k in range(9):
            B[A[j][k]] += 1
            if B[A[j][k]] == 2:
                answer = 0

    #행탐색
    
    for k in range(9):
        B = [0] * 10
        for j in range(9):
            B[A[j][k]] += 1
            if B[A[j][k]] == 2:
                answer = 0
    #열탐색
    
    for j in range(0, 7, 3):
        for k in range(0, 7, 3):
            B = [0] * 10
            for nx in range(3):
                for ny in range(3):
                    B[A[j+nx][k+ny]] += 1
                    if B[A[j+nx][k+ny]] == 2:
                        answer = 0
    
    print('#' + str(i+1), answer)