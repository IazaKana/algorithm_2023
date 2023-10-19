from collections import defaultdict, Counter

def solution(nums):
    answer = -1
    nH = Counter(nums)
    for key in nH:
        if nH(key) == 1:
            answer = max(key, answer)

    return answer