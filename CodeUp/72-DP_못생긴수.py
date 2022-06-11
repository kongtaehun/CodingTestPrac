

n = 10
ugly_num = []
ugly_num.append(1)

now2 = 2
now3 = 3
now5 = 5

idx2 = 0
idx3 = 0
idx5 = 0
i = 0
while i < n:
    ugly_num.append(min(now2, now3, now5))
    if(ugly_num[i] == now2):
        idx2 += 1
        now2 = ugly_num[idx2]*2
    elif(ugly_num[i] == now3):
        idx3 += 1
        now3 = ugly_num[idx3]*3
    elif(ugly_num[i] == now5):
        idx5 += 1
        now5 = ugly_num[idx5]*5
    i += 1
    if ugly_num[i-1] == ugly_num[i]:
        ugly_num.pop(i)
        i -= 1
print(ugly_num)
