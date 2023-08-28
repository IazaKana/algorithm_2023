# +와 -를 번갈아 출력하기1

n = int(input('몇 개를 출력할까요?: '))

for i in range(n):
    if i % 2:
        print('-', end='')
    else:
        print('+', end='')

print()

#두가지 문제점
#1)for문을 반복할 때마다 if문을 수행한다는 것
#2)상황에 따라 유연하게 수정하기는 어렵다는 것

