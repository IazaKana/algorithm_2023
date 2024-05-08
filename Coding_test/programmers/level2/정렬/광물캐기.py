def solution(picks, minerals):
    
    ps = sum(picks)
    if len(minerals) > ps * 5:
        minerals = minerals[:ps * 5]
    
    k_minerals = []
    for x in range(0, len(minerals), 5):
        k_minerals.append(minerals[x:x+5])
    
    re_minerals = []
    for x in k_minerals:
        a = [0, 0, 0]
        for y in x:
            if y == 'diamond':
                a[0] += 1
            elif y == 'iron':
                a[1] += 1
            elif y == 'stone':
                a[2] += 1
        re_minerals.append(a)
    
    re_minerals.sort(key = lambda v : (-v[0], -v[1], -v[2]))
    
    result = 0
    i = 0
    while picks[0] > 0:
        if i >= len(re_minerals):
            break
        result += 1 * re_minerals[i][0] + 1 * re_minerals[i][1] + 1 * re_minerals[i][2]
        i += 1
        picks[0] -= 1
        
    
    while picks[1] > 0:
        if i >= len(re_minerals):
            break
        result += 5 * re_minerals[i][0] + 1 * re_minerals[i][1] + 1 * re_minerals[i][2]
        i += 1
        picks[1] -= 1
        
    while picks[2] > 0:
        if i >= len(re_minerals):
            break
        result += 25 * re_minerals[i][0] + 5 * re_minerals[i][1] + 1 * re_minerals[i][2]
        i += 1
        picks[2] -= 1
        
    return result