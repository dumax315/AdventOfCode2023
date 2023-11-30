f = open("./day1.txt", "r")
res = 0
listOfLines = f.read().split("\n")

i = 0
for line in listOfLines:
    print(f"  line {i} is \n{line}")

    i+=1

print(f"result = \n{res}")