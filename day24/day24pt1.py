with open("day24/input24.txt") as f:
  variables, instructions = f.read().split("\n\n")

variables = {k:int(v) for k, v in [x.strip().split(": ") for x in variables.split("\n")]}
instructions = [x.split(" ") for x in instructions.strip().split("\n")]

formatted_instructions = []
for item in instructions:
  formatted_instructions.append([item[0], item[1], item[2], item[4]])
instructions = formatted_instructions

def combine(instruction):
  a, op, b, _ = instruction
  
  if op == "XOR":
    return a ^ b
  elif op == "AND":
    return a & b
  elif op == "OR":
    return a | b

max_z = 46
values = []

while True:
  if len(values) == max_z:
    break
  
  for x in range(len(instructions)):
      for y in range(len(instructions[x])-1):
        if instructions[x][y] in variables:
          instructions[x][y] = variables[instructions[x][y]]
          
          if isinstance(instructions[x][0], int) and isinstance(instructions[x][2], int):
            variables[instructions[x][3]] = combine(instructions[x])
            
            if instructions[x][3].startswith("z"):
              values.append((int(instructions[x][3].strip("z")), variables[instructions[x][3]]))

number = "".join([str(x[1]) for x in reversed(sorted(values))])
print(number, int(number, 2))