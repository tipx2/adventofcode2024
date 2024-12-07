import re
with open("day3/input3.txt") as f:
  lines = f.readlines()

def mul_dissect(s):
  left, right = s[4:-1].split(",")
  return int(left) * int(right)

matches = []
for line in lines:
  for match in re.findall(r"mul\(\d*,\d*\)|do\(\)|don't\(\)", line):
    matches.append(match)

total = 0
enabled = True
for match in matches:
  if match == "do()":
    enabled = True
  elif match == "don't()":
    enabled = False
  else:
    if not enabled:
      continue
    total += mul_dissect(match)
    

print(total)