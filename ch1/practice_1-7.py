#1부터 n까지의 정수의 합 구하기

n = int(input('n값을 입력하세요.:'))

sum = 0
i = 1

while i <= n:
    sum += i
    i += 1

print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')

#반복을 제어할 때 사용하는 i를 카운터용 변수라고 함
#f-string 포매팅