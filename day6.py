# from aocd import get_data
# # listOfLines = open("day6.txt", "r").read().split("\n")

# listOfLines = get_data(day=6, year=2023).split("\n")
# res = 1

# def getDistance(totalTime, minDis):
#     totalTime = int(totalTime)
#     minDis = int(minDis)
#     start = -1
#     for i in range(1,totalTime):
#         tempTime = totalTime-i
        
#         if start == -1 and tempTime * i > minDis:
#             start = i
#         elif start != -1 and tempTime * i <= minDis:
#             return [start, i-1]

# # races = []
# # for i in range(len(listOfLines[0].split()) -1):
# #     races.append([listOfLines[0].split()[i+1], listOfLines[1].split()[i+1]])

# # for race in races:
# #     ways = getDistance(race[0], race[1])
# #     print(race)
# #     print(ways)
# #     print(ways[1]-ways[0])
# #     res*=(ways[1]-ways[0])+1
# # print(f"result = {res}")


# # from aocd import submit
# # submit(res, part="a", day=6, year=2023)

race = [55999793,401148522741405]
i = 0
for i in range(1,race[0]):
    tempTime = race[0]-i
    
    if tempTime * i > race[1]:
        print(i)
        break

res = 55999793-i*2+1
from aocd import submit
submit(res, part="b", day=6, year=2023)