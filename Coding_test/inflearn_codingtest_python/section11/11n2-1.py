cnt = 0
def DFS(v, graph, ch, n):
    global cnt
    ch[v] = 1
    cnt += 1
    if len(graph[v]) == 0:
        pass
    elif graph[v]:
        for i in graph[v]:
            if ch[i] == 0:
                DFS(i, graph, ch, n)



def solution(n, edges):
    global cnt
    ch = [0] * (n+1)
    graph = [[] for _ in range(n+1)]
    for [a, b] in edges:
        graph[a].append(b)
        graph[b].append(a)
    for i in range(1, n+1):
        DFS(i, graph, ch, n+1)