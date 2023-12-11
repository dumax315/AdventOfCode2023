from aocd import get_data

res = 0
lineArr = [[y for y in x] for x in get_data(day=12, year=2023).split("\n")]

for i, line in enumerate(lineArr):
    print(f"line #{i} \n{line}")

print(res)
# from aocd import submit
# submit(res, part="a", day=12, year=2023)