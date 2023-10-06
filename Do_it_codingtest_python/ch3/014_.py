from queue import PriorityQueue
import sys
print = sys.stdout.write
input = sys.stdin.readline
N = int(input())
myQueue = PriorityQueue()

for i in range(N):
    request = int(input())
    if request == 0:
        if myQueue.empty():
            print('0\n')
        else:
            temp = myQueue.get()
            print(str((temp[1]))+'\n')
    else:
        myQueue.put((abs(request), request))

# 우선순위큐 -  데이터 추가는 어떤 순서로 해도 상관이 없지만 제거될 때는 가장 작은 값을 제거하는 
#              특성을 지닌 자료구조
# put()메서드를 이용하여 우선순위 큐에 원소를 추가할 수 있음
# get()메서드를 이용해서 우선순위 큐에 원소를 삭제할 수 있음, 삭제된 원소를 리턴함
# put()과 get()함수는 O(log n)의 시간 복잡도를 가짐.
# 정렬기준변경 - 단순 오름차순이 아닌 다른 기준으로 원소가 정렬되기를 원한마녀 (우선순위, 값)의 튜플의
# 형태로 데이터를 추가하고 제거하면 됨 ex)que.put((3, 'Apple'))
# 리스트가 비어있는지 확인 -> len 혹은 empty
# abs(x) -> 절대값으로 변환