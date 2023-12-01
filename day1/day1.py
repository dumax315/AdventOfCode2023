f = open("./day1.txt", "r")
res = 0
listOfLines = f.read().split("\n")

i = 0
words =  ["one", "two", "three", "four", "five", "six", "seven", "eight","nine"]

for line in listOfLines:
    # iline = int(line)
    print(f"  line {i} is \n{line}")
    temp = 0

    j = 0
    done = False
    for ch in line:
        j += 1
        try:
            temp += int(ch)*10
            break
        except:
            wwid = 1
            for word in words:
                if(word in line[:j]):
                    print(line[:j])
                    temp += wwid*10
                    done = True
                    break
                wwid+=1
        if(done):
            break


            pass
    j = len(line)
    done = False
    for ch in line[::-1]:
        j -= 1
        try:
            temp += int(ch)
            break
        except:
            wwid = 1
            for word in words:
                if(word in line[j:]):
                    print(line[j:])
                    
                    temp += wwid
                    print(wwid)
                    done = True
                    break


                wwid+=1
        if(done):
            break

    res += temp
    print(temp)

    i+=1

# for i in range(len(listOfLines)):
#     iline = int(listOfLines[i])
#     print(f"  line {i} is \n{listOfLines[i]}")

#     res += int(iline)

print(f"result = {res}")