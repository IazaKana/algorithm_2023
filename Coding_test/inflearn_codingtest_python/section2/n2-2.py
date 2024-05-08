score = list(map(int, input().split()))
k = int(input())
answer = 0

for x in score:
    if x >= k:
        answer += 1

print(answer)