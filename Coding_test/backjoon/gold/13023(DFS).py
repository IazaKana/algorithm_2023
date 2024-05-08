import sys
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N)]
answer = 0
ch = [0] * (N)

def DFS(num, count):
    global answer
    if count == 5:
        answer = 1
        return
    ch[num] = 1
    for k in graph[num]:
        if ch[k] == 0:
            DFS(k, count+1)
    ch[num] = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N):
    DFS(i, 1)
    if answer == 1:
        break

print(answer)