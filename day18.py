with open("day18full.txt", "r") as f:
    lines =  f.read().split("\n")
import time
start_time = time.time()

import sys
sys.setrecursionlimit(100000)

blocks = []

pos = {"x":0,"y":0}

dirKey = {"R":(0,1),"L":(0,-1),"U":(-1,0),"D":(1,0)}
numKey = {0:(0,1),2:(0,-1),3:(-1,0),1:(1,0)}

for line in lines:
    print(line.split(" ")[2][2:7],line.split(" ")[2][7])
    # for i in range():
    blocks.append((pos["x"],pos["y"]))
    pos["x"] += numKey[int(line.split(" ")[2][7])][0] *int(line.split(" ")[2][2:7], 16)
    pos["y"] += numKey[int(line.split(" ")[2][7]) ][1]*int(line.split(" ")[2][2:7], 16)
    # pos["x"] += dirKey[line.split(" ")[0]][0] * int(line.split(" ")[1])
    # pos["y"] += dirKey[line.split(" ")[0]][1] * int(line.split(" ")[1])
res = 0

# blocks = [(1,6),(8,5),(4,4),(7,2),(3,1)]
blocks.append(blocks[0])
print(blocks)
outline = 0
for blockInd in range(len(blocks)-1,0,-1):
    outline+= abs(blocks[blockInd][0]-blocks[blockInd-1][0] + blocks[blockInd][1]-blocks[blockInd-1][1])
    # print(blocks[blockInd])
    res += blocks[blockInd][0] * blocks[blockInd-1][1]
    res -= blocks[blockInd][1] * blocks[blockInd-1][0]
    print(res)

print("outline",outline,outline/2,res/2+outline/2+1)
    

print(res/2)

import matplotlib.pyplot as plt

xs, ys = zip(*blocks) #create lists of x and y values

# plt.figure()
# plt.plot(xs,ys) 
# plt.show() # if you need...
# minX = 10000000000
# maxX = -10000000000
# minY = 10000000000
# maxY = -10000000000
# print("--- %s seconds ---" % (time.time() - start_time))
# for block in blocks:
#     if block[0] < minX:
#         minX = block[0]
#     if block[0] > maxX:
#         maxX = block[0]
#     if block[1] < minY:
#         minY = block[1]
#     if block[1] > maxY:
#         maxY = block[1]
# print(minX, maxX, minY, maxY)

# # grid = [["e" for y in range(minY,maxY+1)] for x in range(minX,maxX+1)]
# # print(grid)

# # for block in blocks:
# #     grid[block[0]["x"]-minX][block[0]["y"]-minY] = block[1]

# def fludFill(curX, curY, grid):
#     # print(curX, curY, grid[curX][curY])
#     if not (0 <= curX and curX < len(grid) and 0 <= curY and curY < len(grid[0])):
#         # print("Asdfasdfafdsafds")
#         return
    
#     if(grid[curX][curY] == 'e'):
#         # print("eeee")
#         grid[curX][curY] = "x"
        
#         fludFill(curX+1, curY, grid)
#         fludFill(curX-1, curY, grid)
#         fludFill(curX, curY+1, grid)
#         fludFill(curX, curY-1, grid)

# # fludFill(67, 1, grid)
# print("--- %s seconds ---" % (time.time() - start_time))

# res = 0
# for x in range(minX,maxX+1):
#     inside = False
#     for y in range(minY,maxY+1):
#         if((x,y) in blocks):
#             inside = not inside
#         else:
#             res+=1
#     print("in loop --- %s seconds ---" % (time.time() - start_time))
#     print(x,"/",maxX)
    
# print("--- %s seconds ---" % (time.time() - start_time))

# # print(grid)
# # res = 0
# # for row in grid:
# #     for item in row:
# #         if not item:
# #             res+=1
# print(res)
# print(len(blocks))
# print(res+len(blocks))

# # toSave = ""
# # for row in grid:
# #     for item in row:
# #         if(len(item) > 1):
# #             toSave +="#"
# #         else:
# #             toSave+=str(item)
# #     toSave += "\n"
# # f = open("map.txt", "w")
# # f.write(toSave)
# # f.close()