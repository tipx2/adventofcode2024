import heapq
with open("day18/input18.txt") as f:
  lines = [tuple(int(z) for z in x.strip().split(",")) for x in f.readlines()]

end = (70, 70)

walls = []
for i in range(1024):
  walls.append(lines[i])

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def djek(walls):
  check = [(0,0,0)] # weight, x, y
  visited = set()

  while check:
    weight, currx, curry = heapq.heappop(check)
    
    if (currx, curry) == end:
      return weight
    
    if (currx, curry) in visited:
      continue
    visited.add((currx, curry))
    
    for d in directions:
      t_dir = (weight + 1, currx + d[0], curry + d[1])
      if (t_dir[1], t_dir[2]) not in walls and 0 <= t_dir[1] <= 70 and 0 <= t_dir[2] <= 70:
        heapq.heappush(check, t_dir)

  return None

for item in lines[1024:]:
  walls.append(item)
  
  if djek(walls) == None:
    print(item)
    break