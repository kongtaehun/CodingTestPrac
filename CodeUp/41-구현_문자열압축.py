# 내풀이
# 내 풀이는 3번이상의 연속된 세트가 나오면 압축앞에 숫자를 표현 못함
#a = input()
a = 'aabbaccc'
max_comp = len(a)//2
comp = [len(a) for i in range(max_comp+1)]
print(len(a))

for k in range(1, max_comp+1):
    i = 0
    count = 0
    while i+k+k <= len(a):
        # 1
        if a[i:i+k] == a[i+k:i+k+k]:
            comp[k] = comp[k]-k
            count += 1
        i = i+k
    comp[k] += count

print(comp)

# 정답
a = 'abcabcdede'
max_comp = len(a)//2
comp = [len(a) for i in range(max_comp+1)]
print(len(a))

for k in range(1, max_comp+1):
    i = 0
    count = 0
    prev = a[0:k]
    for i in range(1, int(len(a)//k)+1):
        now = a[i*k: i*k+k]
        # 현재와 전 순서가 같을 떄
        if prev == now:
            comp[k] -= k
            count = +1
        # 같다가 바뀌었거나 다를떄
        else:
            if count >= 2:
                count = 1
    comp[k] += count

print(min(comp))
