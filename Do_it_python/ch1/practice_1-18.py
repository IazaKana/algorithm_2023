# 10~99 사이의 난수 n개 생성하기

import random

n = int(input('난수의 개수를 입력하세요.: '))

for _ in range(n):
    r = random.randint(10, 99)
    print(r, end='')
    if r == 13:
        print('\n프로그램을 중단합니다.')
        break
else:
    print('\n난수 생성을 종료합니다.')

#반복이 끝난 다음 else문이 실행됨
#13이 생성되면 break문으로 강제 종료하고 else문도 실행되지 않습니다.