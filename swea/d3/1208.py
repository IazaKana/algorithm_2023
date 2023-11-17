for i in range(1, 11):
    num = int(input())
    A = list(map(int, input().split()))
    for j in range(num):
        max_num = max(A)
        min_num = min(A)
        max_idx = A.index(max_num)
        min_idx = A.index(min_num)
        A[max_idx] -= 1
        A[min_idx] += 1
    result = max(A) - min(A)
    print('{}{} {}'.format('#', i, result))

