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
def lr():
    global moves
    global res
    if(moves[res%len(moves)] == "L"):
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
# Import time module
import time
 
# record start time
start = time.time()


while not allNodesZ():
    if(res % 10000000 == 0):
        print("The time of execution of above program is :", (time.time()-start) * 10**3, "ms")
        print(res)
    # print(nodes[curNode].split(", "))
    for nod in nodesTrac:
        nod = nodes[nod][lr()]
    # print(curNode)
    res+=1

# record end time
end = time.time()
 
# print the difference between start 
# and end time in milli. secs
print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")

print(res)
# from aocd import submit
# submit(res, part="a", day=8, year=2023)