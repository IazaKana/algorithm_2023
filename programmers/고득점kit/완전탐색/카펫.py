def solution(brown, yellow):
    
    answer = []
    
    # cd = []
    
    
    # for i in range(1, yellow + 1):
    #     for j in range(i, yellow + 1):
    #         if i * j == yellow:
    #             cd.append((i, j))
    
    for i in range(1, brown//2 + 1):
        for j in range(i, brown//2 + 1):
            if ((i+1) + (j+1)) * 2 == brown and i * j == yellow:
                answer = [i+2, j+2]
    
    
    # for i in cd:
    #     if ((i[0] + 1) + (i[1] + 1)) * 2 == brown:
    #         answer = [i[0]+2, i[1]+2]
    
    answer.sort(reverse = True)
    
    return answer