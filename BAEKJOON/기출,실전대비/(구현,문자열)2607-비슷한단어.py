def check(word1, word2):
    if abs(len(word1) - len(word2)) <= 1:
        len_word2 = 0
        word2_list = list(word2)
        word1_list = list(word1)
        for i in word1_list:
            if i in word2_list:
                word2_list.remove(i)
        len_word2 = len(word2_list)
        word2_list = list(word2)
        for i in word2_list:
            if i in word1_list:
                word1_list.remove(i)
        if len(word1_list) <= 1 and len_word2 <= 1:
            return True

    return False


if __name__ == '__main__':
    n = int(input())
    origin = input()
    words = []
    cnt = 0
    for i in range(n-1):
        if check(origin, input()):
            cnt += 1
    print(cnt)
