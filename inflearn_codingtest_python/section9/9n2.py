def DFS(n):
    answer = 1
    if n > 2:
        return DFS(n-1) + DFS(n-2)
    if n == 2:
        return answer
    if n == 1:
        return answer

    
              
print(DFS(5))
print(DFS(8))

