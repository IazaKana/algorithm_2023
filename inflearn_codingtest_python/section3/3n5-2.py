from collections import Counter

def solution(s):
    s = Counter(s)
    sum = 0
    cnt = 0
    for x in s:
        if s[x] % 2 == 0:
            sum += s[x]
        else:
            sum += s[x]
            cnt += 1
    
    for _ in range(cnt-1):
        sum -= 1

    return sum

print(solution("abcbbbccaaeee"))
print(solution("aabbccddee"))
print(solution("fgfgabtetaaaetytceefcecekefefkccckbsgaafffg"))
print(solution("aabcefagcefbcabbcc"))
print(solution("abcbbbccaa"))