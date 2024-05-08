# T = int(input())
#
# for i in range(1, T+1):
#     N, M = map(int, input().split())
#     graph = [[]] * (N+1)
#     for j in range(M):
#         x, y = map(int, input().split())
#         graph[x].append(y)
#         graph[y].append(x)


#
from collections import defaultdict

t = int(input())
for tc in range(1, t + 1) :
    n, m = map(int, input().split())
    data = defaultdict(list)

    for _ in range(m) :
        x, y = map(int, input().split())
        data[x].append(y)
        data[y].append(x)

    print(data)

    result = 0
    for i in range(1, n + 1) :
        for j in range(i + 1, n + 1) :
            for k in range(j + 1, n + 1) :
                if i in data[j] and j in data[k] and k in data[i] :
                    result += 1

    print('#%d %d' % (tc, result))