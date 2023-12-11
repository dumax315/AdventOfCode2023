from aocd import get_data

res = 0
listOfLines = get_data(day=11, year=2023).split("\n")

for i, line in enumerate(listOfLines):
    
    print(f"line #{i} \n{line}")

print(res)

# from aocd import submit
# submit(res, part="a", day=11, year=2023)