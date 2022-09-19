import sys
input = sys.stdin.readline


def check(known_words, words):
    result = 0
    for word in words:
        flag = 0
        for w in word:
            if not known_words[ord(w)-ord('a')]:
                flag = 1
                break
        if flag != 1:
            result += 1

    return result


def bt(idx, depth):
    global answer
    if depth == m:
        # print(check(known_words, words))
        answer = max(answer, check(known_words, words))
    else:
        for i in range(idx, 26):
            if known_words[i] == 0:
                known_words[i] = 1
                bt(i, depth+1)
                known_words[i] = 0


if __name__ == '__main__':
    n, m = map(int, input().split())
    known_words = [0]*26
    for i in ['a', 'n', 't', 'i', 'c']:
        known_words[ord(i)-ord('a')] = 1
    m = m - 5
    words = []
    for _ in range(n):
        temp = input()
        words.append(set(temp[4:-5]))

    answer = 0
    if m == 26:
        # print("1")
        answer = n
    elif m < 0:
        # print("2")
        answer = 0
    else:
        bt(0, 0)
    print(answer)



import sys
input = sys.stdin.readline


def check(known_words, words):
    result = 0
    for word in words:
        if not (word-known_words):
            result += 1

    return result



