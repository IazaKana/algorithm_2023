def solution(n, moves): 
    x = y = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    dir = ['U', 'R', 'D', 'L']
    for c in moves:
        if x == 0 and c == dir[0]:
            continue
        elif x == n and c == dir[2]:
            continue
        elif y == 0 and c == dir[3]:
            continue
        elif y == 0 and c == dir[1]:
            continue
        for k in range(4):
            if c == dir[k]:
                x = x + dx[k]
                y = y + dy[k]
         
    return [x, y]  
                
                      
print(solution(5, 'RRRDDDUUUUUUL'))
print(solution(7, 'DDDRRRDDLL'))
print(solution(5, 'RRRRRDDDDDU'))
print(solution(6, 'RRRRDDDRRDDLLUU'))

def solution(n, moves):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    dir = ['U', 'R', 'D', 'L']
    x = y = 0
    for c in moves:
        for k in range(4):
            if c == dir[k]:
                nx = x + dx[k]
                ny = y + dy[k]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        x = nx
        y = ny
 
    return [x, y]    