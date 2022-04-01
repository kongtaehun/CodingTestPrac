# 123402
a = input()
mid_idx = int(len(a)/2)  # 3
sum1 = 0
sum2 = 0
for i in range(mid_idx):
    sum1 = sum1 + int(a[len(a)-1-i])
    sum2 = sum2 + int(a[i])

print("LUCKY" if sum1 == sum2 else "READY")
