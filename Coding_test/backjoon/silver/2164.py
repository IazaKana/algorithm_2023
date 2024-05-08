from collections import deque
N = int(input())
test = deque()
for i in range(N, 0, -1):
    test.append(i)

while len(test) > 1:
    test.pop()
    test.appendleft(test.pop())

print(test[0])