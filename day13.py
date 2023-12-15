with open("day13.txt", "r") as f:
  blocks = f.read().split("n")

def numDiff(str1, str2):
  res = 0
  for i in range(len(str1)):
    if(str1[i] != str2[i]):
      res+=1
  return res

def isValid(i, lines):
  shorterLen = min(len(lines) - i - 1, i+1)
  totalDiff = 0
  for offSet in range(shorterLen):
    totalDiff += numDiff(lines[i - offSet], lines[i + 1 + offSet])
    # if(totalDiff >1):
    #   return False
 
  return totalDiff == 1



res = 0
for block in blocks:
  temp = 0
  print(block)
  lines = block.split("\n")
  for i in range(len(lines) - 1):
    print(f"{i} i: {lines[i]} == {lines[i+1]}")

    if numDiff(lines[i], lines[i + 1])<2 and isValid(i, lines):
      temp += ((i + 1) *100)
      continue

  colsT = [[j[i] for j in lines] for i in range(len(lines[0]))]
  cols = ["".join(colsT[i]) for i in range(len(colsT))]
  for i in range(len(cols) - 1):
    print(f"{i} i: {cols[i]} == {cols[i+1]}")

    if numDiff(cols[i], cols[i + 1])<2 and isValid(i, cols):
      temp += (i + 1)
      continue


  print(f"temp = {temp}")
  res += temp

print(res)
