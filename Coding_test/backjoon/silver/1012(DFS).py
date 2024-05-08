import sys
sys.setrecursionlimit(10000)
n = int(input())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(x, y, board, count):
    board[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < N and ny >=0 and ny < M and board[nx][ny] == 1:
            DFS(nx, ny, board, count)



for i in range(n):
    count = 0
    M, N, K = map(int, input().split())
    board = [[0] * M for _ in range(N)]
    for j in range(K):
        a, b = map(int, input().split())
        board[b][a] = 1
    for j in range(N):
        for k in range(M):
            if board[j][k] == 1:
                DFS(j, k, board, count)
                count += 1
    print(count)

