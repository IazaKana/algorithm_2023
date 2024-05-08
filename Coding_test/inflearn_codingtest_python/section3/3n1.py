#제한사항:
#nums의 길이 3<=n<=10,000
#배열 nums의 원소는 자연수입니다. 1<=nums[i]<=1,000

def solution(nums):
    answer = -1
    for x in range(len(nums)):
        for y in range(x, len(nums)-x):
            r

    return answer
                            
                
print(solution([3, 9, 2, 12, 9, 12, 8, 7, 9, 12]))
print(solution([2, 1, 3, 2, 1, 3, 4, 5, 4, 5, 6, 7, 6 ,7, 8, 8]))
print(solution([23, 56, 11, 67, 120, 560, 812, 960, 560, 777, 888, 960]))
print(solution([11, 73, 156, 789, 345, 156, 789, 345, 678, 555, 678]))
print(solution([1, 3, 1, 5, 7, 2, 3, 1, 5]))

#원솟값이 1000밖에 되지 않으므로 direct-address table을 사용

def solution(nums):
    answer = -1
    cnt = [0] * 1001  #1001까지 해야지 인덱스 번호가 0부터 1000번까지 생성
    for x in nums:
        cnt[x] += 1

    for i in range(1000, 0, -1):
        if cnt[i] == 1:
            return i
       
    return answer