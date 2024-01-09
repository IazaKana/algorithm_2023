def solution(citations):
    
    answer = 0
    citations.sort(reverse = True)
    for i in range(len(citations), -1, -1):
        check = 0
        cnt1 = 0
        cnt2 = 0
        for j in citations:
            if j >= i:
                cnt1 += 1
            if j <= i:
                cnt2 += 1
            
        if cnt1 >= i and cnt2 <= i:
            check = i
            
        answer = max(answer, check)
        
    
    return answer