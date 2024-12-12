with open("day12/input12.txt") as f:
  lines = [x.strip() for x in f.readlines()]    

regions = []

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
max_i = len(lines)
max_j = len(lines[0])

def get_surrounding(pos):
  out = []
  for d in directions:
    prosp = (pos[0] + d[0], pos[1] + d[1])
    if 0 <= prosp[0] < max_i and 0 <= prosp[1] < max_j:
      prosp = (prosp[0], prosp[1])
      out.append(prosp)
  return out
  
def already_checked(coord, regions):
  checked = False
  for x in regions:
    if coord in x:
      checked = True
      break
  return checked

for i, line in enumerate(lines):
  for j, letter in enumerate(line):
    if not already_checked((i, j), regions):
      # new region, bfs
      region = []
      seen = set()
      queue = [(i, j)]
      while len(queue) != 0:
        curr = queue.pop()
        seen.add(curr)
        
        new_poses = [x for x in get_surrounding(curr) if x not in seen and lines[x[0]][x[1]] == letter]
        
        queue += new_poses
        seen.update(new_poses)
        
      regions.append(seen)

price = 0
for region in regions:
  
  region = sorted(list(region))
  
  area = len(region)
  
  checked = set()
  perimeter = 0
  for coord in region:
    for p in directions:
      check = (coord[0] + p[0], coord[1] + p[1])
      if check in region:
        continue
      
      adj = False
      for d in directions:
        if (check[0] + d[0], check[1] + d[1], p) in checked:
          adj = True
          break

      if not adj:
        perimeter += 1
      
      checked.add((check[0], check[1], p))
  
  price += area * perimeter

print(price)
