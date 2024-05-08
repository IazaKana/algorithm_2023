N = int(input())

for i in range(1, N+1):
    M = int(input())
    A = list(map(int, input().split()))
    count = 0
    for j in range(1, M-1):
        test = list()
        test.append(A[j-1])
        test.append(A[j])
        test.append(A[j+1])
        test.remove(max(test))
        test.remove(min(test))
        if A[j] == test[0]:
            count += 1
    print('{}{} {}'.format('#', i, count))