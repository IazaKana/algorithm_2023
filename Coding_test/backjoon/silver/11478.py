n = input()
sum = 0
set_a = set()

for i in range(len(n)):
    for j in range(len(n)-i):
        set_a.add(n[j:j+i+1])

print(len(set_a))