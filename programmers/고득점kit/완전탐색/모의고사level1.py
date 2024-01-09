def solution(answers):
    n1 = []
    n2 = []
    n3 = []
    n = len(answers)
    result = []
    
    for x in range(n):
        if x % 5 == 0:
            n1.append(1)
        elif x % 5 == 1:
            n1.append(2)
        elif x % 5 == 2:
            n1.append(3)
        elif x % 5 == 3:
            n1.append(4)
        elif x % 5 == 4:
            n1.append(5)
    
    for x in range(n):
        if x % 2 == 0:
            n2.append(2)
        elif x == 1:
            n2.append(1)
        else:
            if n2[x-2] == 1:
                n2.append(3)
            elif n2[x-2] == 3:
                n2.append(4)
            elif n2[x-2] == 4:
                n2.append(5)
            elif n2[x-2] == 5:
                n2.append(1)
            
    for x in range(n):
        if x % 10 == 0:
            n3.append(3)
        elif x % 10 == 1:
            n3.append(3)
        elif x % 10 == 2:
            n3.append(1)
        elif x % 10 == 3:
            n3.append(1)
        elif x % 10 == 4:
            n3.append(2)
        elif x % 10 == 5:
            n3.append(2)
        elif x % 10 == 6:
            n3.append(4)
        elif x % 10 == 7:
            n3.append(4)
        elif x % 10 == 8:
            n3.append(5)
        elif x % 10 == 9:
            n3.append(5)
            
    ch = [0, 0, 0]
    
    for x in range(n):
        if answers[x] == n1[x]:
            ch[0] += 1
        if answers[x] == n2[x]:
            ch[1] += 1
        if answers[x] == n3[x]:
            ch[2] += 1
            
    mv = max(ch)
    result = [i+1 for i, v in enumerate(ch) if v == mv]