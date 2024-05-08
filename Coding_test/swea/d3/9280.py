from collections import deque
TC = int(input())

for i in range(1, TC+1):
    n, m = map(int, input().split())
    stage = list()
    check_list = [0 for _ in range(n)]
    car = [0 for _ in range(m+1)]
    sum = 0
    dae = deque()
    for j in range(n):
        stage.append(int(input()))

    for j in range(1, m+1):
        car[j] = (int(input()))

    for j in range(2 * m):
        a = int(input())
        if a > 0:
            for k in range(n):
                if check_list[k] == 0:
                    check_list[k] = a
                    sum += stage[k] * car[a]
                    break
                if k == n - 1:
                    dae.append(a)
        elif a < 0:
            for k in range(n):
                if check_list[k] == -a:
                    check_list[k] = 0
                    if len(dae) > 0:
                        b = dae.popleft()
                        check_list[k] = b
                        sum += stage[k] * car[b]


    print('{}{} {}'.format('#', i, sum))
