from aocd import get_data

listOfLines = get_data(day=6, year=2023).split("\n")
res = 0


for i, line in enumerate(listOfLines):
    print(f"line {i} is {line}")


    # res += temp

print(f"result = {res}")


# from aocd import submit
# submit(res, part="a", day=6, year=2023)