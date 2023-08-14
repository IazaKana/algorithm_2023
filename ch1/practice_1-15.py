# *를 n개 출력하되 w개마다 줄바꿈하기2

n = int(input('몇 개를 출력할까요?: '))
w = int(input('몇 개마다 줄바꿈할까요?: '))

for _ in range(n // w):
    print('*' * w)

rest = n % w
if rest:
    print('*' * rest)
    

#for문을 반복할 때마다 if 문을 실행하므로 효율적이지 않음