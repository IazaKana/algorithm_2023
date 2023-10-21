from collections import Counter
def solution(nums):
    answer = 0
    n = len(nums) #사탕의 개수
    nH = Counter(nums)
    m = len(nH) #사탕의 종류
    if n//2 < m:
        answer = n//2
    else:
        answer = m
    return answer
    


print(solution([2, 1, 1, 3, 2, 3, 1, 2]))
print(solution([1, 3, 5, 7, 2, 3, 7, 5, 3, 2, 5, 7, 9, 12]))
print(solution([5, 5, 5, 5, 5, 5]))
print(solution([12, 23, 11, 3, 5, 23, 23, 23, 23, 23, 23, 23]))
print(solution([100, 200, 300, 400, 500, 600, 700, 800]))