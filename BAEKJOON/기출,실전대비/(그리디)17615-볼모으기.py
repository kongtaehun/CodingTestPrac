
from collections import Counter
n = int(input())
balls = list(input())
right = balls[-1]
left = balls[0]
left_side = 0
right_side = 0
for i in range(n):
    if balls[i] == left:
        left_side += 1
    else:
        break

for i in range(n-1, -1, -1):
    if balls[i] == right:
        right_side += 1
    else:
        break

temp = dict(Counter(balls))
compare_list = [temp[right] - right_side, temp[left] -
                left_side]
if 'R' in temp.keys():
    compare_list.append(temp['R'])
if 'B' in temp.keys():
    compare_list.append(temp['B'])

answer = min(compare_list)
print(answer)
