TC = int(input())

for i in range(1, TC+1):
    N = int(input())
    sum = 0
    for _ in range(N):
        p, x = map(float, input().split())
        sum += p * x
    print('{}{} {}'.format('#', i, '{:6f}'.format(sum)))