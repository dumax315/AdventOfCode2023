from aocd import get_data

listOfLines = get_data(day=3, year=2023).split("\n")
res = 0

print("Asdf"[0:2])

import re


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
            
            notFound = True
            if(i != 0): 
                print(listOfLines[i-1][startOfNumber-1:j+1])
                for check in listOfLines[i-1][startOfNumber-1:j+1]:
                   
                    if((not check.isdigit() )and check != "."):
                        notFound = False
                        break
            
            if(notFound and i < len(listOfLines)-1):
                print(listOfLines[i+1][startOfNumber-1:j+1])
                for check in listOfLines[i+1][startOfNumber-1:j+1]:
                    
                    if((not check.isdigit() )and check != "."):
                        notFound = False
                        break

            if(notFound and startOfNumber > 0):
                if(line[startOfNumber-1] != "."):
                    notFound = False

            if(notFound and line[j] != "."):
                notFound = False
            
            print(f"not found? {notFound}")
            if(not notFound):
                res += num
            startOfNumber = -1
            print(f"res = {res}")
                
            



    # res += temp

    
    

print(f"result = {res}")


from aocd import submit
submit(res, part="a", day=3, year=2023)