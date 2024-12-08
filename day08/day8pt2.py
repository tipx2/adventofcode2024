with open("day08/input8.txt") as f:
  lines = [x.strip() for x in f.readlines()]

nodes = {}
for i, line in enumerate(lines):
  for j, letter in enumerate(line):
    if letter != ".":
      if letter not in nodes.keys():
        nodes[letter] = []
      nodes[letter].append((i, j))


boundi = len(lines)
boundj = len(lines[0])

antinodes = set()
for key in nodes.keys():
  
  if len(nodes[key]) > 1:
    for node in nodes[key]:
      antinodes.add(node)
  
  
  for node1 in nodes[key]:
    for node2 in nodes[key]:
      if node1 == node2:
        continue
      
      di = node1[0] - node2[0]
      dj = node1[1] - node2[1]
      
      new_node = (node1[0] + di, node1[1] + dj)
      while 0 <= new_node[0] < boundi and 0 <= new_node[1] < boundj:
        antinodes.add(new_node)
        new_node = (new_node[0] + di, new_node[1] + dj)
      
      di *= -1
      dj *= -1
      new_node = (node2[0] + di, node2[1] + dj)
      while 0 <= new_node[0] < boundi and 0 <= new_node[1] < boundj:
        antinodes.add(new_node)
        new_node = (new_node[0] + di, new_node[1] + dj)


print(len(antinodes))