#모든 것이 동시에끝나면?
from collections import deque
def solution(progresses, speeds):

    result = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    day = 0
    while True:
        day+=1
        setProgress(progresses,speeds,result)
        if len(progresses)==0:
            break
    answer = result
    return answer

#작업
def setProgress(progresses, speeds,result):
    for i in range(len(progresses)):
        progresses[i]+=speeds[i]
    checkDone(progresses,speeds,result)
        
#배포
def checkDone(progresses,speeds,result):
    #처음부터 100넘는거의 개수를 센다
    count = 0
    for i in range(len(progresses)):
        if progresses[i] >=100:
            count+=1
        else:
            break
    temp = 0
    for i in range(count):
        progresses.popleft()
        speeds.popleft()
        temp+=1
    if temp>0:
        result.append(temp)