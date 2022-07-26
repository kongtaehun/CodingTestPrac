
SECOND = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10]
str = input()
result = 0
for i in str:
    if i == 'A' or i == 'B' or i == 'C':
        result += SECOND[2]
    elif i == 'D' or i == 'E' or i == 'F':
        result += SECOND[3]
    elif i == 'G' or i == 'H' or i == 'I':
        result += SECOND[4]
    elif i == 'J' or i == 'K' or i == 'L':
        result += SECOND[5]
    elif i == 'M' or i == 'N' or i == 'O':
        result += SECOND[6]
    elif i == 'P' or i == 'Q' or i == 'R' or i == 'S':
        result += SECOND[7]
    elif i == 'T' or i == 'U' or i == 'V':
        result += SECOND[8]
    elif i == 'W' or i == 'X' or i == 'Y' or i == 'Z':
        result += SECOND[9]
print(result)
