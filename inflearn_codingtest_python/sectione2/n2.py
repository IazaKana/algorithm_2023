#제한사항:
# score의 길이 3 <= n <= 10,000
# 0 <= score[i] <= 100
# 50 <= k <= 90

def solution(score, k):
    answer = 0
    for i in range(len(score)):
        if score[i] >= k:
            answer += 1
    
    return answer

print(solution([60, 50, 80, 90, 55, 70, 65, 45], 60))

#n이 최소한 10만 정도는 되야 효율성을 체크하는 문제

def solution(score, k):
    answer = 0
    for x in score:
        if x >= k:
            answer += 1        
    return answer