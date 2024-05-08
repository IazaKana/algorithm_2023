n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    A = [] #빈리스트 선언
    for j in range(a):
        A.append(list(map(int, input().split()))) #a*a줄 이중리스트 입력
    sum = 0
    answer = 0
    for j in range(a-b+1):
        for k in range(a-b+1):
            for u in range(b):
                for w in range(b):
                    sum += A[j+u][k+w]
            answer = max(answer, sum)
            sum = 0
    print('#' + str(i+1), answer)