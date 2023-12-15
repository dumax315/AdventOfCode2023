# from aocd import get_data
# data = get_data(day=14, year=2023).split("\n")
# itemList = [[data[x][i] for x in range(len(data))] for i in range(len(data[0]))]

f = open("day14.txt", "r")
lineList = f.read().split("\n")
f.close()
itemList = [[lineList[x][i] for x in range(len(lineList))] for i in range(len(lineList[0]))]

def cycle():
    for lineInd in range(len(itemList)):
        
        for i in range(len(itemList[lineInd])):
            if(itemList[lineInd][i] == "O"):
                itemList[lineInd][i] = "."
                revI = i-1
                while(revI >=0):
                    if itemList[lineInd][revI] != ".":
                        itemList[lineInd][revI+1] = "O"
                        break
                    revI -= 1
                if(revI == -1):
                    itemList[lineInd][0] = "O"
        # print(f"line #{i} \n{''.join(itemList[lineInd])}")

    for lineInd in range(len(itemList[0])):
        
        for i in range(len(itemList)):
            if(itemList[i][lineInd] == "O"):
                itemList[i][lineInd]  = "."
                revI = i-1
                while(revI >=0):
                    if itemList[revI][lineInd]  != ".":
                        itemList[revI+1][lineInd]  = "O"
                        break
                    revI -= 1
                if(revI == -1):
                    itemList[0][lineInd]  = "O"
    for lineInd in range(len(itemList)):
        
        for i in range(len(itemList[lineInd])-1,-1,-1):
            if(itemList[lineInd][i] == "O"):
                itemList[lineInd][i] = "."
                revI = i+1
                while(revI <len(itemList[lineInd])):
                    if itemList[lineInd][revI] != ".":
                        itemList[lineInd][revI-1] = "O"
                        break
                    revI += 1
                if(revI == len(itemList[lineInd])):
                    itemList[lineInd][len(itemList[lineInd])-1] = "O"
        # print(f"line #{i} \n{''.join(itemList[lineInd])}")

    for lineInd in range(len(itemList[0])):
        
        for i in range(len(itemList)-1,-1,-1):
            if(itemList[i][lineInd] == "O"):
                itemList[i][lineInd]  = "."
                revI = i+1
                while(revI < len(itemList[0])):
                    if itemList[revI][lineInd]  != ".":
                        itemList[revI-1][lineInd]  = "O"
                        break
                    revI += 1
                if(revI == len(itemList[0])):
                    itemList[len(itemList[0])-1][lineInd]  = "O"
        # print(f"line #{i} \n{''.join(itemList[lineInd])}")
import time
start_time = time.time()
times = 100000
repeatChecker = []
for i in range(times):
    if(i % 100 == 0):
        print(i/times)
        print("--- %s seconds ---" % (time.time() - start_time))
    cycle()


    res = 0
    for lineInd in range(len(itemList)):
        for i in range(len(itemList[lineInd])):
            if(itemList[lineInd][i] == "O"):
                res +=len(itemList[lineInd])-i
    repeatChecker.append(res)

print(itemList)
repeatChecker = repeatChecker[1000:]

i=0
for i in range(1,10000):
    found = True
    repeats = 0
    # print(f"{repeatChecker[0:i] }!= { repeatChecker[i+i*repeats:i*2+i*repeats]}")
    for repeats in range((len(repeatChecker)//2)//i):
    
        if repeatChecker[0:i] != repeatChecker[i+i*repeats:i*2+i*repeats]:
            found= False
            break
        print(f"{repeatChecker[0:i] }!= { repeatChecker[i+i*repeats:i*2+i*repeats]}")
    if found:
        print(i)
        break

print(i)
print(repeatChecker[(1000000000-1001)%i])
print("--- %s seconds ---" % (time.time() - start_time))