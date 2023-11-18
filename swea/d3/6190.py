from itertools import combinations
T = int(input())

def solution(number):
    arr = list(str(number))
    i = 0
    while i < len(arr)-1:
        if arr[i] > arr[i+1]:
            return False
        i += 1
    return True

for i in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    #조합으로 2개로 이루어진 경우의 수
    B = list(combinations(A, 2))
    C = list()
    max_num = -1

    #모든 경우 리스트로 반환
    for j in range(len(B)):
        C.append(B[j][0] * B[j][1])

    for j in C:
        if max_num < j and solution(j):
            max_num = j


    print('{}{} {}'.format('#', i, max_num))

