from queue import PriorityQueue
N = int(input())
pq = PriorityQueue()

for _ in range(N):
    date = int(input())
    pq.put(date)

a = 0
b = 0
sum = 0

while pq.qsize()>1:
    a = pq.get()
    b = pq.get()
    temp = a + b
    sum += temp
    pq.put(temp)

print(sum)