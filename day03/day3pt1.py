import re
with open("day03/input3.txt") as f:
  lines = f.readlines()

def mul_dissect(s):
  left, right = s[4:-1].split(",")
  return int(left) * int(right)

total = 0
for line in lines:
  for match in re.findall(r"mul\(\d*,\d*\)", line):
    total += mul_dissect(match)

print(total)