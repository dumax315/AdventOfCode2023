from functools import lru_cache

import time
start_time = time.time()
with open("day16.txt", "r") as f:
  data = [[y for y in x] for x in f.read().split("\n")]



def testSide(row, col, rowChange, colChange):

    res = 0

    # for i, line in enumerate(data):
    #   print(f"line {i} ={line}")

    d2 = [[0 for x in range(len(data[0]))] for y in range(len(data))]
    alreadyDone = set()


    def shineLight(row, col, rowChange, colChange,alreadyDone):
        # print(alreadyDone)
        if((row, col, rowChange, colChange) in alreadyDone):
            # print(len(alreadyDone))
            return []
        
    
        
        alreadyDone.add((row, col, rowChange, colChange))
        if(row < 0 or col < 0 or row >= len(data) or col >= len(data[0])):
            return []
        d2[row][col] = 1
        
        if(data[row][col] == "." or (data[row][col] == "|" and rowChange != 0) or (data[row][col] == "-" and colChange != 0)):
            return [[row+rowChange, col+colChange, rowChange, colChange]]
            shineLight(row+rowChange, col+colChange, rowChange, colChange)
        elif(data[row][col] == "|"):
            return [[row-1, col+0, -1, 0],[row+1, col+0, 1, 0]]
            shineLight(row+1, col+0, 1, 0)
            shineLight(row-1, col+0, -1, 0)
        elif(data[row][col] == "-"):
            return [[row+0, col+1, 0, 1],[row+0, col-1, 0, -1]]
            shineLight(row+0, col+1, 0, 1)
            shineLight(row+0, col-1, 0, -1)

        elif(data[row][col] == "\\"):
            return [[row+colChange, col+rowChange, colChange, rowChange]]
            shineLight(row+colChange, col+rowChange, colChange, rowChange)
        elif(data[row][col] == "/"):
            return [[row+colChange*-1, col+rowChange*-1, colChange*-1, rowChange*-1]]
            shineLight(row+colChange*-1, col+rowChange*-1, colChange*-1, rowChange*-1)
        




    stack = []
    stack.extend(shineLight(row, col, rowChange, colChange,alreadyDone))
    while(len(stack) > 0):
        tempStack = []
        for item in stack:
            tempStack.extend(shineLight(item[0], item[1], item[2], item[3],alreadyDone))
        # print(tempStack)
        stack = tempStack 
        
        

    for row in d2:
        # print(row)
        for item in row:
            res+=item

    # print(res)
    return res

max = 0
for i in range(len(data)):
    cur = testSide(0, i, 1, 0)
    if( cur > max):
        max = cur

    cur = testSide(len(data[0])-1, i, -1,0)
    if( cur > max):
        max = cur

for i in range(len(data[0])):
    cur = testSide(i, 0, 0,1)
    if( cur > max):
        max = cur

    cur = testSide(i, len(data)-1, 0,-1)
    if( cur > max):
        max = cur



print(max)
print("--- %s seconds ---" % (time.time() - start_time))
# from aocd import submit
# submit(max, part="b", day=16, year=2023)