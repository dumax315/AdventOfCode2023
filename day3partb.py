from aocd import get_data

listOfLines = get_data(day=3, year=2023).split("\n")
res = 0

# this list records the ratio for each gear
gears = [ [ 1 for y in range( len(listOfLines[0]) ) ] for x in range( len(listOfLines) ) ]
# this 2d list records the number of numbers for each *
gears2 = [ [ 0 for y in range( len(listOfLines[0]) ) ] for x in range( len(listOfLines) ) ]
for i, line in enumerate(listOfLines):
    print(f"line {i} is {line}")

    startOfNumber = -1
    for j, char in enumerate(line):
        # check to see if this char is the start of a new number
        if(char.isdigit() and startOfNumber==-1): startOfNumber= j
        
        # check to see if this char is the end of a number
        if((not char.isdigit()) and startOfNumber !=-1):
            # get the number
            num = int(line[startOfNumber:j])
            # look for gears on the line above
            if(i != 0): 
                for jj, check in enumerate(listOfLines[i-1][startOfNumber-1:j+1]):
                    if(check == "*"):
                        gears[i-1][startOfNumber-1+jj] *= num
                        gears2[i-1][startOfNumber-1+jj] +=1
            
            # look for gears on the line below
            if(i < len(listOfLines)-1):
                for jj, check in enumerate(listOfLines[i+1][startOfNumber-1:j+1]):
                    if(check == "*"):
                        gears[i+1][startOfNumber-1+jj] *= num
                        gears2[i+1][startOfNumber-1+jj] +=1
                        
            # look for a gear to the left
            if(startOfNumber > 0):
                if(line[startOfNumber-1] == "*"):
                    gears[i][startOfNumber-1] *= num
                    gears2[i][startOfNumber-1] +=1

            # look for a gear to the right
            if(line[j] == "*"):
                gears[i][j] *= num
                gears2[i][j] +=1
            
            startOfNumber = -1
for i in range(len(gears)):
    for j in range(len(gears[0])):
        
        if(gears2[i][j] == 2):
            print(gears[i][j])
            res+= gears[i][j]

print(f"result = {res}")


from aocd import submit
submit(res, part="b", day=3, year=2023)