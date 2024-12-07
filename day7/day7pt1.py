from itertools import product
with open("day7/input7.txt") as f:
  lines = f.readlines()

over_total = 0
for line in lines:
  result, eqn = line.split(": ")
  result = int(result)
  eqn = [int(x) for x in eqn.split(" ")]
  
  operators = list(product("+*", repeat=len(eqn) - 1))
  
  for op in operators:
    total = eqn[0]
    
    for x in range(len(op)):
      if op[x] == "+":
        total += eqn[x + 1]
      elif op[x] == "*":
        total *= eqn[x + 1]
    
    if total == result:
      over_total += result
      break

print(over_total)
