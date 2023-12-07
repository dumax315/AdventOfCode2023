from aocd import get_data

res = 0
listOfLines = get_data(day=7, year=2023).split("\n")

cards = "AKQT98765432J"

def getfrq(hand):
    toRe = {}
    joks = 0
    for l in hand:
        if l == "J":
            joks+=1
        elif l in toRe:
            toRe[l]+=1
        else:
            toRe[l]=1
    largestVal = -1
    largestKey = ""
    for key, value in toRe.items():
        if(value > largestVal):
            largestVal = value
            largestKey = key
    if(largestKey == ""):
        return {"A":5}
    
    toRe[largestKey] += joks
    return toRe

def getRank(hand1):
    hand1cards = getfrq(hand1)
    hand1Rank = 0
    if(5 in hand1cards.values()):
        hand1Rank = 10
    elif(4 in hand1cards.values()):
        hand1Rank = 9
    elif(3 in hand1cards.values() and 2 in hand1cards.values()):
        hand1Rank = 8
    elif(3 in hand1cards.values()):
        hand1Rank = 7
    elif(list(hand1cards.values()).count(2) ==2):
        hand1Rank = 6
    elif(list(hand1cards.values()).count(2) ==1):
        hand1Rank = 5
    return hand1Rank

def compareHand(hand1, hand2):
    hand1Rank = getRank(hand1.split()[0])
    hand2Rank = getRank(hand2.split()[0])

    if(hand1Rank != hand2Rank):
        return hand1Rank - hand2Rank
    
    else:
        for i in range(len(hand1)):
            if cards.index(hand1[i]) == cards.index(hand2[i]):
                continue
            else:
                return cards.index(hand2[i]) -cards.index(hand1[i]) 

from functools import cmp_to_key

listOfLines.sort(key=cmp_to_key(compareHand))
for i, line in enumerate(listOfLines):
    print(line)
    res+=int(line.split()[1])*(i+1)

print(res)
# from aocd import submit
# submit(res, part="a", day=7, year=2023)