def solution(moves):
    answer = [0] * 2
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    n = len(moves)
    for i in range(n):
        if moves[i] == 'U':
            answer[0] += dx[0]
            answer[1] += dy[0]
        elif moves[i] == 'R':
            answer[0] += dx[1]
            answer[1] += dy[1]
        elif moves[i] == 'D':
            answer[0] += dx[2]
            answer[1] += dy[2]
        elif moves[i] == 'L':
            answer[0] += dx[3]
            answer[1] += dy[3]
    
    return answer

print(solution('RRRDDDLU'))
print(solution('DDDRRRDDLL'))
print(solution('RRRRRRDDDDDDUULLL'))
print(solution('RRRRDDDRRDDLLUU'))