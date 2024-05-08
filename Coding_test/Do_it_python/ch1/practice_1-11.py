#a부터 b까지 정수의 합 구하기(for문)
#practice_1-10 개선버전

a = int(input('정수 a의 값을 입력하세요'))
b = int(input('정수 b의 값을 입력하세요'))
sum = 0

if a > b:
    a, b = b, a
    #a와 b를 오름차순으로 정렬

sum = 0

for i in range(a, b):
    print(f'{i} + ', end='')
    sum += i

print(f'{b} = ', end = '')

print(sum)