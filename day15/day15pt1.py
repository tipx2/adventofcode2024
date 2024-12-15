with open("day15/input15.txt") as f:
  r_map, instructions = f.read().split("\n\n")

instructions = instructions.replace("\n", "")

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
    elif letter == "O":
      boxes.append((i, j))
    elif letter == "@":
      robot = [i, j]


directions = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}

for inst in instructions:
  dx, dy = directions[inst]
  check = (robot[0] + dx, robot[1] + dy)
  
  moving = []
  while check in boxes:
    moving.append(check)
    boxes.remove(check)
    check = (check[0] + dx, check[1] + dy)
  
  if check in walls:
    boxes += moving
    continue
  else:
    robot[0] += dx
    robot[1] += dy
    boxes += [(x[0] + dx, x[1] + dy) for x in moving]

total = 0
for box in boxes:
  total += box[0] * 100 + box[1]

print(total)