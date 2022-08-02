# 구간점수의최댓값 -> 배열점수
# 배열점수의 최솟값


# 배열점수가 mid가 가능한가? -> 배열점수가
# mid보다 큰 배열의 개수가 cnt 개있다.
def check(arr, mid):
    minV = arr[0]
    maxV = arr[0]
    cnt = 1
    for i in range(len(arr)):
        minV = min(arr[i], minV)
        maxV = max(arr[i], maxV)
        # 구간점수가 mid이상인 구간이 cnt개
        if maxV-minV > mid:
            cnt += 1
            minV = arr[i]
            maxV = arr[i]
    return cnt


def bs(arr, m):
    start = 0
    end = max(arr)

    while start <= end:
        mid = (start+end)//2
        isValid = check(arr, mid)
        if isValid <= m:
            end = mid-1
        else:
            start = mid+1
    return start, mid, end


if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    s, mid, e = bs(arr, m)
    print(s)
