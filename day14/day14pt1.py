import re
with open("day14/input14.txt") as f:
  lines = [[int(z) for z in re.findall("-?\d+", x.strip())] for x in f.readlines()]

grid = []
for line in lines:
  final_x = (line[0] + 100 * line[2]) % 101
  final_y = (line[1] + 100 * line[3]) % 103
  
  grid.append((final_x, final_y))


scores = [0, 0, 0, 0]
for x, y in grid:
  if x == 50 or y == 51:
    continue
  
  if x < 50 and y < 51:
      scores[0] += 1
  elif x < 50 and y > 51:
      scores[1] += 1
  elif x > 50 and y < 51:
      scores[2] += 1
  elif x > 50 and y > 51:
      scores[3] += 1

print(scores)
print(scores[0] * scores[1] * scores[2] * scores[3])

