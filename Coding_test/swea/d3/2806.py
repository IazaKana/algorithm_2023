T = int(input())

def DFS(x, y, arr):
    global count
    arr[x][y] = 1
    if x == N-1:
        count += 1
    for i in range(N):
        #행삭제
        if arr[x][i] == 0:
            arr[x][i] = 1
        #열삭제
        if arr[i][y] == 0:
            arr[i][y] = 1
        #사선삭제
    for j in range(1, N):
        nx = x + j
        ny = y + j
        if nx >= 0 and nx < N and ny >= 0 and ny < N and arr[nx][ny] == 0:
            arr[nx][ny] = 1

    for j in range(1, N):
        nx = x - j
        ny = y - j
        if nx >= 0 and nx < N and ny >= 0 and ny < N and arr[nx][ny] == 0:
            arr[nx][ny] = 1

    for j in range(1, N):
        nx = x + j
        ny = y - j
        if nx >= 0 and nx < N and ny >= 0 and ny < N and arr[nx][ny] == 0:
            arr[nx][ny] = 1

    for j in range(1, N):
        nx = x - j
        ny = y + j
        if nx >= 0 and nx < N and ny >= 0 and ny < N and arr[nx][ny] == 0:
            arr[nx][ny] = 1

    for i in range(N):
        if x+1 < N and x+1 >= 0 and y+i < N and y+i >= 0 and arr[x+1][y+i] == 0:
            DFS(x+1, y+i, arr)

for i in range(1, T+1):
    count = 0
    N = int(input())
    graph = [[0 for _ in range(N)] for _ in range(N)]
    for j in range(N):
        DFS(0, j, graph)
    print('{}{} {}'.format('#', i, count))