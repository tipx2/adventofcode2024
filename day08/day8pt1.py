with open("day08/input8.txt") as f:
  lines = [x.strip() for x in f.readlines()]

nodes = {}
for i, line in enumerate(lines):
  for j, letter in enumerate(line):
    if letter != ".":
      if letter not in nodes.keys():
        nodes[letter] = []
      nodes[letter].append((i, j))

antinodes = set()

for key in nodes.keys():
  for node1 in nodes[key]:
    for node2 in nodes[key]:
      if node1 == node2:
        continue
      
      di = node1[0] - node2[0]
      dj = node1[1] - node2[1]
      
      antinodes.add((node1[0] + di, node1[1] + dj))
      
      di *= -1
      dj *= -1
      
      antinodes.add((node2[0] + di, node2[1] + dj))

boundi = len(lines)
boundj = len(lines[0])

filtered = set(x for x in antinodes if 0 <= x[0] < boundi and 0 <= x[1] < boundj)

print(len(filtered))