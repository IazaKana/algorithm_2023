import sys
print = sys.stdout.write
A = list(input())

for i in range(len(A)):
    Max = i
    for j in range(i+1, len(A)):
        if A[j] > A[max]:
            Max = j
    if A[i] < A[Max]:
        temp = A[i]
        A[i] = A[Max]
        A[Max] = temp
for i in range(len(A)):
    print(A[i])


#sys.stdout.write - str형식만 출력이 가능, 줄바꿈이 없다(줄바꿈을 쓰고싶으면 sys.stdout.write('\n'))
#sys.stdin.readline()를 쓰면 마지막에 '\n'이 포함되어 있으므로 유의해야 함