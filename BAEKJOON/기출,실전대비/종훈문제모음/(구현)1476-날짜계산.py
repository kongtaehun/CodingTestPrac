if __name__ == '__main__':
    e, s, m = map(int, input().split())
    E, S, M = 1, 1, 1
    year = 1

    while True:
        year += 1
        E += 1
        if E > 15:
            E = 1
        S += 1
        if S > 28:
            S = 1
        M += 1
        if M > 19:
            M = 1
        # print(E, S, M, year)
        if E == e and S == s and M == m:
            if year == 7981:
                print(1)
            else:
                print(year)
            break
