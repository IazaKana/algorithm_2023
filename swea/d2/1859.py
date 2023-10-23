# from collections import deque
# n = int(input())

# def DFS(nums, sum):
#     max_n = max(nums)
#     ex_nums = []
#     count = 0
#     #리스트 안의 가장 큰 값 구하기
#     for i in nums:
#         count += 1
#         if i == max_n:
#             sum += count * i #제일 큰 값을 만났을떄는 ((인덱스값 + 1) * 값)을 sum에 추가하기
#             for k in nums:
#                 ex_nums.append(k) #남은 값들을 다른 빈 리스트에 추가 해서 새로운 리스트 만듦
#             if len(ex_nums) > 1:
#                 DFS(ex_nums, sum)
#             elif len(ex_nums) <= 1:
#                 return sum
#         else:
#             sum += (-1 * i)
#     #처음 부터 가장 큰 값이 나올떄까지 (-1 * 해당 값)을 sum에 추가하기, 해당 값 popleft하기
#     #해당값 popleft하기
#     #리스트의 길이가 남아있으면 DFS반복


# for i in range(n):
#     a = int(input())
#     nums = deque(map(int, input().split()))
#     sum = 0
#     DFS(nums, sum)
#     print('#' + (i+1), sum)


# ====================================

b = int(input())
for i in range(b):
    n = int(input())
    nums = list(map(int, input().split()))
    m = max(nums)
    count = 0
    sum = 0
    start = 0
    for j in range(0, n):
        if nums[start] == m:
            break
        count += 1
        if nums[j] == m:
            sum += (count-1)*nums[j]
            nums[j] = -1
            m = max(nums)
            count = 0
            start = j+1
        elif nums[j] < m:
            sum += (-1)*nums[j]
            nums[j] = -1
    print('#' + str(i+1), sum)

    # ===================================

