# 1.시간복잡도
# n제한이 10만 이상이면 시간복잡도를 O(nlogn)이나 O(n)으로 짜려고 해야 한다

#2.배열과 연결리스트
#2.2

def cal(nums):
    n = len(nums)
    for i in range(n):
        for j in range(2**n):