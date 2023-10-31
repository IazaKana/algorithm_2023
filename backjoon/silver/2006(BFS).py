from collections import deque

n = int(input())
m = int(input())

def BFS(a, ch, A):
    Q = deque()
    Q.append(a)
    count = 0
    while Q:
        c = len(Q)
        for j in range(c):
            v = Q.popleft()
            ch[v] = 1
            for nv in A[v]:
                if ch[nv] == 0:
                    ch[nv] = 1
                    Q.append(nv)
                    count += 1

    print(count)



B = []
for i in range(m):
    a, b = map(int, input().split())
    B.append([a, b])

A = [[] for _ in range(n+1)]
for [x, y] in B:
    A[x].append(y)
    A[y].append(x)
ch = [0] * (n+1)

BFS(1, ch, A)

