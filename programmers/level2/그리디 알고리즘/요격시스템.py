def solution(targets):
    targets.sort(key = lambda v : v[1])
    
    cnt, end = 0, 0
    for x, y in targets:
        if x >= end:
            cnt += 1
            end = y

    return cnt