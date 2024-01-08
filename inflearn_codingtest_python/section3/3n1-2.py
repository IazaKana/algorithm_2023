from collections import Counter

def solution(nums):
    cnt = Counter(nums)
    m = []
    
    for x in cnt:
        if cnt[x] == 1:
            m.append(x)

    if len(m) > 0:
        m.sort(reverse = True)
        result = m[0]
    else:
        result = -1

    return result

print(solution([3, 9, 2, 12, 9, 12, 8, 7, 9, 12]))
print(solution([2, 1, 3, 2, 1, 3, 4, 5, 4, 5, 6, 7, 6 ,7, 8, 8]))
print(solution([23, 56, 11, 67, 120, 560, 812, 960, 560, 777, 888, 960]))
print(solution([11, 73, 156, 789, 345, 156, 789, 345, 678, 555, 678]))
print(solution([1, 3, 1, 5, 7, 2, 3, 1, 5]))