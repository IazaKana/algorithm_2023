from collections import deque

def solution(nums):
    answer = deque(nums)
    for i in range(1, len(nums)):
        if answer[i] == answer[i-1]:
            answer.pop()
    answer.sort(reverse = True)
    return list(answer)

print(solution([0, 1, 1, 1, 2, 2, 2, 3]))
print(solution([1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 5]))
print(solution([0, 0, 0, 3, 3, 3, 5, 7, 7, 7]))
print(solution([1, 2, 3, 4, 5, 6, 7, 7, 7, 8, 9]))

#바꾸는 방법이 아닌 다른 방법 활용