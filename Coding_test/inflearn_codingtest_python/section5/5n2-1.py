def solution(nums):
    n = len(nums)
    nums.sort()
    answer = []
    m = nums[1] - nums[0]
    for i in range(1, n-1):
        a = nums[i+1] - nums[i]
        if a < m:
            m = a
    for i in range(n-1):
        if nums[i+1] - nums[i] == m:
            answer.append([nums[i], nums[i+1]])
    return answer

print(solution([3, 8, 1, 5, 12]))
print(solution([2, 1, 3, 5, 4]))
print(solution([5, 10, 15, 20, 25, 11]))
print(solution([2, 4, 3, 1, 5, 7, 8, 12, 13, 15, 23]))
print(solution([100, 200, 300, 400, 120, 130, 135, 132, 121]))

# nums오름차순 정리
# for문으로 nums돌면서 최소차 구하기
# for문으로 nums돌면서 최소차와 같은 쌍 구해서 answer로 반환
