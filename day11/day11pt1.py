with open("day11/input11.txt") as f:
  lines = [int(x) for x in f.read().strip().split(" ")]

for x in range(25):
  
  i = 0
  
  while i < len(lines):
    
    if lines[i] == 0:
      lines[i] = 1
      
    elif len(str(lines[i])) % 2 == 0:
      n = str(lines[i])
      j, k = n[:len(n)//2], n[len(n)//2:]
      
      lines[i] = int(j)
      lines.insert(i+1, int(k))
      i += 1
      
    else:
      lines[i] *= 2024
    
    i += 1

print(len(lines))
