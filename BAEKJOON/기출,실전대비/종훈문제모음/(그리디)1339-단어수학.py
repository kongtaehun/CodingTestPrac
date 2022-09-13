
from re import A


if __name__ == '__main__':
    NUMS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ALPH = {}
    RESULT_ALPH = {}
    for i in range(65, 91):
        ALPH[chr(i)] = [-1, chr(i)]
        RESULT_ALPH[chr(i)] = -1
    # 최대자리수 부터 가장 중복이 많은 것을
    strs = []
    max_len = 0
    for i in range(int(input())):
        temp = input()
        max_len = max(len(temp), max_len)
        strs.append(temp)

    # 최대자리수 맞추기
    for i in range(len(strs)):
        temp = ['0']*(max_len - len(strs[i]))
        strs[i] = ''.join(temp)+strs[i]

    # 숫자 삽입
    for i in range(max_len):
        for j in range(len(strs)):
            if strs[j][i] != '0':

                if ALPH[strs[j][i]][0] == -1:
                    ALPH[strs[j][i]][0] = 10**(max_len-i-1)
                else:
                    ALPH[strs[j][i]][0] += 10**(max_len-i-1)

    for i in sorted(ALPH.values(), reverse=True):
        # print(i)
        if i[0] != -1:
            if RESULT_ALPH[i[1]] == -1:
                RESULT_ALPH[i[1]] = NUMS.pop()

    answer = 0
    for strr in strs:
        temp = []
        for chr in strr:
            if chr != '0':
                temp.append(RESULT_ALPH[chr])
        answer += int(''.join(list(map(str, temp))))
    print(answer)
