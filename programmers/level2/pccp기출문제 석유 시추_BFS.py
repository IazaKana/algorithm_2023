from collections import deque

def solution(land):
    global cnt
    global answer
    cnt = 0
    answer = 0
    width = len(land[0])
    height = len(land)
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    def BFS(j, i):
        global cnt
        Q = deque()
        Q.append((j, i))
        ch[j][i] = 2
        cnt += 1
        while Q:
            n = len(Q)
            for x in range(n):
                m, n = Q.popleft()
                for k in range(4):
                    nx = m + dx[k]
                    ny = n + dy[k]
                    if nx >= 0 and nx < height and ny >= 0 and ny < width and land[nx][ny] == 1 and ch[nx][ny] != 2:
                        Q.append((nx, ny))
                        ch[nx][ny] = 2
                        cnt += 1

    for i in range(width):
        ch = [[0] * width for _ in range(height)]
        cnt = 0
        for j in range(height):
            if ch[j][i] == 0 and land[j][i] == 1:
                BFS(j, i)
        answer = max(answer, cnt)
    
    return answer

print(solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]))