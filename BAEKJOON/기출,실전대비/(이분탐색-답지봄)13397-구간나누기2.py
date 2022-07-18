INF = int(1e9)


def isValid(mid):
    cnt = 1
    minV = nums[0]
    maxV = nums[0]

    # 구간점수가 mid값보다 큰 집합의 개수 조사
    for i in range(n):
        minV = min(minV, nums[i])
        maxV = max(maxV, nums[i])
        # 전체구간의 최댓값중 최솟값이므로
        # 전체구간에 대해서 구간점수가 mid보다 커야함
        # mid는 예상하는 구간점수 최댓값의 최솟값
        if maxV - minV > mid:
            cnt += 1
            maxV = nums[i]
            minV = nums[i]

    return cnt


def bs(nums):
    global result
    start = 0
    end = max(nums)
    while start <= end:
        mid = (start+end)//2
        if isValid(mid) <= m:
            end = mid - 1
            result = mid
        else:
            start = mid + 1


if __name__ == '__main__':
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    result = 0
    bs(nums)
    print(result)
