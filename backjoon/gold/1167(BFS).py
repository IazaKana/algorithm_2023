from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
graph = [[] for _ in range(N+1)]
answer = 0

def DFS(num):
    Q = deque()
    Q.append(num)
    ch = [0] * (N+1)
    distance_list = [0] * (N+1)
    ch[num] = 1
    while Q:
        n = len(Q)
        for i in range(n):
            v = Q.popleft()
            for nv in graph[v]:
                if ch[nv[0]] == 0:
                    Q.append(nv[0])
                    distance_list[nv[0]] += distance_list[v] + nv[1]
                    ch[nv[0]] = 1
    max_distance = max(distance_list)
    return max_distance


for i in range(N):
    A = list(map(int, input().split()))
    for j in range(1, len(A), 2):
        if A[j] == -1:
            break
        graph[A[0]].append([A[j], A[j+1]])

for i in range(1, N+1):
    answer = max(DFS(i), answer)

print(answer)

#시간복잡도 줄이기 -> graph만들 떄 이중 for문이 아닌 for문안의 while문으로 만들기