with open("day16/input16.txt") as f:
  lines = [x.strip() for x in f.readlines()]

grid = []

for i, line in enumerate(lines):
  for j, letter in enumerate(line):
    if letter == "#":
      grid.append((i, j))
    elif letter == "S":
      deerx = i
      deery = j
    elif letter == "E":
      endx = i
      endy = j

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
curr_dir = 0 # east

costs = [(deerx, deery, curr_dir, 0)] # x, y, direction, cost

visited = set()

while costs:
  currx, curry, currdir, currcost = costs.pop(0)
  
  if currx == endx and curry == endy:
    print(currcost)
    break
  
  if (currx, curry, currdir) in visited:
    continue
  visited.add((currx, curry, currdir))
  
  costs.append((currx, curry, (currdir + 1) % len(directions), currcost + 1000))
  costs.append((currx, curry, (currdir - 1) % len(directions), currcost + 1000))
  
  prosp = (currx + directions[currdir][0], curry + directions[currdir][1])
  if prosp not in grid:
    costs.append((prosp[0], prosp[1], currdir, currcost + 1))
    
  costs = sorted(costs, key=lambda x : x[3])
