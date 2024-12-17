import re
with open("day17/input17.txt") as f:
  registers, program = f.read().split("\n\n")

program = [int(x) for x in re.findall(r"\d+", program)]

# (A%8 ^ A/2**(A%8^7)) % 8 = item

options = [[0]]

for i, item in enumerate(reversed(program)):
  options.append([])
  
  for option in options[i]:
    for x in range(8):
        new_num = (option * 8) + x
        if (x ^ (new_num // 2 ** (x ^ 7))) % 8 == item:
          options[i + 1].append(new_num)
    
print(min(options[-1]))