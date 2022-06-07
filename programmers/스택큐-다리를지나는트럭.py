from collections import deque
def solution(bridge_length, weight, truck_weights):
    
    다리건너는트럭 = deque()
    건너는트럭경과시간 = deque()
    건너는트럭경과시간.append(0)
    다리건너는트럭.append(truck_weights[0])
    truck_weights.pop(0)
    
    
    time =1
    while 다리건너는트럭:
        
        time +=1
        #시간초올리기
        upsecond(건너는트럭경과시간)
        #트럭뺴기
        if 건너는트럭경과시간[0] >= bridge_length:
            건너는트럭경과시간.popleft()
            다리건너는트럭.popleft()
        #트럭추가
        if len(truck_weights)>0 and sum(list(다리건너는트럭))+truck_weights[0]<=weight:
            건너는트럭경과시간.append(0)
            다리건너는트럭.append(truck_weights[0])
            truck_weights.pop(0)
        
    answer = time
    return answer


def upsecond(건너는트럭경과시간):
    for i in range(len(건너는트럭경과시간)):
        건너는트럭경과시간[i]+=1