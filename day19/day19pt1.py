import functools
with open("day19/input19.txt") as f:
  towels, configs = f.read().split("\n\n")
  configs = [x.strip() for x in configs.strip().split("\n")]
  towels = towels.strip().split(", ")
  
@functools.cache
def attempt(goal):
  if goal == "":
    return True
  
  for t in towels:
    if goal.startswith(t):
      if attempt(goal[len(t):]):
        return True
  
  return False

total = 0
for c in configs:
  if attempt(c):
    total += 1

print(total)