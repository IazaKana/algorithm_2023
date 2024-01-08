cnt = 0
answer = 0

def solution(land):
    global cnt
    global answer
    width = len(land[0])
    height = len(land)
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    def DFS(j, i):
        global cnt
        cnt += 1
        ch[j][i] = 2
        for x in range(4):
            nx = j + dx[x]
            ny = i + dy[x]
            if nx >= 0 and nx < height and ny >= 0 and ny < width and land[nx][ny] == 1 and ch[nx][ny] != 2:
                DFS(nx, ny)

    for i in range(width):
        ch = [[0] * width for _ in range(height)]
        cnt = 0
        for j in range(height):
            if ch[j][i] == 0 and land[j][i] == 1:
                DFS(j, i)
        answer = max(answer, cnt)
    
    return answer


print(solution([[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]))