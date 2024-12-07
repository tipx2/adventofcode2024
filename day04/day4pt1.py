with open("day04/input4.txt") as f:
  lines = [x.strip() for x in f.readlines()]

max_i = len(lines)
max_j = len(lines[0])

directions = [(-1,-1), (-1, 0), (1, 0), (1, 1), (0, 1), (0, -1), (-1, 1), (1, -1)]

xmas_count = 0

for i in range(len(lines)):
  for j in range(len(lines[i])):

    for direction in directions:
      
      found_xmas = True
      
      curr_i, curr_j = i, j
      
      for letter in "XMAS":
        if curr_i >= max_i or curr_i < 0 or curr_j >= max_j or curr_j < 0:
          found_xmas = False
          break
        elif lines[curr_i][curr_j] != letter:
          found_xmas = False
          break
        
        curr_i += direction[0]
        curr_j += direction[1]
      
      if found_xmas:
        xmas_count += 1

print(xmas_count)
    