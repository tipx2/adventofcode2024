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


movedIds = set()
maxFile = max(files)
bufend = len(files) - 1

while len(movedIds) != maxFile:
  
  fileId = files[bufend]
  
  if fileId == -1:
    bufend -= 1
    continue

  bufstart = files.index(fileId)
  buflen = bufend - bufstart + 1
  
  if fileId in movedIds:
    bufend = bufstart - 1
    continue
  else:
    movedIds.add(fileId)
  
  for x in range(len(files) - buflen + 1):
    if x > bufend:
      break
    if all([x == -1 for x in files[x:x+buflen]]):
      files[x:x+buflen] = [fileId] * buflen
      files[bufstart:bufstart+buflen] = [-1] * buflen
      break
  
  bufend = bufstart - 1


total = 0
for i, item in enumerate(files):
  if item != -1:
    total += item * i

print(total)