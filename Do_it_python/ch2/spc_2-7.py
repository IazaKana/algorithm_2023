# 파이썬 표준 라이브러리를 사용하면 리스트를 역순으로 정렬하거나 정렬한 리스트를 새로 생성할 수 있음
# x.reverse() - 리스트x의 원소를 역순으로 정렬
# reversed(X) - x의 원소를 역순으로 꺼내는 이터레이터(반복자)를 반환하는 것
# 리스트 x를 역순으로 정렬하여 y에 대입하려면 - y = list(reversed(x))

x = [1, 2, 3, 4, 5, 6, 7]
print(x)
y = list(reversed(x))
print(y)
# z = x.reverse()
# print(z)
# print(x)

#reverse는 값을 반환하지 않고 단순히 해당 list를 뒤섞어줌
#reversed는 내장함수로 list에서 제공하는 함수가 아님

# .reverse()와 reversed()의 차이
# 1.리스트 함수 vs 내장 함수인 점
# .reverse()는 List, 리스트 함수 - 리스트에만 쓸 수 있음
# reversed()는 파이썬 내장 함수 - 리스트, 튜플, 스트링, 딕셔너리 사용 가능
# 2.값 반환 여부의 차이
# .reverse()는 값을 반환하지 않음
# reversed()는 객체 값을 반환
# 3.해당 객체 원형 변형 여부
# .reverse() -> 해당 리스트의 원형을 바꿔놓음
# reversed() -> 해당 객체의 원형을 바꾸지 않음