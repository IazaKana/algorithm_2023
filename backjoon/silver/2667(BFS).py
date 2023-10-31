from collections import deque

n = int(input())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def BFS(x, y, A):
    Q = deque()
    Q.append([x, y])
    A[x][y] = 0
    count2 = 1
    while Q:
        c = len(Q)
        for i in range(c):
            x, y = Q.popleft()
            for j in range(4):
                nx = x + dx[j]
                ny = y + dy[j]
                if nx >= 0 and nx < n and ny >= 0 and ny < n and A[nx][ny] == 1:
                    Q.append([nx, ny])
                    A[nx][ny] = 0
                    count2 += 1
    B.append(count2)


A = []
for i in range(n):
    a = list(map(int, input()))
    A.append(a)

B = []
count1 = 0
for i in range(n):
    for j in range(n):
        if A[i][j] == 1:
            count1 += 1
            BFS(i, j, A)

B.sort()
print(count1)
for i in B:
    print(i)