from aocd import get_data

# returns the new range with the mapping applied first and the excess ranges second
def rangeOverLapAndExess(seedRange, mapRange, mapsTo):
    dif = -mapRange[0] + mapsTo
    if(seedRange[1] < mapRange[0] or seedRange[0] > mapRange[1]):
        return [], []
    elif(seedRange[0] < mapRange[0] and mapRange[1] < seedRange[1]):
        return [mapRange[0]+dif,mapRange[1]+dif], [[seedRange[0], mapRange[0]-1],[mapRange[1]+1,seedRange[1]]]
    elif(mapRange[0] < seedRange[0] and seedRange[1] < mapRange[1]):
        return [seedRange[0]+dif,seedRange[1]+dif], []
    else:
        new = [i for i in seedRange]
        new.extend([i for i in mapRange])
        new.sort()
        
        newRange = [new[1]+dif, new[2]+dif]

        if(seedRange[0] < mapRange[0]):
            return newRange, [[seedRange[0],mapRange[0]-1]]
        elif(seedRange[1] > mapRange[1]):
            return newRange, [[mapRange[1]+1,seedRange[1]]]
        return newRange, []

# f = open("day5.txt", "r").read()
f = get_data(day=5, year=2023)

res = 0

seedsWithoutRanges = f.split("\n")[0].split(": ")[1].split()
seeds = []
for sIndex in range(0,len(seedsWithoutRanges),2):
    seeds.append([int(seedsWithoutRanges[sIndex]), int(seedsWithoutRanges[sIndex])+int(seedsWithoutRanges[sIndex+1])-1])


nextGroup = []
for section in f.split("map:"):
    listOfLinesSmall =section.split("\n")
    for i, line in enumerate(listOfLinesSmall):

        if(line == "" or (not line.split()[0].isdigit())):
            continue
        for j in range(len(seeds)-1,-1,-1):
            newRange, ex = rangeOverLapAndExess(
                seeds[j], 
                [int(line.split()[1]), int(line.split()[1]) + int(line.split()[2])-1], int(line.split()[0])
            )
            if(len(newRange) > 0):
                foundNothing = False

                nextGroup.append(newRange)
                del seeds[j]
                seeds.extend(ex)
    nextGroup.extend(seeds)
    seeds = nextGroup
    nextGroup = []


nextGroup.extend(seeds)
seeds = nextGroup

res = [i[0] for i in seeds]

lowest = 100000000000000000
for seed in seeds:
    if(lowest > seed[0]):
        lowest = seed[0]
print(lowest)

from aocd import submit
submit(lowest, part="b", day=5, year=2023)