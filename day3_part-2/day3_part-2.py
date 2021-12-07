linesArray = []
toDeleteArray = []
filteredSelections = []
gammaRate = ""
epsilionRate = ""
def countCol(col, mode):
    zeroCount = 0
    oneCount = 0

    for i in filteredSelections:
        if int(i[col]) == 0:
            zeroCount+=1
        else:
            oneCount+=1
    #print("zeroCount: {}\noneCount: {}".format(zeroCount,oneCount))
    
    if mode == "higher":
        if zeroCount > oneCount:
            return 0
        elif zeroCount == oneCount:
            return 1
        else:
            return 1

    if mode == "lower":
        if zeroCount < oneCount:
            return 0
        elif zeroCount == oneCount:
            return 0
        else:
            return 1


def deleteLine(col,commonNum):
    global filteredSelections
    y = 0

    for line in filteredSelections:
        #print("number: {}\ncol: {}\nbit: {}\ncommonNum {}\n".format(line,col,line[col],commonNum))
        if len(filteredSelections) == 1:
            return filteredSelections[0]
        if line[col] != str(commonNum):
            toDeleteArray.append(line)

    filteredSelections = list(filter(lambda x: x not in toDeleteArray,linesArray))
    return filteredSelections[0]

with open('input.txt') as file:
        for line in file:
            linesArray.append(line.strip())
            filteredSelections = linesArray

        for i in range(12):
            oxygen = deleteLine(i, countCol(i, "higher"))
        filteredSelections = linesArray
        toDeleteArray = []
        for x in range(12):
            co2 = deleteLine(x, countCol(x, "lower"))

        print("oxygen:", int(oxygen, 2))
        print("co2:", int(co2, 2))
        print("Power consumption:",int(co2, 2) * int(oxygen, 2))









