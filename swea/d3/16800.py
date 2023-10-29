n = int(input())

for i in range(1, n+1):
    m = int(input())
    A = []
    for j in range(1, m+1):
        if m % j == 0:
            a = j
            b = m // j
            A.append([a, b])
    print(A)

    # answer = m
    # for a, b in A:
    #     n = a + b - 2
    #     answer = min(answer, n)
            # sub = abs(b-a)
            # if sub < check:
            #     check = sub
            #     answer = b+a-2
    # print('{}{} {}'.format('#', i, answer))

    #math모듈 사용? 시간복잡도 초과