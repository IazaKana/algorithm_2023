from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def BFS(x, y, A):
    count = 1
    Q = deque()
    Q.append([x, y])
    A[x][y] = 0
    while Q:
        n = len(Q)
        for _ in range(n):
            x, y = Q.popleft()
            for j in range(4):
                nx = x + dx[j]
                ny = y + dy[j]
                if (nx > 0 and nx < a+1 and ny > 0 and ny < b+1 and A[nx][ny] == 1):
                    if nx == a and ny == b:
                        count += 1
                        return count
                    Q.append([nx, ny])
                    A[nx][ny] = 0
                
        count += 1

a, b = map(int, input().split())

#지도완성
A = [[0] * (b+1) for _ in range(a+1)]
for i in range(1, a+1):
    c = str(input())
    for j in range(1, len(c)+1):
        A[i][j] = int(c[j-1])

print(BFS(1, 1, A))