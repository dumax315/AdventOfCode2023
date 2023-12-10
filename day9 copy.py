from aocd import get_data

res = 0
listOfLines = get_data(day=9, year=2023).split("\n")
# listOfLines = open("day9full.txt", "r").read().split("\n")

def allZeros(lastValues):
    for val in lastValues:
        if val != 0:
            return False
    return True

for i, line in enumerate(listOfLines):
    
    print(f"line #{i} \n{line}")

    lastValues = []
    temp = [int(x) for x in line.split().__reversed__()]
    while(not allZeros(temp)):
        lastValues.append(temp[-1])
        if(len(temp) == 1):
            lastValues.append(0)
            break
        else:
            print(temp)
            superTemp = []
            for i in range(len(temp)-1):
                superTemp.append(temp[i+1]-temp[i])
            temp = superTemp
    print(lastValues)
    partRes = sum(lastValues)
    print(partRes)
    res+=partRes



print(res)
from aocd import submit
submit(res, part="b", day=9, year=2023)