# +와 -를 번갈아 출력하기2

n = int(input('몇 개를 출력할까요?: '))

for _ in range(n // 2):
    print('+-', end='')

if n % 2:
    print('+', end='')

print()

print(n % 2)

#for문에서 언더스코어(_)를 사용한 이유는 for문에서 rane()함수가 for문에서 순환하며 반환하는 값을 사용할 필요하 없기 때문
#if문에서 0값이 나오는 것을 true로 판단해서 결과가 도출되는 것으로 추정