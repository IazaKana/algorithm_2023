from itertools import combinations
T = int(input())

for i in range(1, T+1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    result = 0
    for j in range(1, len(A)+1):
        for k in combinations(A, j):
            if sum(k) == K:
                result += 1

    print('{}{} {}'.format('#', i, result))