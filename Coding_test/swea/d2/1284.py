n = int(input())

for i in range(n):
    P, Q, R, S, W = map(int, input().split())
    answer = 0
    if W <= R:
        if P*W <= Q:
            answer = P*W
        else:
            answer = Q
    elif W > R:
        if P*W <= Q+S*(W-R):
            answer = P*W
        else:
            answer = Q+S*(W-R)
    print('{}{} {}'.format('#', i+1, answer))