N = int(input())

def solution(x, y, num):
    answer = 1
    graph[x][y] = '.'
    for i in range(x+1, x+num):
        for j in range(y, y+num):
            if graph[i][j] != '#':
                graph[i][j] = '.'
                answer = 0
                break
            else:
                graph[i][j] = '.'
    return answer

for i in range(N):
    M = int(input())
    graph = list()
    for j in range(M):
        graph.append(list(input()))
    count = 0
    result = 'no'
    for x in range(M):
        for y in range(M):
            if graph[x][y] == '#':
                count += 1
                if count == 1:
                    #처음 #을 발견했을때 해당 자리 x, y값 저장
                    nx = x
                    ny = y
                if count >= 2:
                    # 다음 y의 탐색값이 벽이거나 '.'일 경우
                    if y+1 == M or (y+1 < M and graph[x][y+1] == '.'):
                        if solution(nx, ny, count) == 1:
                            result = 'yes'
                            break
            else:
                count = 0
        if result == 'yes':
            break

    print('{}{} {}'.format('#', i+1, result))


