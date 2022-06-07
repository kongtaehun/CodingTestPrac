#1. sort의 key인자(특정컬럼기준 정렬)
from collections import Counter
def solution(genres, plays):

    장르별횟수 = []
    for i in range(len(genres)):
        장르별횟수.append((genres[i],plays[i],i))
    
    장르별총횟수 = {}
    장르별횟수.sort(key = lambda x:(x[0],-x[1]))
    result = {}
    
    for i in range(len(장르별횟수)):
        if i==0 or 장르별횟수[i][0] != 장르별횟수[i-1][0]:
            장르별총횟수[장르별횟수[i][0]] = 장르별횟수[i][1]
            
            if i != len(장르별횟수)-1 and 장르별횟수[i][0] == 장르별횟수[i+1][0]:
                result[장르별횟수[i][0]] = [장르별횟수[i][2],장르별횟수[i+1][2]]
            
            else:
                result[장르별횟수[i][0]]=[장르별횟수[i][2]]
        else:
            장르별총횟수[장르별횟수[i][0]] += 장르별횟수[i][1]
            
    장르별총횟수 = sorted(sorted(장르별총횟수.items()),key = lambda x: (-x[1]))
    
    answer = []
    for i in range(len(장르별총횟수)):
        if len(result[장르별총횟수[i][0]]) ==2:
            answer.append(result[장르별총횟수[i][0]][0])
            answer.append(result[장르별총횟수[i][0]][1])
        else:
            answer.append(result[장르별총횟수[i][0]][0])
    

    return answer