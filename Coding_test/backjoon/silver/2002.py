import sys
from collections import deque

N = int(input())
A = deque()
B = list()

for i in range(N):
    A.append(sys.stdin.readline())

for i in range(N):
    B.append(sys.stdin.readline())

answer = 0
#A를 순서대로 탐색 시작
#A에 대해서 B를 탐색하는데 첫번째로 탐색할 떄 값이 같으면 넘어가고
#다를 경우 같을 때까지 다를 때마다 값 삭제 후 answer += 1재탐색

for i in A:
    for j in range(len(B)):
        if i == B[j]:
            B[j] = 0
            break
        else:
            if  B[j] != 0:
                answer += 1
                B[j] = 0

print(answer)

