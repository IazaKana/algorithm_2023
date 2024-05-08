import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

f_min = 100
f_max = 0
answer = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
board = []

def DFS(x, y, ch):
    ch[x][y] = 1
    for j in range(4):
        nx = x + dx[j]
        ny = y + dy[j]
        if nx >= 0 and nx < n and ny >= 0 and ny < n and board[nx][ny] - na > 0 and ch[nx][ny] == 0:
            DFS(nx, ny, ch)

n = int(input())            

for i in range(n):
    a = list(map(int, input().split()))
    min1 = min(a)
    max1 = max(a)
    #리스트 안의 최대 높이와 최소 높이를 반환 -> 최소 높이와 최대 높이사이에서 구하기 위함
    f_min = min(f_min, min1)
    f_max = max(f_max, max1)
    board.append(a)

#board에서 경우의 수만큼 높이의 값 빼기
for na in range(f_min, f_max+1):
    ch = [[0] * (n) for _ in range(n)]
    
    #DFS진입
    cnt = 0
    for x in range(n):
        for y in range(n):
            if board[x][y] - na > 0 and ch[x][y] == 0:
                DFS(x, y, ch)
                cnt += 1
    
    answer = max(cnt, answer)

print(answer)



