n = int(input())
nums = [0]*1001
mx_idx, mx_val = 0, 0
for i in range(n):
    a, b = map(int, input().split())
    if mx_val < b:
        mx_val = b
        mx_idx = a
    nums[a] = b

# 왼쪽에서부터 오름차로 면적계산
mx = 0
area = 0
for i in range(mx_idx):
    if nums[i] > mx:
        mx = nums[i]
        area += mx
    else:
        area += mx
# 오른쪽에서부터 오름차로 면적계산
mx = 0
for i in range(1000, mx_idx, -1):
    if nums[i] > mx:
        mx = nums[i]
        area += mx
    else:
        area += mx


# 최댓값 기둥 면적추가
area += mx_val

print(area)
# 최댓값을 중심으로 오름차순만들기
# 양끝에서 중앙으로
