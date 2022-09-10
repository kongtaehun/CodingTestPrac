# 중복없는 product
def bt(depth, start):
    global answer, result
    if depth == n:
        answer.add(result)
    else:
        for i in range(start, 4):
            result += nums[i]
            bt(depth+1, i)
            result -= nums[i]


n = int(input())
nums = [1, 5, 10, 50]
answer = set()
result = 0
bt(0, 0)
print(len(answer))
