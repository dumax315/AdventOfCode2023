from aocd import get_data

listOfLines = get_data(day=3, year=2023).split("\n")
res = 0

print("Asdf"[0:2])

import re

gears = [ [ 1 for y in range( len(listOfLines[0]) ) ] for x in range( len(listOfLines) ) ]
# print(gears)
gears2 = [ [ 0 for y in range( len(listOfLines[0]) ) ] for x in range( len(listOfLines) ) ]


for i, line in enumerate(listOfLines):
    print(f"line {i} is {line}")

    startOfNumber = -1
    for j, char in enumerate(line):
        # print(startOfNumber)
        if(char.isdigit() and startOfNumber==-1):
            startOfNumber= j
        
        if((not char.isdigit()) and startOfNumber !=-1):
            num = int(line[startOfNumber:j])
            print(num)
            
            if(i != 0): 
                print(listOfLines[i-1][startOfNumber-1:j+1])
                for jj, check in enumerate(listOfLines[i-1][startOfNumber-1:j+1]):
                   
                    if(check == "*"):
                        gears[i-1][startOfNumber-1+jj] *= num
                        gears2[i-1][startOfNumber-1+jj] +=1
            
            if(i < len(listOfLines)-1):
                print(listOfLines[i+1][startOfNumber-1:j+1])
                for jj, check in enumerate(listOfLines[i+1][startOfNumber-1:j+1]):
                    
                    if(check == "*"):
                        gears[i+1][startOfNumber-1+jj] *= num
                        gears2[i+1][startOfNumber-1+jj] +=1
                        
                        

            if(startOfNumber > 0):
                if(line[startOfNumber-1] == "*"):
                    gears[i][startOfNumber-1] *= num
                    gears2[i][startOfNumber-1] +=1

            if(line[j] == "*"):
                gears[i][j] *= num
                gears2[i][j] +=1
            

            startOfNumber = -1

            print(f"res = {res}")
                

    # res += temp

    
    
for i in range(len(gears)):
    for j in range(len(gears[0])):
        
        if(gears2[i][j] == 2):
            print(gears[i][j])
            res+= gears[i][j]
# print(gears)
# print(gears2)
print(f"result = {res}")


from aocd import submit
submit(res, part="b", day=3, year=2023)