from collections import deque
T = int(input())

for i in range(1, T+1):
    n = int(input())
    result = deque()
    card = list(input().split())
    if len(card) % 2 == 0:
        A = card[:n//2]
        B = card[n//2:]
        for j in range(n // 2):
            result.append(A[j])
            result.append(B[j])
    else:
        A = card[:n//2+1]
        B = card[n//2+1:]
        for j in range(n // 2 + 1):
            result.append(A[j])
            if j != n//2:
                result.append(B[j])

    print('{}{}'.format('#', i), end=' ')
    print(*result)