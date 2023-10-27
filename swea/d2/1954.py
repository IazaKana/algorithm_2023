n = int(input())

def DFS(m, A):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    x = y = 0
    d = 1
    A[0][0] = 1
    for i in range(2, m*m+1):
        x += dx[d]
        y += dy[d]
        if (x >= 0 and x < m and y >= 0 and y < m and A[x][y] != 0) or x < 0 or x >= m or y < 0 or y >=m:
            x -= dx[d]
            y -= dy[d]
            d = (d + 1) % 4
            x += dx[d]
            y += dy[d]
        A[x][y] = i
    return A
    
for i in range(n):
    m = int(input())
    A = [[0 for _ in range(m)] for _ in range(m)]
    DFS(m, A)
    print('{}{}'.format('#', i+1))
    for j in range(m):
        print(*A[j])

#DFS방향전환 문제