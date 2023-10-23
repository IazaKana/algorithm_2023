from collections import deque
def BFS(home):
    Q = deque()
    Q.append(0)
    L = 0
    while Q:
        n = len(Q)
        # print(L, end = " : ")
        for i in range(n):
            v = Q.popleft()
            # print(v, end = " ")
            for nv in [v-1, v+1, v+5]:
                if nv == home:
                    return L + 1
                Q.append(nv)
        # print()
        L += 1

#시간복잡도 성능 최악

print(BFS(10))
print(BFS(14))
print(BFS(25))
print(BFS(24))
print(BFS(345))

def BFS(home):
    Q = deque()
    Q.append(0)
    ch = [0] * 10001
    L = 0
    ch[0] = 1
    for i in range(len(Q)):
        v = Q.popleft()
        if v == home:
            return L
        for nv in [v-1, v+1, v+5]:
            if nv >=0 and nv < 10001 and ch[nv] == 0:
                Q.append(nv)
                ch[nv] = 1
        L += 1
