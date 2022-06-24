# 백트래킹으로 풀어봤으나 재귀제한걸렸음!
# 답은 나오는 정도
def dfs(x, start):
    global count
    if x == n:
        # 저장하기

        count += 1
    else:
        for i in range(start, 10):
            temp.append(i)
            dfs(x+1, i)
            temp.pop()


if __name__ == '__main__':
    temp = []
    n = int(input())
    visited = [0]*10
    count = 0
    dfs(1, 0)
    print(count)
