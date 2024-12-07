with open("day06/input6.txt") as f:
  lines = [x.strip() for x in f.readlines()]


grid = []
curr_x = 0
curr_y = 0
for x in range(len(lines)):
  for y in range(len(lines[x])):
    if lines[x][y] == "#":
      grid.append((x, y))
    elif lines[x][y] == "^":
      curr_x = x
      curr_y = y

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
curr_dir = 0

seen_poses = set()
while 0 <= curr_x < len(lines) and 0 <= curr_y < len(lines[0]):
  seen_poses.add((curr_x, curr_y))
  
  direct = directions[curr_dir]
  if (curr_x + direct[0], curr_y + direct[1]) in grid: # if we see a box
    curr_dir = (curr_dir + 1) % len(directions) # rotate 90
  else:
    curr_x += direct[0]
    curr_y += direct[1]
  
print(len(seen_poses))
# took ~10 mins :)