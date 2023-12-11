from aocd import get_data

res = 0
lineArr = [[y for y in x] for x in get_data(day=11, year=2023).split("\n")]
# lineArr = [[y for y in x] for x in open("day11.txt", "r").read().split("\n")]

# print(lineArr)
# print(["." for x in range(len(lineArr[0]))])
numLines = 1
i = 0
while i < len(lineArr):
    shouldExp = True
    for area in lineArr[i]:
        if(area == "#"):
            shouldExp = False
            break
    if(shouldExp):
        # print(i)
        for jj in range(numLines):
            lineArr.insert(i, ["!" for x in range(len(lineArr[i]))])
        i+=numLines
    i+=1

i = 0
while i < len(lineArr[0]):
    shouldExp = True
    for row in range(len(lineArr)):
        if(lineArr[row][i] == "#"):
            shouldExp = False
            break
    if(shouldExp):
        # print(i)
        for jj in range(numLines):
            for row in range(len(lineArr)):
                lineArr[row].insert(i, "!")
        i+=numLines
    i+=1

numberOfGal = 0
galPos = []
for row in range(len(lineArr)):
    for i in range(len(lineArr[row])):
        if(lineArr[row][i] == "#"):
            lineArr[row][i] = numberOfGal
            galPos.append([row,i])
            numberOfGal+=1
print(galPos)



while (len(galPos) > 0):
    curPos = galPos[0]
    galPos.pop(0)
    for gal in galPos:
        res+= abs(curPos[0] - gal[0])
        res+= abs(curPos[1] - gal[1])

# print(lineArr)

# for i, line in enumerate(listOfLines):
    
#     print(f"line #{i} \n{line}")

print(res)
toSave = ""
# for row in lineArr:
#     for item in row:
#         toSave+=str(item)
#     toSave += "\n"
# f = open("map.txt", "w")
# f.write(toSave)
# f.close()

# from aocd import submit
# submit(res, part="a", day=11, year=2023)