def tp():
    global result
    l = 0
    r = 0
    while l <= r and r <= n:
        total = sum(nums[l:r])
        if total == m:
            result += 1
            r += 1
        elif total < m:
            r += 1
        else:
            l += 1


if __name__ == '__main__':
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    # 투포인터
    result = 0
    tp()
    print(result)
