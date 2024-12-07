with open("day01/input1.txt") as f:
    lines = f.readlines()

lefts = []
rights = []
for line in lines:
  l, r = line.split("   ")
  lefts.append(int(l))
  rights.append(int(r))

total = 0

for left in lefts:
  total += left * rights.count(left)

print(total)