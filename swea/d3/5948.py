from itertools import combinations
T = int(input())

for i in range(1, T+1):
    A = list(map(int, input().split()))
    B = list(combinations(A, 3))
    C = list()
    for j in range(len(B)):
        C.append(B[j][0] + B[j][1] + B[j][2])
    C = set(C)
    C = list(C)
    C.sort(reverse = True)

    print('{}{} {}'.format('#', i, C[4]))