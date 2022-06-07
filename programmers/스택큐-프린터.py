#큐자료구조를 활용하면 더 쉽게 풀 수 있음
#enumerate를 활용하면 더 쉬움
#any를 이용하여 조건문 만들기
from collections import deque
def solution(priorities, location):
    que = [(i,v) for i,v in enumerate(priorities)]
    q = deque(que)
    answer = 0

    while True:
        cur= q.popleft()
        #value보다 큰값이 있으면 뒤에 붙히기
        if any(cur[1]<b for a,b in q):
            q.append(cur)
        else:
            
            answer +=1
            if cur[0] == location:
                return answer

            
            


# #같은 숫자에 주의!
# def solution(priorities, location):

#     idx = [i for i in range(len(priorities))]
#     result = []

#     while True:
#         mx = max(priorities)
#         if priorities[0] != mx:
#             mx_idx = priorities.index(mx)
            
#             before_value = priorities[:mx_idx]
#             before_index = idx[:mx_idx]
#             after_value = priorities[mx_idx:]
#             after_index = idx[mx_idx:]
#             priorities = after_value+before_value
#             idx = after_index+before_index

#         else:
#             result.append(idx[0])
#             temp_value = priorities[1:]
#             temp_index = idx[1:]
#             idx = temp_index
#             priorities = temp_value
#             if len(idx) == 1:
#                 result.append(idx[0])
#                 break

#     answer = result.index(location)+1
    
#     return answer