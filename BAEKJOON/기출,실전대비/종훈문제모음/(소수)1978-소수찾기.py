def getPrim(n):
    if n == 1:
        return False
    for i in range(2, n):
        # 나머지는 몫을 제외한 나머지 값을 의미한다.
        if n % i == 0:
            return False
    return True


n = int(input())
nums = list(map(int, input().split()))
answer = 0
for i in nums:
    if getPrim(i):
        answer += 1
print(answer)

# 2부터 자기자신까지 나누기하기
