TC = int(input())

for i in range(TC):
    N, M = map(int, input().split())
    M = str(bin(M))
    answer = 'ON'
    for j in range(1, N+1):
        if M[-j] == '0':
            answer = 'OFF'
            break
    print('{}{} {}'.format('#', i+1, answer))

#=============================================
TC = int(input())

for i in range(TC):
    N, M = map(int, input().split())
    if M % 2 ** N == 2 ** N -1:
        answer = 'ON'
    else:
        answer = 'OFF'
    print('{}{} {}'.format('#', i+ 1, answer))