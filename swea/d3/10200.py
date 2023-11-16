TC = int(input())

for i in range(1, TC+1):
    N, A, B = map(int, input().split())
    if N >= A+B:
        min_ = 0
    else:
        min_ = A+B - N

    max_ = min(A, B)
    print(max_, min_)

    print('{}{} {} {}'.format('#', i, max_, min_))