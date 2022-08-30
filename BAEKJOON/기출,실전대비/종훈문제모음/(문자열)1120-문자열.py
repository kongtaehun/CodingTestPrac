if __name__ == '__main__':
    a, b = map(str, input().split())
    result = 0
    for i in range(len(b)-len(a)+1):
        cnt = 0
        for j in range(len(a)):
            if a[j] == b[i+j]:
                cnt += 1
        result = max(result, cnt)
    print(len(a)-result)
