n = int(input())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 0

def solution():
    global count
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        #조건1)해당 방향으로 K길이만큼 모두 1이어야함
        if x + dx[i] * 3

for i in range(n):
    N, K = map(int, input().split())
    A = []
    for j in range(N):
        A.append(map(int, input().split()))

    for j in range(N):
        for k in range(N):
            if A[j][k] == 1:
                solution(j, k)


#===============================================
t - int(input())

for tc in range(1, t + 1):
    n, k = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(n)]

    result = 0

    for i in range(n):
        cnt = 0
        for j in range(n):
            if data[i][j] == 1:
                cnt += 1
            if data[i][j] == 0 or j == n-1:
                if cnt == k:
                    result += 1
                if data[i][j] == 0:
                    cnt = 0

                        
