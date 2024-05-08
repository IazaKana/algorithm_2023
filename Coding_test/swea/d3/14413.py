T = int(input())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS1(a, b):
    global answer
    test[a][b] = 1
    graph[a][b] = 0
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        if nx >= 0 and nx < N and ny >= 0 and ny < M and test[nx][ny] == 0:
            if graph[nx][ny] == '.' or graph[nx][ny] == '?':
                DFS2(nx, ny)
            else:
                answer = 'impossible'
                break

def DFS2(a, b):
    global answer
    test[a][b] = 1
    graph[a][b] = 0
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        if nx >= 0 and nx < N and ny >= 0 and ny < M and test[nx][ny] == 0:
            if graph[nx][ny] == '#' or graph[nx][ny] == '?':
                DFS1(nx, ny)
            else:
                answer = 'impossible'
                break


for i in range(T):
    N, M = map(int, input().split())
    graph = []
    test = [[0] * M for _ in range(N)]
    answer = 'possible'
    for j in range(N):
        graph.append(list(input()))

    for j in range(N):
        for k in range(M):
            if graph[j][k] == '#' or '.':
                if graph[j][k] == '#':
                    DFS1(j, k)
                    break
                elif graph[j][k] == '.':
                    DFS2(j, k)
                    break

    print('{}{} {}'.format('#', i+1, answer))


for i in range(T):
    N, M = map(int, input().split())
    graph = []
    test = [[0] * M for _ in range(N)]
    answer = 'possible'
    for j in range(N):
        graph.append(list(input()))

    for j in range(N):
        for k in range(M):
            if graph[j][k] == '#' or '.':
                if graph[j][k] == '#':
                    DFS1(j, k)
                    break
                elif graph[j][k] == '.':
                    DFS2(j, k)
                    break

    print('{}{} {}'.format('#', i+1, answer))