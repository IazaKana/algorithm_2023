T = int(input())

for i in range(1, T+1):
    A = list(input())
    A = list(map(int, A))
    min_num = 10
    max_num = 0
    result_min = 0
    result_max = 0
    #최솟값의 인덱스 구하기

    if len(A) == 1 and A[0] == 0:
        result_min = 0
        result_max = 0
    else:
        for j in range(len(A)):
            if A[j] <= min_num and A[j] > 0:
                min_num = A[j]
                min_index = j
        #최댓값의 인덱스 구하기
        for j in range(len(A)):
            if A[j] >= max_num:
                max_num = A[j]
                max_index = j


        #최솟값 구하기
        if min_index == 0:
            for k in range(len(A)):
                result_min += 10 ** (len(A)-1-k) * A[k]

        elif min

        else:
            for k in range(len(A)):
                if k == 0:
                    result_min += 10 ** (len(A)-1-k) * A[min_index]
                elif k == min_index:
                    result_min += 10 ** (len(A) - 1 - k) * A[0]
                else:
                    result_min += 10 ** (len(A)-1-k) * A[k]

        #최댓값 구하기
        if max_index == 0:
            for k in range(len(A)):
                result_max += 10 ** (len(A) - 1 - k) * A[k]
        else:
            for k in range(len(A)):
                if k == 0:
                    result_max += 10 ** (len(A) - 1 - k) * A[max_index]
                elif k == max_index:
                    result_max += 10 ** (len(A) - 1 - k) * A[0]
                else:
                    result_max += 10 ** (len(A) - 1 - k) * A[k]




    print('{}{} {} {}'.format('#', i, result_min, result_max))