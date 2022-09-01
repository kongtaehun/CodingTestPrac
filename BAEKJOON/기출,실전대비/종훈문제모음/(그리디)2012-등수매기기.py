# 그리디하게 일단 오름차순 정렬
if __name__ == '__main__':
    n = int(input())
    nums = []
    for i in range(n):
        nums.append(int(input()))
    nums.sort()
    now = 1
    answer = 0
    for i in range(n):
        answer += abs((i+1)-nums[i])

    print(answer)
