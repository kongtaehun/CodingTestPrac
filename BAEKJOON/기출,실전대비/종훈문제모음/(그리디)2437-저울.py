

if __name__ == '__main__':
    # 추들을 조합하여 측정할 수 없는 정수
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()

    target = 1
    for now in nums:
        if now > target:
            break
        target += now
    print(target)
