for i in range(1):
    T = int(input())
    graph = []
    max_width = 0
    max_height = 0
    for j in range(100):
        graph.append(list(map(int, input().split())))

    #가로 최대합
    for j in range(100):
        max_width = max(max_width, sum(graph[j]))

    for j in range(100):
        a = 0
        for k in range(100):
            a += graph[k][j]
        max_height = (max_height, a)

    diagonal1 = 0
    for j in range(100):
        diagonal1 += graph[j][j]

    diagonal2 = 0
    for j in range(100):
        diagonal2 += graph[j][99-j]

    result = max(max_width, max_height, diagonal1, diagonal2)

    print('{}{} {}'.format('#', T, result))