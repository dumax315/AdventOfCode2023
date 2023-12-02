from aocd import get_data

listOfLines = get_data(day=2, year=2023).split("\n")

res = 0

import re

# 12 red cubes, 
# 13 green cubes, and 
# 14 blue cubes
# colors = {"red":12,"green":13,"blue":14}

for i, line in enumerate(listOfLines):
    temp = 1
    print(f"line is {line}")
    suc = True
    colors = {"red":0,"green":0,"blue":0}
    for item in re.split('[,;]', line.split(": ")[1]):
        if(colors[item.strip().split()[1]] < int(item.strip().split()[0])):
            colors[item.strip().split()[1]] = int(item.strip().split()[0])
    
    print(int(line.split(" ")[1].split(":")[0]))
    temp *= colors["red"]
    temp *= colors["green"]
    temp *= colors["blue"]
    res += temp
    # if suc:
    #     res += int(line.split(" ")[1].split(":")[0])
    
    

print(f"result = {res}")


from aocd import submit
submit(res, part="b", day=2, year=2023)