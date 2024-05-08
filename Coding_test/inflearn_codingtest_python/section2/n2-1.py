def solution(score, k):
    answer = 0
    for i in range(len((score))):
        if score[i] >= k:
            answer += 1
    return answer