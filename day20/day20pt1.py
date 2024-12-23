import heapq
with open("day20/input20.txt") as f:
  lines = [x.strip() for x in f.readlines()]

walls = set()
for i, line in enumerate(lines):
  for j, letter in enumerate(line):
    if letter == "#":
      walls.add((i, j))
    elif letter == "S":
      starti = i
      startj = j
    elif letter == "E":
      endi = i
      endj = j

def boundary_check(coord):
  return 0 <= coord[0] < len(lines) and 0 <= coord[1] < len(lines[0])

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dijk(walls):
  check = [(0, starti, startj)]
  seen = set()

  while check:
    
    weight, curri, currj = heapq.heappop(check)
    
    if (curri, currj) == (endi, endj):
      return weight
    
    for d in directions:
      prosp = (curri + d[0], currj + d[1])
      
      if prosp not in walls and boundary_check(prosp) and prosp not in seen:
        heapq.heappush(check, (weight + 1 , prosp[0], prosp[1]))
        seen.add(prosp)

original_weight = dijk(walls)

saved = []
for wall in walls:
  
  new_walls = walls.copy()
  new_walls.remove(wall)
  
  for d in directions:

    dird = (wall[0] + d[0], wall[1] + d[1])
    if dird in new_walls:
      continue
    
    new_weight = dijk(new_walls)
    
    if new_weight < original_weight:
      saved.append(original_weight - new_weight)
      break

print(len([x for x in saved if x >= 100]))

