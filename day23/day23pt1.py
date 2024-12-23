with open("day23/input23.txt") as f:
  twos = [tuple(x.strip().split("-")) for x in f.readlines()]

def get_overlap(a, b):
  
  if a[0] == b[0]:
    return (a[1], a[0], b[1])
  elif a[1] == b[0]:
    return (a[0], a[1], b[1])
  elif a[0] == b[1]:
    return (a[1], a[0], b[0])
  elif a[1] == b[1]:
    return (a[0], a[1], b[0])

threes = []

for item in twos:
  for item2 in twos:
    overlap = get_overlap(item, item2)
    if overlap != None:
      threes.append(overlap)

total = 0
for item in threes:
  if ((item[0], item[2]) in twos or (item[2], item[0]) in twos) and any([x.startswith("t") for x in item]):
    total += 1

print((total//3)//2) # just works lol