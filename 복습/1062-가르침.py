# 읽을 수 있는 단어수 반환
known_word = [set()]


def bt(depth, chrs, visited, start, k, words):
    global known_word
    if depth == k:
        print(count(words, known_word))
        return
    else:
        for i in range(start, len(chrs)):
            if visited[i] == 0:
                visited[i] = 1
                known_word.add(chrs[i])
                bt(depth+1, chrs, visited, i, k, words)
                known_word.remove(chrs[i])
                print(chrs[i])
                visited[i] = 0


def count(words, known_word):
    cnt = 0
    print(words, known_word)
    for word in words:
        flag = 0
        for i in word:
            if i not in known_word:
                flag = 1
                break
        if flag == 0:
            cnt += 1
    return cnt


def solution():
    global known_word
    n, k = map(int, input().split())
    words = []
    chrs = set()
    for _ in range(n):
        temp = input()
        words.append(temp[4:-4])
        for i in temp[4:-4]:
            chrs.add(i)

    if k < 5:
        print(0)
        return

    temp = ['a', 'n', 't', 'i', 'c']
    for i in temp:
        known_word.add(i)
    k -= 5
    chrs = list(chrs)
    visited = [0]*(len(chrs))
    # 선택가능한 개수 k개
    # 선택가능한단어 chrs
    bt(0, chrs, visited, 0, k, words)
    print(words)


solution()
