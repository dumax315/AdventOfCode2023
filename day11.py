from aocd import get_data

res = 0
lineArr = [[y for y in x] for x in get_data(day=11, year=2023).split("\n")]
# lineArr = [[y for y in x] for x in open("day11.txt", "r").read().split("\n")]
# print(lineArr)
# print(["." for x in range(len(lineArr[0]))])
extraRowInds = []
i = 0
while i < len(lineArr):
    shouldExp = True
    for area in lineArr[i]:
        if(area == "#"):
            shouldExp = False
            break
    if(shouldExp):
        # print(i)
        extraRowInds.append(i)
        # lineArr.insert(i, ["!" for x in range(len(lineArr[i]))])
        # i+=1
    i+=1


extraColInds = []
i = 0
while i < len(lineArr[0]):
    shouldExp = True
    for row in range(len(lineArr)):
        if(lineArr[row][i] == "#"):
            shouldExp = False
            break
    if(shouldExp):
        # print(i)
        extraColInds.append(i)
        # for row in range(len(lineArr)):
        #     lineArr[row].insert(i, "!")
        # i+=1
    i+=1
print(f"row = {extraRowInds}")
print(f"col = {extraColInds}")
numberOfGal = 0
galPos = []
for row in range(len(lineArr)):
    for i in range(len(lineArr[row])):
        if(lineArr[row][i] == "#"):
            lineArr[row][i] = numberOfGal
            galPos.append([row,i])
            numberOfGal+=1
print(galPos)

def getExpand(rc, curPos, gal):
    key = extraRowInds
    if(rc == "col"):
        key = extraColInds
    
    numOfCross = 0
    if(curPos > gal):
        temp = curPos
        curPos = gal
        gal = temp
    
    for i in range(curPos,gal):
        
        if i in key:
            numOfCross+=1
    # print(numOfCross)
    return numOfCross*999999
    # print(f"{curPos} - {gal} rc = {rc} hit = {numOfCross}")
    # return numOfCross*1
    

while (len(galPos) > 0):
    curPos = galPos[0]
    galPos.pop(0)
    for gal in galPos:
        res+= abs(curPos[0] - gal[0]) + getExpand("row", curPos[0], gal[0])
        res+= abs(curPos[1] - gal[1]) + getExpand("col", curPos[1], gal[1])
        # res -=1

# # print(lineArr)

# # for i, line in enumerate(listOfLines):
    
# #     print(f"line #{i} \n{line}")

print(res)
# toSave = ""
# for row in lineArr:
#     for item in row:
#         toSave+=str(item)
#     toSave += "\n"
# f = open("map.txt", "w")
# f.write(toSave)
# f.close()

# from aocd import submit
# submit(res, part="b", day=11, year=2023)