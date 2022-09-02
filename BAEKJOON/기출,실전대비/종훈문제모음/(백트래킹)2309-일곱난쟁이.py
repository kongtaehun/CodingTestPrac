flag = 0


def bt(depth):
    # print(result)
    global flag
    if flag == 1:
        return
    if depth == 7:
        if sum(result) == 100:
            result.sort()
            for i in result:
                print(i)
            flag = 1
            return
    else:
        for i in range(9):
            if visited[i] == 0:
                result.append(nums[i])
                visited[i] = 1
                bt(depth+1)
                result.pop()
                visited[i] = 0


if __name__ == '__main__':
    nums = []
    visited = [0]*(9)
    for i in range(9):
        nums.append(int(input()))
    result = []
    bt(0)
