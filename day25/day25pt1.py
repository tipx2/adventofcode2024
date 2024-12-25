with open("day25/input25.txt") as f:
  lines = [x.strip().split("\n") for x in f.read().split("\n\n")]

def numerate(item):
  return [row.count("#")-1 for row in zip(*item[::-1])]
  
keys = []
locks = []

for line in lines:
  if all([x == "." for x in line[0]]):
    keys.append(numerate(line))
  else:
    locks.append(numerate(line))

total = 0
for l in locks:
  for k in keys:
    if all([k[i] + l[i] < 6 for i in range(5)]):
      total += 1
  
print(total)