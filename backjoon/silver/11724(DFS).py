import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M = map(int, input().split())

def DFS(v, board, ch):
    ch[v] = 1
    for nv in board[v]:
        if ch[nv] == 0:
            DFS(nv, board, ch)


board = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    board[a].append(b)
    board[b].append(a)

ch = [0] * (N+1)
cnt = 0

for i in range(1, N+1):
    if board[i] and ch[i] == 0:
        DFS(i, board, ch)
        cnt += 1

print(cnt)

#======================================
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
N, M = map(int, input().split())
ch = [0] * (N+1)
graph = [[] for _ in range(N+1)]

def DFS(num):
    ch[num] = 1
    for k in graph[num]:
        if ch[k] == 0:
            DFS(k)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0

for i in range(1, N+1):
    if ch[i] == 0:
        count += 1
        DFS(i)

print(count)

#visited로 true, false로 해보기

