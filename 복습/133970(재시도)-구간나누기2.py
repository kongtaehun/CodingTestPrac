# 이분탐색
# target을 최소로하고 구간을 나누고 싶을 떄 구간의 개수
def check(target):
    minV = nums[0]
    maxV = nums[0]
    cnt = 1
    for i in range(n):
        minV = min(minV, nums[i])
        maxV = max(maxV, nums[i])
        if maxV-minV > target:
            cnt += 1
            minV = nums[i]
            maxV = nums[i]
    return cnt


def binary_search():
    start = 0
    end = max(nums)
    while start <= end:
        mid = (start+end)//2
        cnt = check(mid)
        if cnt <= m:
            end = mid - 1
        else:
            start = mid+1
    return start


if __name__ == '__main__':
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    print(binary_search())
