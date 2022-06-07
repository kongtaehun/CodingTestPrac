def solution(prices):
    times = []
    for i in range(len(prices)):
        time = 0
        for j in range(i+1,len(prices)):
            time+=1
            if prices[j]<prices[i]:
                break
        times.append(time)

    
    
    answer = times
    return answer

#전체가격검사?