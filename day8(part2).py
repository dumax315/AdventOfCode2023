from aocd import get_data

res = 0
listOfLines = get_data(day=8, year=2023).split("\n")



nodes = {}
for i, line in enumerate(listOfLines):
    if(len(line.split()) < 3):
        continue
    nodes[line.split()[0]] = [line.split(" ", 2)[2][1:4],line.split(" ", 2)[2][6:9]]
    print(f"line #{i} \n{line}")

moves = listOfLines[0]

curNode = "AAA"
def lr(tempRes):
    global moves
    if(moves[tempRes%len(moves)] == "L"):
        return 0
    return 1

nodesTrac = []

for key, value in nodes.items():
    if(key[-1] == "A"):
        nodesTrac.append(key)


def allNodesZ():
    global nodesTrac
    for nod in nodesTrac:
        if(nod[-1] != "Z"):
            return False
        
    return True

print(f"node tracks { nodesTrac}")

# while not allNodesZ():
#     if(res % 1000000 == 0):
#         print(res)
#     # print(nodes[curNode].split(", "))
#     for nod in nodesTrac:
#         nod = nodes[nod][lr()]
#     # print(curNode)
#     res+=1
times = []
for nod in nodesTrac:
    tempRes = 0
    while nod[-1] != "Z":
        if(tempRes % 10000 == 0):
            print(nod[-1])
        nod = nodes[nod][lr(tempRes)]
        tempRes +=1
    times.append(tempRes)
    print(tempRes)


print(f"times {times}")
import numpy as np
print(np.lcm.reduce(times))


import math
print(math.lcm(*times))

import math
from functools import reduce

def lcm(arr):

    l=reduce(lambda x,y:(x*y)//math.gcd(x,y),arr)
    return l

print(lcm(times))
print(res)

# from aocd import submit
# submit(np.lcm.reduce(times), part="b", day=8, year=2023)