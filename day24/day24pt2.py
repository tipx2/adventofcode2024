with open("day24/input24.txt") as f:
  variables, instructions = f.read().split("\n\n")

variables = {k:int(v) for k, v in [x.strip().split(": ") for x in variables.split("\n")]}
instructions = [x.split(" ") for x in instructions.strip().split("\n")]

print(variables, instructions)