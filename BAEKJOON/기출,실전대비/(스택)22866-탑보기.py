import sys
input = sys.stdin.readline


def searchBuilding(start, end, step):
    global cnt
    stk = []
    for i in range(start, end, step):
        while len(stk) > 0 and nums[stk[-1]] <= nums[i]:
            stk.pop()
        if len(stk) > 0 and (result_val[i] == 0 or abs(stk[-1] - i) < abs(result_val[i]-i)):
            result_val[i] = stk[-1]
        cnt[i] += len(stk)
        stk.append(i)


if __name__ == '__main__':
    n = int(input())
    nums = [0]+list(map(int, input().split()))
    cnt = [0]*(n+1)
    result_val = [0]*(n+1)
    searchBuilding(1, n+1, 1)
    searchBuilding(n, 0, -1)
    for i in range(1, n+1):
        if cnt[i] == 0:
            print(0)
        else:
            print(cnt[i], result_val[i])
