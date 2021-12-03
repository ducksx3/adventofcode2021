def main():
    entries = []
    windowIndex = 0
    sum1 = 0 
    sum2 = 0
    sum3 = 0
    result = 0
    lastResult = 0
    higherCount = 0
    
    with open('input.txt', 'r') as file:
        for line in file:
            entries.append(int(line.strip()))

    for i in entries:
        sum1 = entries[windowIndex]
        sum2 = entries[windowIndex+1]
        sum3 = entries[windowIndex+2]
        result = sum1+sum2+sum3
        print("{} + {} + {} = {}".format(sum1,sum2,sum3,result))
               
        if lastResult != 0 and result > lastResult:
            higherCount+=1

        if (windowIndex+3 < len(entries)):
                windowIndex = windowIndex+1
                lastResult = result
        else:
            break
    print(higherCount,"Increases")

main()