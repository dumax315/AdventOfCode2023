from aocd import get_data

listOfLines = get_data(day=4, year=2023).split("\n")
res = 0

cardToCheck = [ 1 for y in range( len(listOfLines) ) ]
while True:
    for cardIndex, times in enumerate(cardToCheck):
        if(times == 0):
            continue
        cardToCheck[cardIndex] = 0
        line = listOfLines[cardIndex]

        temp = 0

        found = False
        win = {-1}
        # print(line.split(":")[1].split("|")[0].split())
        for card in line.split(":")[1].split("|")[0].split():
            win.add(int(card))

        for card in line.split(":")[1].split("|")[1].split():
            if(int(card) in win):
                temp +=1
                found = True
        print(f"temp = { temp}")
        for i in range(cardIndex+1,cardIndex+1+temp):
            print(i)
            cardToCheck[i]+=times
            res += times

            # print(temp)
            
            
    done = True
    print(cardToCheck)
    for cardIndex, times in enumerate(cardToCheck):
        if(times > 0):
            done =False
    if(done):
        break


print(f"result = { len(listOfLines) + res}")


from aocd import submit
submit(len(listOfLines) + res, part="b", day=4, year=2023)