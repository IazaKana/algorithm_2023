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

for test_case in range(1, t + 1):
    n, l = map(int, input().split())

    ingredient = []
    for _ in range(n):
        score, cal = map(int, input().split())
        ingredient.append((score, cal))

    result = [[] for _ in range(n)]

    for i in range(n):
        result[i].append(ingredient[i])
        for j in range(0, i):
            for k in result[j]:
                score, cal = k
                if cal + ingredient[i][1] <= l:
                    result[i].append((score + ingredient[i][0], cal + ingredient[i][1]))

    max_score = 0
    for i in range(n):
        for j in result[i]:
            score, cal = j
            if score > max_score:
                max_score = score




