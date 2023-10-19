from collections import defaultdict, Counter
def solution(nums):
    answer = 1000000
    nH = defaultdict(int)
    for i in nums:
        nH[i] += 1
    for key in nH:
        if key == nH[key]:
            answer = min(key, answer)

    return -1 if answer == 1000000 else answer

print(solution([1, 2, 3, 1, 3, 3, 2, 4]))
print(solution([1, 2, 3, 3, 3, 2, 4, 5, 5, 5]))
print(solution([1, 1, 2, 5, 5, 5, 5, 5, 3, 3, 3, 3, 5]))
print(solution([7, 6, 7, 7, 8, 8, 8, 8, 7, 5, 7, 7, 7, 8, 8]))