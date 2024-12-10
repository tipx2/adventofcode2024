with open("day10/input10.txt") as f:
  lines = [[int(z) for z in x.strip()] for x in f.readlines()]

max_x = len(lines)
max_y = len(lines[0])

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def get_surrounding(pos):
  out = []
  for d in directions:
    prosp = (pos[0] + d[0], pos[1] + d[1])
    if 0 <= prosp[0] < max_x and 0 <= prosp[1] < max_y:
      
      prosp = (prosp[0], prosp[1], lines[prosp[0]][prosp[1]])
      out.append(prosp)
  return out

total = 0
for x in range(max_x):
  for y in range(max_y):
    if lines[x][y] != 0:
      continue
    
    seen = set()
    poses = [(x, y, 0)]
    nines = 0
    
    while len(poses) != 0:
      
      p = poses.pop(0)
      if p[2] == 9:
        nines += 1
      
      new_poses = [x for x in get_surrounding(p) if p[2] + 1 == x[2]]
      
      poses += new_poses
      seen.update(new_poses)

    total += nines
    

print(total)