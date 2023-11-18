T = int(input())

for i in range(1, T+1):
    A, B, C, D = map(int, input().split())
    if min(D, B) - max(A, C) < 0:
        answer = 0
    else:
        answer = min(D, B) - max(A, C)
    print('{}{} {}'.format('#', i, answer))