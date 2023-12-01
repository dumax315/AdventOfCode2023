from aocd import get_data

res = 0
listOfLines = get_data(day=1, year=2023).split("\n")

words =  ["one", "two", "three", "four", "five", "six", "seven", "eight","nine"]

for line in listOfLines:
    print(f"line is {line}")
    numberForThisLine = 0

    indexOfLine = 0
    done = False
    for ch in line:
        indexOfLine += 1
        try:
            numberForThisLine += int(ch)*10
            break
        except:
            wwid = 1
            for word in words:
                if(word in line[:indexOfLine]):
                    print(line[:indexOfLine])
                    numberForThisLine += wwid*10
                    done = True
                    break
                wwid+=1
        if(done):
            break


            pass
    indexOfLine = len(line)
    done = False
    for ch in line[::-1]:
        indexOfLine -= 1
        try:
            numberForThisLine += int(ch)
            break
        except:
            wwid = 1
            for word in words:
                if(word in line[indexOfLine:]):
                    print(line[indexOfLine:])
                    
                    numberForThisLine += wwid
                    print(wwid)
                    done = True
                    break


                wwid+=1
        if(done):
            break

    res += numberForThisLine
    print(numberForThisLine)

print(f"result = {res}")