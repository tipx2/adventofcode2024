import functools
with open("day19/input19.txt") as f:
  towels, configs = f.read().split("\n\n")
  configs = [x.strip() for x in configs.strip().split("\n")]
  towels = towels.strip().split(", ")
  
@functools.cache
def attempt(goal):
  if goal == "":
    return 1
  
  total_ways = 0
  for t in towels:
    if goal.startswith(t):
      total_ways += attempt(goal[len(t):])
  
  return total_ways

total = 0
for c in configs:
  total += attempt(c)

print(total)