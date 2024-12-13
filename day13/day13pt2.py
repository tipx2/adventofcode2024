import re
with open("day13/input13.txt") as f:
  lines = [x for x in f.read().strip().split("\n\n")]

for x in range(len(lines)):
  lines[x] = [int(z) for z in re.findall(r"\d+", lines[x])]

total = 0
for line in lines:
  a_x = line[0]
  a_y = line[1]
  
  b_x = line[2]
  b_y = line[3]
  
  target_x = line[4] + 10000000000000
  target_y = line[5] + 10000000000000
  
  # little bit of maths
  b_presses = ((target_y * a_x / a_y) - target_x) / ((b_y * a_x / a_y) - b_x)
  a_presses = (target_x - b_x * b_presses) / a_x
  
  
  if abs(round(a_presses) - a_presses) < 0.0001 and abs(round(b_presses) - b_presses) < 0.0001: # ensure solution is whole # of presses  
    total += round(a_presses) * 3 + round(b_presses)

print(total)
