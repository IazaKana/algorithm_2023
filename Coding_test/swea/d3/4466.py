T = int(input())

for i in range(1, T+1):
    N, K = map(int, input().split())
    score = list(map(int, input().split()))
    score.sort(reverse = True)
    sum = 0
    for j in range(K):
        sum += score[j]

    print('{}{} {}'.format('#', i, sum))