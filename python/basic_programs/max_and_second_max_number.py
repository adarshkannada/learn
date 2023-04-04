pos = 0
max = 0

numList = [-5, -1, -1, -10, -2, -2, -6, -1, -4, 50]


def checkmax():
    global pos, max, numList
    print("list before modification", numList)
    max = numList[0]
    for i in range(1, len(numList)):
        if max < numList[i]:
            max = numList[i]
            pos = i
    numList.remove(numList[pos])
    print("list after modification", numList)


# print(numList)
checkmax()
print("first run position= ", pos)
print("first run value= ", max)
checkmax()
print("second run position= ", pos)
print("second run value= ", max)
