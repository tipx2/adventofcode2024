with open("day6/input6.txt") as f:
  lines = [x.strip() for x in f.readlines()]

def detect_loop(grid):
  curr_x = start_x
  curr_y = start_y
  directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
  curr_dir = 0
  
  seen_poses = set()
  while 0 <= curr_x < len(lines) and 0 <= curr_y < len(lines[0]):
    
    if (curr_x, curr_y, curr_dir) in seen_poses:
      return True
    else:
      seen_poses.add((curr_x, curr_y, curr_dir))
    
    direct = directions[curr_dir]
    if (curr_x + direct[0], curr_y + direct[1]) in grid: # if we see a box
      curr_dir = (curr_dir + 1) % len(directions) # rotate 90
    else:
      curr_x += direct[0]
      curr_y += direct[1]
      
  return False


grid = []
for x in range(len(lines)):
  for y in range(len(lines[x])):
    if lines[x][y] == "#":
      grid.append((x, y))
    elif lines[x][y] == "^":
      start_x = x
      start_y = y

total = 0
for x in range(len(lines)):
  print(x)
  for y in range(len(lines[0])):
    if detect_loop(grid + [(x, y)]):
      total += 1

print(total)
