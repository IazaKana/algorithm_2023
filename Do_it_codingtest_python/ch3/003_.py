#반복문으로 여러줄 입력받는 상황에서는 반드시
#sys.stdin.readlint()을 사용해야 시간초과가 발생하지 않는다.
# sys.stdin.readline() 사용법
# import sys
# 한 개의 정수를 입력받을 때
# a = int(sys.stdin.readline())
# 정해진 개수의 정수를 한줄에 입력받을 때
# import sys
# a,b,c = map(int,sys.stdin.readline().split())
# 임의의 개수의 정수를 한줄에 입력받아 리스트에 저장할 때
# import sys
# data = list(map(int,sys.stdin.readline().split()))
# 임의의 개수의 정수를 n줄 입력받아 2차원 리스트에 저장할 때
# import sys
# data = []
# n = int(sys.stdin.readline())
# for i in range(n):
#     data.append(list(map(int,sys.stdin.readline().split())))
# 문자열 n줄을 입력받아 리스트에 저장할 때
# import sys
# n = int(sys.stdin.readline())
# data = [sys.stdin.readline().strip() for i in range(n)]