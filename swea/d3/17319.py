n = int(input())

for i in range(1, n+1):
    a = int(input())
    S = str(input())
    if a % 2 == 1:
        answer = 'No'
    else:
        if S[:a//2] == S[a//2:]:
            answer = 'Yes'
        else:
            answer = 'No'
    print('{}{} {}'.format('#', i, answer))
        
#if else 분류 신중히