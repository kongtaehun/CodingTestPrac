# 이분탐색으로 풀었다.
def check(words, x):
    temp = set()
    for i in range(len(words)):
        if len(words) < x:
            continue
        if words[i][:x] in temp:
            # 해당부분에서 문제가 있었음
            return True, words[i][:x]
        else:
            temp.add(words[i][:x])
    return False, '0'


# x로 시작하는 첫번째 비슷한 단어 찾기
def serchWord(words, x):
    result = []
    for i in range(len(words)):
        if x in words[i]:
            result.append(words[i])
        if len(result) == 2:
            return result

# x로 시작하는 첫번째 비슷한 단어 찾기


def serchWord(words, x):
    result = []
    result_idx = []
    for i in range(len(words)):
        if words[i][:x] in result:
            return result_idx[result.index(words[i][:x])], i
        else:
            result.append(words[i][:x])
            result_idx.append(i)


def binarySearch(words, max_word_len):
    start = 0
    end = max_word_len
    start_word = ''
    while start <= end:
        mid = (start+end)//2
        check_bool, check_val = check(words, mid)
        if check_val != '0':
            start_word = check_val
        if not check_bool:
            end = mid - 1
        else:
            start = mid+1

    return start-1, start_word


if __name__ == '__main__':
    n = int(input())
    words = []
    # 최대 단어 길이
    max_word_len = 0
    for i in range(n):
        temp = input()
        if temp in words:
            continue
        max_word_len = max(max_word_len, len(temp))
        words.append(temp)

    start_cnt, start_words = binarySearch(words, max_word_len)
    result = serchWord(words, start_cnt)
    for i in result:
        print(words[i])
