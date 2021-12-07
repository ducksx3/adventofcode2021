linesArray = []
gammaRate = ""
epsilionRate = ""
with open('input.txt') as file:
    for line in file:
        linesArray.append(line)

def countCol(col):
    zeroCount = 0
    oneCount = 0

    for i in linesArray:
        if int(i[col]) == 0:
            zeroCount+=1
        else:
            oneCount+=1
    print("zeroCount: {}\noneCount: {}".format(zeroCount,oneCount))
    
    if zeroCount > oneCount:
        return 0, 1
    else:
        return 1, 0

for x in range(12):
    commonNum, leastCommon = countCol(x)
    gammaRate += str(commonNum)
    epsilionRate += str(leastCommon)
    print("gammaRate:",gammaRate)
    print("epsilionRate:",epsilionRate)


print("Final binary gammarate is: ",gammaRate)
print("Final decimal gammarate is: ",int(gammaRate, 2))
print("Final binary epsilionRate is: ",epsilionRate)
print("Final decimal epsilionRate is: ",int(epsilionRate, 2))
print("Final power consumption:", int(gammaRate, 2) * int(epsilionRate, 2))