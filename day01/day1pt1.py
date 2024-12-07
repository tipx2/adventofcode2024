with open("day01/input1.txt") as f:
    lines = f.readlines()

lefts = []
rights = []
for line in lines:
  l, r = line.split("   ")
  lefts.append(int(l))
  rights.append(int(r))

lefts = sorted(lefts)
rights = sorted(rights)

total = 0
for i in range(len(lefts)):
  total += abs(lefts[i] - rights[i])

print(total)