# from aocd import get_data

res = 0
# lineList = get_data(day=12, year=2023).split("\n")
lineList = open("day12full.txt", "r").read().split("\n")
    
import time
start_time = time.time()

dpArr = []

def checkLine(line, numsList, su, chStart, valCh):
    global dpArr
    if(line.count("#") > su or line.count("#")+line.count("?") < su):
        return 0
    
    startI = -1
    lVI = 0
    for i,ch in enumerate(line[chStart:]):
        if(ch == "?"):
            break
        if(startI == -1 and ch=="#"):
            startI = i
        if(startI != -1 and ch=="."):
            if(i-startI == numsList[valCh]):
                # print(startI)
                # print(line[chStart:])
                lVI = i+1
                valCh+=1
                startI = -1
            else:
                return 0
    chStart += lVI
    
        
    if(not "?" in line):
        # print(line)
        lineIndex=0
        while(lineIndex != len(line)-1 and line[lineIndex] == "."):
            lineIndex+=1

        
        if(line.count("#") != su):
            return 0
        for i, val in enumerate(numsList):
            for valCheck in range(val):
                if(lineIndex >= len(line) or line[lineIndex] == "."):
                    return 0
                lineIndex+=1
            if(i < len(numsList)-1 and (lineIndex >= len(line)-1 or line[lineIndex] != ".")):
                return 0
            while(lineIndex < len(line) and line[lineIndex] == "."):
                lineIndex+=1

        while(lineIndex < len(line)):
            if(line[lineIndex] == "#"):
                return 0
            lineIndex+=1
        # print(f"{line} = 1 at {valCh}")
        return 1
    
    if(((line.index("?")-1 >= 0) and line[line.index("?")-1] == ".") and dpArr[valCh][line.index("?")] != -1):
        # print(valCh)
        # print(dpArr[valCh][line.index("?")-1])
        # print(f"{line} = {dpArr[valCh][line.index('?')-1]} at {valCh} + {line.index('?')-1} !")
        return dpArr[valCh][line.index("?")-1]
    toReturn = checkLine(line.replace("?", "#", 1), numsList, su, chStart, valCh)
    toReturn += checkLine(line.replace("?", ".", 1), numsList, su, chStart, valCh)

    if((line.index("?")-1 >= 0) and line[line.index("?")-1] == "."):
        
        dpArr[valCh][line.index("?")-1] = toReturn
        # print(f"{line} = {dpArr[valCh][line.index('?')-1]} at {valCh} + {line.index('?')-1} *")
    return toReturn


for i, line in enumerate(lineList):
    print(f"line #{i} \n{line}")
    
    if(i % 10 == 0):
        print(f"line #{i} \n{line}")
        print("--- %s seconds ---" % (time.time() - start_time))
    li = [int(x) for x in line.split()[1].split(",")]*5
    # print(li)
    sumOfLi = sum(li)
    unpacked = (line.split()[0]+"?")*4 + line.split()[0]
    # print(line.split()[0])
    # print(unpacked)
    dpArr = [[-1 for x in range(len(unpacked))] for y in range(len(li)+1)]
    # print(dpArr)
    thisline = checkLine(unpacked, li, sumOfLi, 0, 0)
    # thisline = checkLine(line.split()[0], [int(x) for x in line.split()[1].split(",")], sum([int(x) for x in line.split()[1].split(",")]), 0, 0)

    # print(thisline)
    res += thisline
    

print(res)
print("--- %s seconds ---" % (time.time() - start_time))


# from aocd import submit
# submit(res, part="a", day=12, year=2023)