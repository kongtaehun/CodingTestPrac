
# 2. 최적인지 특정값찾는 건지 확인
# 이문제는 최적의 랜선길이에 수렴해야함

# 1. 기준 만들기
# 기준 = 랜선의 길이
#   최소 0
#   최대 랜선길이 최댓값

def getLenCount(len, nums):
    count = 0
    for i in nums:
        if len != 0:
            count += i//len
    return count


def binary_search(nums, target):
    end = max(nums)
    start = 0

    while start <= end:              # todo 부등호 화깅ㄴ
        mid = (start+end)//2
        now = getLenCount(mid, nums)
        if now < target:
            end = mid-1
        else:
            start = mid + 1
    return start, mid, end


k, n = map(int, input().split())
nums = []
for i in range(k):
    nums.append(int(input()))
s, m, e = binary_search(nums, n)
print(e)
