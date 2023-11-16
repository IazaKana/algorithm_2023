T = int(input())

for i in range(1, T+1):
    N, L = map(int, input().split())
    rate = []
    cal_check = 0
    sum = 0

    for j in range(N):
        a, b = map(int, input().split())
        c = a / b
        rate.append([c, b, a])

    rate.sort(key = lambda v : (-v[0], v[1]))
    print(rate)

    for j in rate:
        if cal_check + j[1] <= L:
            sum += j[2]
            cal_check += j[1]

    print('{}{} {}'.format('#', i, sum))

#========================================

t = int(input())


