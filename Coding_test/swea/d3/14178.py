T = int(input())

for i in range(T):
    N, D = map(int, input().split())
    if N % ((D * 2) + 1) == 0:
        answer = N // ((D * 2) + 1)
    else:
        answer = N // ((D * 2) + 1) + 1
    print('{}{} {}'.format('#', i+1, answer))