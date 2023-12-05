from aocd import get_data

def rangeOverLap(seedRange, mapRange, mapsTo):
    dif = -mapRange[0] + mapsTo
    if(seedRange[1] < mapRange[0] or seedRange[0] > mapRange[1]):
        return []
    elif(seedRange[0] < mapRange[0] and mapRange[1] < seedRange[1]):
        return [mapRange[0]+dif,mapRange[1]+dif]
    elif(mapRange[0] < seedRange[0] and seedRange[1] < mapRange[1]):
        return [seedRange[0]+dif,seedRange[1]+dif]
    else:
        new = [i for i in seedRange]
        new.extend([i for i in mapRange])
        # print(new)
        new.sort()
        return [new[1]+dif, new[2]+dif]
    
def exc(seedRange, mapRange):
    if(seedRange[1] < mapRange[0] or seedRange[0] > mapRange[1]):
        return []
    elif(seedRange[0] < mapRange[0] and mapRange[1] < seedRange[1]):
        return [[seedRange[0], mapRange[0]-1],[mapRange[1]+1,seedRange[1]]]
    elif(mapRange[0] < seedRange[0] and seedRange[1] < mapRange[1]):
        return []
    elif(seedRange[0] < mapRange[0]):
        return [[seedRange[0],mapRange[0]-1]]
    else:
        return [[mapRange[1]+1,seedRange[1]]]

# f = open("day5.txt", "r").read()
f = get_data(day=5, year=2023)

listOfLines = f.split("\n")

res = 0

seedss = listOfLines[0].split(": ")[1].split()
seeds = []
for sIndex in range(0,len(seedss),2):
    
    seeds.append([int(seedss[sIndex]),int(seedss[sIndex])+int(seedss[sIndex+1])-1])

seeds.sort()
print(seeds)

nextGroup = []

# while len(bonus) > 0
print(f.split("map:"))
for section in f.split("map:"):
    listOfLinesSmall =section.split("\n")
    print(listOfLinesSmall)
    foundNothing = False
    while not foundNothing:
        foundNothing = True
        for i, line in enumerate(listOfLinesSmall):
            print(f"line {i} is {line}")

            if(line == ""):
                print("blank")
                continue
                
            elif(not line.split()[0].isdigit()):
                continue
            else:
                j = len(seeds)-1
                while(j>=0):
                    newRange = rangeOverLap(seeds[j], [int(line.split()[1]),int(line.split()[1]) + int(line.split()[2])-1], int(line.split()[0]))
                    ex = exc(seeds[j], [int(line.split()[1]),int(line.split()[1]) + int(line.split()[2])-1])
                    if(len(newRange) > 0):
                        foundNothing = False

                        # print(f"{newRange} + leftover : {ex}")
                        nextGroup.append(newRange)
                        del seeds[j]
                        seeds.extend(ex)
                            # j+=1
                    
                    j-=1

    print(f" remaining seeds  = {len(seeds)}")
    print(f" nextgroup  = {len(nextGroup)}")
    print(len(nextGroup) + len(seeds))
    nextGroup.extend(seeds)
    seeds = nextGroup
    nextGroup = []
    print(len(seeds))

                


# res += temp
print(f" remaining seeds  = {len(seeds)}")
print(f" nextgroup  = {len(nextGroup)}")
print(len(nextGroup) + len(seeds))
nextGroup.extend(seeds)
seeds = nextGroup
nextGroup = []
print(len(seeds))
# seeds.sort()
# print(f"result = {seeds}")
print(seeds[0:10])
res = [i[0] for i in seeds]
res.sort()
print(res)
lowest = 100000000000000000
for seed in seeds:
    if(lowest > seed[0]):
        lowest = seed[0]
print(lowest)

# print(res)
# from aocd import submit
# submit(lowest, part="b", day=5, year=2023)