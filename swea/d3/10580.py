TC = int(input())

for i in range(1, TC+1):
    N = int(input())
    A = list()
    for j in range(N):
        a, b = map(int, input().split())
        A.append([a, b])
    A.sort()
    count = 0
    for j in range(N-1):
        for k in range(j+1, N):
            if A[j][1] > A[k][1]:
                count += 1
    print('{}{} {}'.format('#', i, count))