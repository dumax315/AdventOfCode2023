from aocd import get_data

# map = [list(row) for row in open("day10.txt", "r").read().split("\n")]
map = [list(row) for row in get_data(day=10, year=2023).split("\n")]
# print(map)
lengthOfPipe = 0

posRow = 0
posCol = 0
startR = 0
startC = 0
for row in range(len(map)):
    for pipe in range(len(map[0])):
        # print(len(map[0]))
        # print(row,pipe)
        if(map[row][pipe] == "S"):
            startR, posRow = row, row
            startC, posCol = pipe, pipe
            print(row,pipe)

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
drawKey = {
    "|":".*#..#.*#",
    "-":"###*.*...",
    "L":".*#..*...",
    "J":"#*.*.....",
    "7":"...*..#*.",
    "F":".....*.*#",
}

order = [0,1,2,5,8,7,6,3,0,1,2,5,8,7,6,3]
# ***
# ***
# ***

blocksInside = [[0 for x in range(len(map[0]))] for xx in range(len(map))]
# input(blocksInside)
posCol -= 1
lastPosInd = 5
ii = 0
print()
sidesInside = {
    0:True,
    2:True,
    6:False,
    8:True
}
mapFromNumToChange = {
    0:[-1,-1],
    1:[-1,0],
    2:[-1,1],
    3:[0,-1],
    4:[0,0],
    5:[0,1],
    6:[1,-1],
    7:[1,0],
    8:[1,1]
}

while ((posCol != startC or posRow != startR) and ii<10):
    # print(posRow,posCol)
    # print(map[posRow][posCol])
    # print(f"lastPosComming {lastPosInd}")
    blocksInside[posRow][posCol] = 1


    if(lastPosInd == 1):
        lookFor = 2
        fillWith = 8
    elif(lastPosInd == 3):
        lookFor = 0
        fillWith = 2
    elif(lastPosInd == 5):
        lookFor = 2
        fillWith = 0
    elif(lastPosInd == 7):
        lookFor = 6
        fillWith = 0


    bottomRight = sidesInside[2]
    curInside = False
    curSymbol = ""
    for i in order:
        if(curSymbol == "" and i == lookFor):
            curSymbol = drawKey[map[posRow][posCol]][i]
            curInside = sidesInside[fillWith]
            # print("start")
        if(curSymbol != "" and drawKey[map[posRow][posCol]][i] != curSymbol and drawKey[map[posRow][posCol]][i] != "*"):
            if(curSymbol == "."):
                curInside = (not curInside)
                curSymbol = "#"
            elif(curSymbol == "#"):
                curInside = (not curInside)
                curSymbol = "."
        if(curSymbol != ""):
            # print(f"cur = {curSymbol} vs {drawKey[map[posRow][posCol]][i]} curentIndside = {curInside}")
            sidesInside[i] = curInside
            try:
                if(blocksInside[posRow + mapFromNumToChange[i][0]][posCol + mapFromNumToChange[i][1]] == 0):
                    val = 2
                    if(curInside):
                        # print("insided")
                        val = 3
                    blocksInside[posRow + mapFromNumToChange[i][0]][posCol + mapFromNumToChange[i][1]] = val 
            except:
                # print("outside")
                pass

    # print(sidesInside)


    for i,ch in enumerate(drawKey[map[posRow][posCol]]):
        if(i != lastPosInd and ch == "*"):
            posRow += (i//3) -1
            posCol += (i%3)  -1
            # print(((i%3) -1))
            lastPosInd = 4 - ((i%3) -1) - ((i//3) -1)*3

            
            break
    lengthOfPipe+=1
    # ii+=1
    
print(lengthOfPipe)
print(lengthOfPipe/2)


# print(blocksInside)
filling = False
for i, row in enumerate(blocksInside):
    for j, item in enumerate(row):
        
        if(blocksInside[i][j] == 2):
            filling = True
        elif(filling and blocksInside[i][j] == 0):
            
            blocksInside[i][j] = 2
        else:
            filling = False

toSave = ""
for row in blocksInside:
    for item in row:
        toSave+=str(item)
    toSave += "\n"
f = open("map.txt", "w")
f.write(toSave)
f.close()
# I then opened the file counted the 2s with contorl+F