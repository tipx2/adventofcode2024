with open("day15/input15.txt") as f:
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

box_lookup = {}

for i, row in enumerate(r_map.split("\n")):
  for j, letter in enumerate(row):
    if letter == "#":
      walls.append((i, j))
    elif letter == "[" or letter == "]":
      boxes.append((i, j))
      box_lookup[(i, j)] = letter
    elif letter == "@":
      robot = [i, j]

directions = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}

for inst in instructions:
  dx, dy = directions[inst]
  
  check = [(robot[0] + dx, robot[1] + dy)]
  attended_boxes = []
  
  moving = True
  while check:
    curr = check.pop(0)
    
    if curr in boxes:
      boxes.remove(curr)
      attended_boxes.append(curr)
      
      check.append((curr[0] + dx, curr[1] + dy))

      if box_lookup[curr] == "[":
        check.append((curr[0], curr[1] + 1))
      elif box_lookup[curr] == "]":
        check.append((curr[0], curr[1] - 1))

    elif curr in walls:
      moving = False
      break
  
  if moving:
    new_box_lookup = {}
    for k in list(box_lookup.keys()):
      if k in attended_boxes:
        new_box_lookup[(k[0] + dx, k[1] + dy)] = box_lookup[k]
      else:
        new_box_lookup[k] = box_lookup[k]
    
    box_lookup = new_box_lookup
      
    
    attended_boxes = [(x[0] + dx, x[1] + dy) for x in attended_boxes]
    
    robot[0] += dx
    robot[1] += dy
    
  boxes += attended_boxes

total = 0
for box in boxes:
  if box_lookup[box] == "[":
    total += box[0] * 100 + box[1]

print(total)