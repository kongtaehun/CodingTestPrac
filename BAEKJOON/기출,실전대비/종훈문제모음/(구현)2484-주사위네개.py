from collections import Counter


def count(a):
    temp = dict(Counter(a))
    max_cnt = 0
    now_val = 0
    now_val_temp = 0
    for key in temp.keys():
        cnt = temp[key]
        if max_cnt < cnt:
            max_cnt = cnt
            now_val = key
        elif max_cnt == 2 and cnt == 2:
            now_val_temp = key

    if max_cnt == 1:
        now_val = max(temp.keys())
    return max_cnt, now_val, now_val_temp


answer = 0
for i in range(int(input())):
    a = list(map(int, input().split()))
    result = 0
    cnt, val, anat = count(a)
    if cnt == 4:
        result += 50000+val*5000
    elif cnt == 3:
        result += 10000+val*1000
    elif cnt == 2 and anat == 0:
        result += 1000+val*100
    elif cnt == 2 and anat != 0:
        result += 2000+val*500+anat*500
    else:
        result += val*100
    answer = max(result, answer)
print(answer)
