from aocd import get_data
data = get_data(day=15, year=2023).split(",")
# with open("day15.txt", "r") as f:
#   data = f.read().split(",")

res = 0


def rainHash(inp):
    print(inp)
    resHash = 0
    for ch in inp:
        resHash += ord(ch)
        resHash*=17
        resHash%=256
    return resHash

lenses = [{} for x in range(256)]


for item in data:
    print(item)
    curHash = rainHash(item.split("=")[0].split("-")[0])
    if "=" in item:
        lenses[curHash][item.split("=")[0]] = item.split("=")[1]
    else:
        try:
            del lenses[curHash][item.split("-")[0]]
        except:
            print(curHash)
            print("no item")

i = 0
for d in lenses:
    for key, value in d.items():

        temp = i + 1
        temp *= list(d.keys()).index(key)+1
        temp *= int(value)
        res += temp
    i+=1
print(lenses)
print(res)


# One plus the box number of the lens in question.
# The slot number of the lens within the box: 1 for the first lens, 2 for the second lens, and so on.
# The focal length of the lens.



