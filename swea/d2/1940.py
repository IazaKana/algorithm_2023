n = int(input())

for i in range(n):
    N = int(input())
    v = 0
    A = [0] * 3
    answer = 0
    for j in range(N):
        m = list(map(int, input().split()))
        if m[0] == 1:
            v += m[1]
        elif m[0] == 2:
            if v < m[1]:
                v = 0
            else:
             v -= m[1]
        answer += v
    print('{}{} {}'.format('#', i+1, answer))