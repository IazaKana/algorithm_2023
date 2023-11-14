N = int(input())

for i in range(1, N+1):
    a = list(input())
    cnt_o = 0
    cnt_x = 0
    answer = ''
    for j in a:
        if j == 'o':
            cnt_o += 1
        elif j == 'x':
            cnt_x += 1
    b = 15 - len(a)
    if b >= 8-cnt_o:
        answer = 'YES'
    else:
        answer = 'NO'
    print('{}{} {}'.format('#', i, answer))

