import re
import statistics
import math
with open("day14/input14.txt") as f:
  lines = [[int(z) for z in re.findall("-?\d+", x.strip())] for x in f.readlines()]

def debug_draw(grid):
  for x in range(101):
    for y in range(103):
      if (y, x) in grid:
        print("#", end="")
      else:
        print(".", end="")
    print()

def get_grid(n):
  grid = []
  for line in lines:
    final_x = (line[0] + n * line[2]) % 101
    final_y = (line[1] + n * line[3]) % 103
    
    grid.append((final_x, final_y))
    
  return grid


minspread = 99999999999999
min_i = 0
for i in range(101 * 103):
  new_grid = get_grid(i)
  
  spread = statistics.stdev([x[0] for x in new_grid]) + statistics.stdev([x[1] for x in new_grid])
  if spread < minspread:
    minspread = spread
    min_i = i

debug_draw(get_grid(min_i))
print(min_i)