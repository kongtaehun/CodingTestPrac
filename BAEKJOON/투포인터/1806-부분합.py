n, s = map(int, input().split())
nums = list(map(int, input().split()))

start = 0
end = 0
now = int(1e9)
sumval = nums[start]

while True:
    if sumval >= s:
        now = min(now, end-start+1)
        sumval -= nums[start]
        start += 1
    else:

        end += 1
        if end == n:
            break
        sumval += nums[end]

print(now if now != int(1e9) else 0)
