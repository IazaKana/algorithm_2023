from collections import deque

def DFS(V, graph, ch):
    print(V, end=' ')
    ch[V] = 1
    for i in graph[V]:
        if ch[i] == 0:
            DFS(i, graph, ch)

def BFS(V, graph, ch):
    Q = deque()
    Q.append(V)
    ch[V] = 1
    while Q:
        n = len(Q)
        for i in range(n):
            v = Q.popleft()
            print(v, end = ' ')
            for nv in graph[v]:
                if ch[nv] == 0:
                    Q.append(nv)
                    ch[nv] = 1



N, M, V = map(int, input().split())
A = []
for i in range(M):
    a, b = map(int, input().split())
    A.append([a, b])
ch = [0] * (N + 1)
graph = [[] for _ in range(N+1)]
for [a, b] in A:
    graph[a].append(b)
    graph[b].append(a)
for i in graph:
    i.sort()

DFS(V, graph, ch)
print()
ch = [0] * (N + 1)
BFS(V, graph, ch)
