from collections import Counter
INF = int(1e9)
# K개부터 슬라이딩 윈도우
# 슬라이딩 윈도우의 길이를 이분탐색으로??
for i in range(int(input())):
    string = list(input())
    k = int(input())
    min_len = INF
    max_len = 0
    temp = dict(Counter(string))
    for key in temp.keys():
        char_idx = []
        # key 알파벳의 인덱스 리스트
        if temp[key] >= k:
            for i in range(len(string)):
                if string[i] == key:
                    char_idx.append(i)
        # char들
        for i in range(len(char_idx)-k+1):
            # 인덱스의 차이
            min_len = min(min_len, char_idx[i+k-1]-char_idx[i])
            max_len = max(max_len, char_idx[i+k-1]-char_idx[i])
    if min_len == INF and max_len == 0:
        print(-1)
    else:
        print(min_len+1, max_len+1)
