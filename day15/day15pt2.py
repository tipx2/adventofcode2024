with open("day15/test.txt") as f:
  r_map, instructions = f.read().split("\n\n")

instructions = instructions.replace("\n", "")
r_map = r_map.replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@.")

def debug_draw(boxes, walls, robot):
  for x in range(50):
    for y in range(50):
      if (x, y) in boxes:
        print("O", end="")
      elif (x, y) in walls:
        print("#", end="")
      elif robot == [x, y]:
        print("@", end="")
      else:
        print(".", end="")
    print()


boxes = []
walls = []

for i, row in enumerate(r_map.split("\n")):
  for j, letter in enumerate(row):
    if letter == "#":
      walls.append((i, j))
    elif letter == "[" or letter == "]":
      boxes.append((i, j))
    elif letter == "@":
      robot = [i, j]

debug_draw(boxes, walls, robot)

directions = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}

for inst in instructions:
  dx, dy = directions[inst]
  check = [(robot[0] + dx, robot[1] + dy)]
  
  move_these = []
  not_moving = False
  
  while check:
    curr = check.pop()
    move_these.append(curr)
    
    if (curr[0] + dx, curr[1] + dy) in walls:
      not_moving = True
      break
    elif (curr[0] + dx, curr[1] + dy) in boxes:
      check.append((curr[0] + dx, curr[1] + dy))
    
    if (curr[0], curr[1]) in boxes:
      check.append((curr[0], curr[1]))
    elif (curr[0], curr[1]) in boxes:
      pass
    
  
  if not_moving:
    continue
  else:
    boxes += [(x[0] + dx, x[1] + dy) for x in move_these]
    
debug_draw(boxes, walls, robot)