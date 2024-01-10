def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        c = queue.pop(0)
        if any(c[1] < q[1] for q in queue):
            queue.append(c)
        else:
            answer += 1
            if c[0] == location:
                return answer