N = int(input())

for i in range(1, N+1):
    A = list(map(int, input().split()))
    ch = [0] * A[0]
    B_list = [0 for _ in range(101)]
    O_list = [0 for _ in range(101)]
    #케이스에 따라 복도에 버튼이 어디있는지 리스트 형식으로 정렬
    # for j in range(1, A[0]*2+1, 2):
    #     if A[j] == 'B':
    #         B_list[A[j+1]] = 1
    #     elif A[j] == 'O':
    #         O_list[A[j+1]] = 1
    count = 0
    B_num = 0
    O_num = 0
    k = 1
    distance_B = 1
    distance_O = 1
    check_str = ''
    while True:
        check_str = A[k]
        if A[k] == 'B':
            count += abs(distance_B - A[k+1])
            distance_B = A[k+1]
            if A[k+2] != 'B':
                if abs(dsitance_B - A[k+1]) > abs:


        elif A[k] == 'O':
            count += abs(distance_O - A[k + 1])
            distance_O = A[k+1]






