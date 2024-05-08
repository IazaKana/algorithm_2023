for i in range(1, 11):
    N = int(input())
    A = list(map(int, input().split()))
    result = 0
    for j in range(2, N-2):
        c = max(A[j-2], A[j-1], A[j], A[j+1], A[j+2])
        if c == A[j]:
            check_num = max(A[j-2], A[j-1], A[j+1], A[j+2])
            result += c - check_num

    print('{}{} {}'.format('#', i, result))