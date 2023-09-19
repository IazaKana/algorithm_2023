dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(5):
    for j in range(5):
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if nx >= 0 and nx < 5 and ny >= 0 and ny < 5:
                if nums[nx][ny] <= nums[i][j]:
                    flag = False