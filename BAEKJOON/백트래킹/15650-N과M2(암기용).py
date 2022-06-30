

def bt(x, start):
    if x == m:
        print(result_arr)
    else:
        for i in range(start, n+1):
            if visited[i] == 0:
                visited[i] = 1
                result_arr.append(i)
                bt(x+1, i)
                visited[i] = 0
                result_arr.pop()


if __name__ == '__main__':
    n, m = map(int, input().split())
    visited = [0]*(n+1)
    result_arr = []
    bt(0, 1)
