import time
start_time = time.time()

from functools import lru_cache 
import sys
sys.setrecursionlimit(150000)


with open("day17.txt", "r") as f:
  data = [[int(y) for y in x] for x in f.read().split("\n")]


print(data)

dp = {}

def search(x, y, inARow, numToGetHere):
  if(x < 0 or y < 0 or x >= len(data[0]) or y >= len(data)):
    return -1
  newNum = numToGetHere
  newNum.append(data[y][x])

  if((x, y, inARow["x"], inARow["y"]) in dp):
    if(sum(numToGetHere) < sum(dp[(x, y, inARow["x"], inARow["y"])])):
      toSearch = dp[(x, y, inARow["x"], inARow["y"])]
      toSearch.append(data[y][x])
      for key, val in dp.items():
        if(val == toSearch):
          dp[key] = newNum
      dp[(x, y, inARow["x"], inARow["y"])] = numToGetHere
    return -1
  
  dp[(x, y, inARow["x"], inARow["y"])] = numToGetHere
  
  searched = []
  dir = ""
  if(inARow["x"] > 0):
    dir = "e"
    if(inARow["x"] < 3):
      inARow["x"]+=1
      searched.append(search(x+1, y, inARow, newNum))

  elif(inARow["x"] < 0):
    dir = "w"
    if(inARow["x"] > -3):
      inARow["x"]-=1
      searched.append(search(x-1, y, inARow, newNum))


  elif(inARow["y"] > 0):
    dir = "n"
    if(inARow["y"] < 3):
      inARow["y"]+=1
      searched.append(search(x, y+1, inARow, newNum))


  elif(inARow["y"] < 0):
    dir = "s"
    if(inARow["y"] > -3):
      inARow["y"]-=1
      searched.append(search(x, y-1, inARow, newNum))
    
  if(dir != "w"):
    inARow = {"x":-1, "y":0}
    searched.append(search(x-1, y, inARow, newNum))
  if(dir != "e"):
    inARow = {"x":1, "y":0}
    searched.append(search(x+1, y, inARow, newNum))
  if(dir != "n"):
    inARow = {"x":0, "y":1}
    searched.append(search(x, y+1, inARow, newNum))
  if(dir != "s"):
    inARow = {"x":0, "y":-1}
    searched.append(search(x, y-1, inARow, newNum))

  smallest = 1000000000000000000
  sm = []
  for item in searched:
    if(item != -1 and smallest > sum(item)):
      smallest = sum(item)
      sm = item
  return sm 
 



res = search(0, 0, {"x":0, "y":0}, [])

print(res)
shortest = 1000000000000
shortestKey = ""
for key, val in dp.items():
  if(key[0] == len(data[0])-1 and key[1] == len(data)-1):
    # print(val)
    if(sum(val) < shortest):
      shortest = sum(val)
      shortestKey = key

print(shortestKey, shortest)
# print(dp[shortestKey])