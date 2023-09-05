#1부터 n까지 정수의 합 구하기

def sum_1ton(n):
    s = 0
    while n > 0:
        s += n
        n -= 1
    return s

x = int(input('x의 값을 입력하세요.: '))
print(f'1부터 {x}까지의 정수의 합은 {sum_1ton}입니다.')

# 파이썬에서는 매개변수에 실제 인수가 대입됨.
# 파이썬에서 인수 전달은 실제 인수인 객체에 대한 참조를 값으로 전달하여 매개변수에 대입되는 방식
# 함수의 실행 시작 시점에서 매개변수는 실제 인수와 같은 객체를 참조함, 함수에서 매개변수의 값을 변경하면 인수의 형에 따라 다음과 같이 구분
# 1.인수가 이뮤터블일 때:함수 안에서 매개변수의 값을 변경하면 다른 객체를 생성하고 그 객체에 대한 참조로 업데이트됨. 따라서 매개변수의 값을 변경해도 호출하는 쪽의 실제 인수에는 영향을 주지 않음.
# 2.인수가 뮤터블일 떄:함수 안에서 매개변수의 값을 변경하면 객체 자체를 업데이트함. 따라서 매개변수의 값을 변경하면 호출하는 쪽의 실제 인수는 값이 변경