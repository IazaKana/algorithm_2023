dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(x, y, board):
    board[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < 5 and ny >= 0 and ny < 5 and board[nx][ny] == 1:
            DFS(nx, ny, board)

def solution(board):
    answer = 0
    for i in range(5):
        for j in range(5):
            if board[i][j] == 1:
                DFS(i, j, board)
                answer += 1
    return answer