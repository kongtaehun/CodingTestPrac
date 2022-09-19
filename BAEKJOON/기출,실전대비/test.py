import sys
input = sys.stdin.readline


def check(known_words, words):
    result = 0
    for word in words:
        if not (word-known_words):
            result += 1

    return result


def bt(idx, depth):
    global answer
    if depth == m:

        # print(check(known_words, words))
        answer = max(answer, check(known_words, words))
    else:
        for i in range(idx, len(possible_words)):
            if visited[i] == 0:
                visited[i] = 1
                known_words.add(possible_words[i])
                bt(i, depth+1)
                visited[i] = 0
                known_words.remove(possible_words[i])


if __name__ == '__main__':
    n, m = map(int, input().split())
    known_words = set()
    known_words.add('a')
    known_words.add('n')
    known_words.add('t')
    known_words.add('i')
    known_words.add('c')
    # 학습이 가능한 단어들
    possible_words = set()
    m = m - 5
    words = []
    for _ in range(n):
        temp = input()
        words.append(set(temp[4:-5]))

        for i in temp:
            if i not in known_words:
                possible_words.add(i)

    possible_words = list(possible_words)
    # print(possible_words)
    visited = [0]*(len(possible_words))
    answer = 0

    if m >= len(possible_words):
        answer = n
    else:
        bt(0, 0)
    print(answer)
