from collections import Counter

def solution(participant, completion):
    
    np = Counter(participant) - Counter(completion)
    
    answer = list(np.keys())[0]
    
    return answer