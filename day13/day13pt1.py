import re
with open("day13/input13.txt") as f:
  lines = [[int(z) for z in re.findall(r"\d+", x)] for x in f.read().strip().split("\n\n")]

total = 0
for line in lines:
  a_x = line[0]
  a_y = line[1]
  
  b_x = line[2]
  b_y = line[3]
  
  target_x = line[4]
  target_y = line[5]  
  
  for a_presses in range(100):
    for b_presses in range(100):
      if a_x * a_presses + b_x * b_presses == target_x and a_y * a_presses + b_y * b_presses == target_y:
        total += a_presses * 3 + b_presses

print(total)