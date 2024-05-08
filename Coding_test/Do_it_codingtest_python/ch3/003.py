#S[i] = S[i-1] + A[i]
n, m = map(int, input().split())
p_list = list(map(int, input().split()))
sum = 0
p_sum = [0]

for i in range(n):
    sum += i
    p_sum.append(sum)
    
for i in range(m):
    s, e = map(int, input().split())
    print(p_sum[e] - p_sum[s])