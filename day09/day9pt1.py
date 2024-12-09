with open("day09/input9.txt") as f:
  line = f.read().strip()

files = []

isFile = True
currId = 0
for num in line:
  num = int(num)
  
  for _ in range(num):
    if isFile:
      files.append(currId)
    else:
      files.append(-1)
  
  if isFile:
    currId += 1
  
  isFile = not isFile

for i, item in enumerate(reversed(files)):
  if item == -1:
    continue
  files[files.index(-1)] = item
  
  files[len(files) - 1 - i] = -1

del files[0]

total = 0
for i, item in enumerate(files):
  if item != -1:
    total += item * i

print(total)