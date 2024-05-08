T = int(input())

for i in range(1, T+1):
    answer = 1

    S = [0]
    D = [0]
    H = [0]
    C = [0]

    S_check = [0 for _ in range(14)]
    D_check = [0 for _ in range(14)]
    H_check = [0 for _ in range(14)]
    C_check = [0 for _ in range(14)]

    for j in range(1, 14):
        S.append(['S', j])
    for j in range(1, 14):
        D.append(['D', j])
    for j in range(1, 14):
        H.append(['H', j])
    for j in range(1, 14):
        C.append(['C', j])

    S_num = 13
    D_num = 13
    H_num = 13
    C_num = 13

    arr = list(input())

    for j in range(0, len(arr), 3):
        if arr[j] == 'S':
            num = int(arr[j+1]) * 10 + int(arr[j+2])
            if S_check[num] == 0:
                S_check[num] = 1
                S_num -= 1
            else:
                answer = 0
                break

        elif arr[j] == 'D':
            num = int(arr[j+1]) * 10 + int(arr[j+2])
            if D_check[num] == 0:
                D_check[num] = 1
                D_num -= 1
            else:
                answer = 0
                break

        elif arr[j] == 'H':
            num = int(arr[j+1]) * 10 + int(arr[j+2])
            if H_check[num] == 0:
                H_check[num] = 1
                H_num -= 1
            else:
                answer = 0
                break

        elif arr[j] == 'C':
            num = int(arr[j+1]) * 10 + int(arr[j+2])
            if C_check[num] == 0:
                C_check[num] = 1
                C_num -= 1
            else:
                answer = 0
                break

    if answer == 1:
        print('{}{} {} {} {} {}'.format('#', i, S_num, D_num, H_num, C_num))
    elif answer == 0:
        print('{}{} {}'.format('#', i, 'ERROR'))




