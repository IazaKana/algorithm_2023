#a부터 b까지 정수의 합 구하기(for문)

a = int(input('정수 a의 값을 입력하세요'))
b = int(input('정수 b의 값을 입력하세요'))
sum = 0

if a > b:
    a, b = b, a
    #a와 b를 오름차순으로 정렬

for i in range(a, b+1):
    if i < b:
        print(f'{i} + ', end='')
    else:
        print(f'{i} = ', end='')
    sum += i

print(sum)

print(f'{a}부터 {b}까지 정수의 합은 {sum}입니다')

#수가 커지면 판단 한 번을 위해 많은 실행을 해야하므로 효율적이지 않음
