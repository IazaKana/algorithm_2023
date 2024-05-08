def solution(box, limit):
    answer = 0
    box.sort(key = lambda v : -v[1])
    for x in box:
        cnt = min(limit, x[0])
        answer += (cnt * x[1])
        limit -= cnt
        if limit == 0:
            break
    
    return answer

#불규칙 반복 연산 