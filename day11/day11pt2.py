from collections import defaultdict, Counter
with open("day11/input11.txt") as f:
  lines = [int(x) for x in f.read().strip().split(" ")]

def evolve(n):
  
  if n == 0:
    return 1, None
    
  elif len(str(n)) % 2 == 0:
    n = str(n)
    j, k = n[:len(n)//2], n[len(n)//2:]
    
    return int(j), int(k)
    
  else:
    return n * 2024, None


# needed a bit of help to figure out this one
counter = Counter(lines)

for _ in range(75):
  values = list(counter.keys())
  new_counts = defaultdict(int)
  
  for item in values:
    a, b = evolve(item)
    if b is not None:
      new_counts[b] += counter[item]
    new_counts[a] += counter[item]
  
  counter = new_counts
    

print(sum(counter.values()))