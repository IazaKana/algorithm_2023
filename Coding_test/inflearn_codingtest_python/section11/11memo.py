#1.무방향 그래프
n = 5
edge = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 4]]
graph = [[0] * (n+1) for _ in range(n+1)]
for [a, b] in edge:
    graph[a][b] = 1
    graph[b][a] = 1

#2.방향 그래프
n = 5
edge = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 4]]
graph = [[0] * (n+1) for _ in range(n+1)]
for [a, b] in edge:
    graph[a][b] = 1

#3. 가중치 방향 그래프
n = 5
edge = [[1, 2, 2], [1, 3, 4], [2, 4, 5], [2, 5, 5], [3, 4, 5]]
graph = [[0] * (n+1) for _ in range(n+1)]
for [a, b, c] in edge:
    graph[a][b] = c


# ==============================================================


n = 5
edge = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 4]]
graph = [[] for _ in range(n+1)]
for [a, b] in range(n+1):
    graph[a].append(b)
    graph[b].append(a)

n = 5
edge = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 4]]
graph = [[] for _ in range(n+1)]
for [a, b] in range(n+1):
    graph[a].append(b)

n = 5
edge = [[1, 2, 2], [1, 3, 4], [2, 4, 5], [2, 5, 5], [3, 4, 5]]
graph = [[] for _ in range(n+1)]
for [a, b, c] in edge:
    graph[a].append([b, c])