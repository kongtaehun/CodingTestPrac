strr = input()
numStart = 0
numList = []
calList = []
for i in range(len(strr)):
    if strr[i] == '-' or strr[i] == '+':
        calList.append(strr[i])
        numList.append(int(strr[numStart:i]))
        numStart = i+1
numList.append(int(strr[numStart:]))


result = numList[0]
flag = False
for i in range(len(calList)):
    # 괄호가 안 열렸을 때 (0) 그리고 -를 만났을 때
    if calList[i] == "-" and flag == False:
        result -= numList[i+1]
        flag = True
    # 괄호가 열려있고 -를 만났을 떄
    elif calList[i] == "-" and flag == True:
        result -= numList[i+1]
    # 괄호가 열려있고 +를만났을 떄
    elif calList[i] == "+" and flag == True:
        result -= numList[i+1]
    # 괄호가 닫혀있고 +일때
    elif calList[i] == "+" and flag == False:
        result += numList[i+1]


print(result)
