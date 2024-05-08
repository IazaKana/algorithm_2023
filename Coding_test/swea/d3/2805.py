T = int(input())

for i in range(1, T+1):
    #N은 무조건 홀수
    N = int(input())
    graph = []
    result = 0
    for j in range(N):
        graph.append(list(input()))
    u = 0

    for j in range(N):
        for k in range(N):
            graph[j][k] = int(graph[j][k])

    for j in range(N//2 + 1):
        result += sum(graph[j][N//2 - j:N//2 + 1 + j])

    for j in range(N//2-1, -1, -1):
        u += 1
        result += sum(graph[N//2 + u][N//2 - j:N//2 + 1 + j])

    print('{}{} {}'.format('#', i, result))

#========================참고코드=====================
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    a = [list(map(int, input())) for _ in range(N)]
    ans = 0  # output 변수

    # s: 시작포인트, e: 끝포인트
    s, e = N // 2, N // 2
    for i in range(N):
        for j in range(s, e+1):
            ans += a[i][j]
        # 행의 인덱스가 mid 전까지는 s-e 간격 늘리고 mid 이후로는 간격 줄임
        if i < N // 2:
            s -= 1
            e += 1
        else:
            s += 1
            e -= 1

    print("#{} {}".format(tc, ans))