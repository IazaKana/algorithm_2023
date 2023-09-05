#1부터 n까지의 정수의 합 구하기2

n = int(input('n값을 입력하세요.:'))

sum = 0

for i in range(1, n+1):
    sum += i

print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')

#range()함수로 이터러블 객체 생성하기 range(n), range(a, b), range(a, b, step)