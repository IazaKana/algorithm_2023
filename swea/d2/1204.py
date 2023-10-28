n = int(input())

for i in range(n):
    a = int(input())
    A = list(map(int, input().split()))
    B = [0] * 101
    bin = 0
    max = 0
    for j in A:
        B[j] += 1
    for j in range(101):
        if B[j] >= bin:
            bin = B[j]
            max = j
    print('{}{} {}'.format('#', a, max))

#다음에 counter모듈 사용해보기