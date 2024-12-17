import heapq
with open("day16/input16.txt") as f:
  lines = [x.strip() for x in f.readlines()]

grid = set()

for i, line in enumerate(lines):
  for j, letter in enumerate(line):
    if letter == "#":
      grid.add((i, j))
    elif letter == "S":
      deerx = i
      deery = j
    elif letter == "E":
      endx = i
      endy = j

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def pathfind(startx, starty, startdir):
  costs = [(0, startx, starty, startdir)] # x, y, direction, cost
  visited = {(startx, starty, startdir): 0}

  while costs:
    currcost, currx, curry, currdir = heapq.heappop(costs)
    
    if (currx, curry, (currdir + 1)% len(directions)) not in visited:
      heapq.heappush(costs, (currcost + 1000, currx, curry, (currdir + 1) % len(directions)))
      visited[(currx, curry, (currdir + 1)% len(directions))] = currcost
    
    if (currx, curry, (currdir - 1)% len(directions)) not in visited:
      heapq.heappush(costs, (currcost + 1000, currx, curry, (currdir - 1) % len(directions)))
      visited[(currx, curry, (currdir - 1)% len(directions))] = currcost
    
    prosp = (currx + directions[currdir][0], curry + directions[currdir][1])
    if prosp not in grid and (prosp[0], prosp[1], currdir) not in visited:
      heapq.heappush(costs, (currcost + 1, prosp[0], prosp[1], currdir))
      visited[(prosp[0], prosp[1], currdir)] = currcost
      
  return visited

visited_start = pathfind(deerx, deery, 0)
visited_end = pathfind(endx, endy, 0)

for x in range(1, 4):
  for key, value in pathfind(endx, endy, x).items():
    if value < visited_end[key]:
      visited_end[key] = value


visited_end = {(k[0], k[1], (k[2] + 2) % len(directions)): v for k, v in visited_end.items()}

shortest = 99488 # cheeky

seen = set()

for k in visited_start.keys():
  if (k[0], k[1]) in seen:
    continue
  if visited_start[k] + visited_end[k] == shortest:
    seen.add((k[0], k[1]))
    
print(len(seen))