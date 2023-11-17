T = int(input())

for i in range(1, T+1):
    D, H, M = map(int, input().split())
    answer = 0
    #날짜가 11일 보다 클 때
    if D > 11:
        answer = 769 + (D-12) * 24 * 60 + H * 60 + M
    elif D == 11:
        if H > 11:
            answer = 48 + (H-12) * 60 + M
            pass
        elif H == 11:
            if M >= 11:
                answer = M - 11
            elif M < 11:
                answer = -1
        elif H < 11:
            answer = -1

    print('{}{} {}'.format('#', i, answer))