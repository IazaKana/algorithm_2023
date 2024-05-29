# Decorator
# 함수에서 코드를 변경하지 않고 기능을 추가, 수정하는 문법
# 함수안에 중복코드를 데코레이터 함수로 작성 > 유지보수 향상

def func1():
    print('code1')
    print('code2')
    print('code3')

def func2():
    print('code1')
    print('code4')
    print('code3')

func1()
func2()
#====================================

def deco(func):
    def wrapper(*args, **kwargs):
        print('code1')
        func(*args, **kwargs)
        print('code3')
    return wrapper

@deco
def func1():
    print('code2')

@deco
def func2():
    print('code4')

func1()
func2()

#====================================

import time

start = time.time()
print('code')
end = time.time()
print(end - start)

def show_time(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(end - start)
    return wrapper

@show_time
def func1():
    print('code2')

func1 = show_time(func1)

def func2():
    print('code4')

func1()
func2()

#====================================

def login(func):
    def wrapper(*args, **kwargs):
        pw = input('pw : ')
        if pw == '1234':
            func()
        else:
            print('wrong password')
    return wrapper

#====================================

@login
def func1():
    print('code2')

func1()

#====================================

# *args, **kwargs
# parameter : 여러개의 argument를 하나의 parameter(tuple, dict)로 받는 방법
# argument : 하나의 parameter(list, tuple, dict)를 여러개의 argument로 사용 방법

# 식별자 1개, 데이터 n개 : 컬렉션 데이터타입

def plus(*args): # parameter : 1개
    print(type(args), args)
    print(sum(args))

plus(1, 2, 3, 4, 5) # args : 3개
# argument의 개수의 상관없이 함수를 실행

def plus(*args, **kwargs): # parameter : 1개
    print(type(args), args)
    print(type(kwargs), kwargs)
    print(sum(args) + sum(kwargs.values()))

plus(1, 2, 3, n4=10, n5=20) # args : 3개
# tuple데이터 타입에서 받아줄 수 없는 키워드가 있는 argument는 **kwargs에서 받음