#세 정수의 최댓값 구하기
print('세 정수의 최댓값을 구합니다.')
a = int(input('정수 a의 값을 입력하세요.: '))
b = int(input('정수 b의 값을 입력하세요.: '))
c = int(input('정수 c의 값을 입력하세요.: '))

maximum = a
if b > maximum: maximum = b
if c > maximum: maximum = c

print(f'최댓값은 {maximum}입니다.')

#순차 구조 - 한 문장씩 순서대로 처리되는 구조
#선택  구조 - 조건식으로 평가한 결과에 따라 프로그램의 실행 흐름이 변경되는 구조
#형 변환 - 문자열형을 정수형으로 변환하는 과정
